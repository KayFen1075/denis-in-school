default cookbook = list()
default inv = Inventory("Inventory")

label load_items:
    $ cookbook = list()
    $ player_inv = Inventory("[a.name]")
    # var = Item(name, desc, icon=False, value=0, act=Show("inventory_popup", message="Nothing happened!"), type="item", recipe=False, tags={})
    $ hpotion = Item("Малое лечебное зелье", "Востанавливает 30 хп", 50, "heal.png", 20, type="cons", tags={'pwr': -30,'sfx': "potion"})
    $ bighpotion = Item("Большое лечебное зелье", "Востанавливает 100 хп", 150, "big_heal.png", 20 , type="cons", tags={'pwr': -100,'sfx': "potion"})
    $ mpotion = Item("Манная каша", "Востанавливает 50 маны", 50, "mpotion.webp", 20, type="cons", tags={'mp': -50,'sfx': "potion"})
    $ bigmpotion = Item("Большая манная каша", "Востанавливает 100 маны", 150, "mpotion.webp", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    $ rpotion = Item("Второй шанц", "Воскрешает умершего", 450, "revive.webp", 300, type="cons", tags={'pwr': -200,'sfx': "potion",'targ': "ko"})

    $ bow = Weapon(name="Ебейший лук", desc="A sharp sword", cost=100, damage=199, icon="bronze_sworld.png")
    $ pizdezbow = Weapon(name="Ещё более Ебейший лук", desc="A sharp sword", cost=100, damage=1999)
    $ shield = Armor(name="Shield", desc="A sturdy shield", defense=35, cost=100, icon="bronze_helmet.png")
    $ shield2 = Armor(name="Золотой нагрудник", desc="Просто крутой", defense=35, cost=100, icon="bronze_helmet.png")
    
    # Sworlds
    
    $ bronze_sworld = Weapon(name="Бронзовый меч", desc="Слабое оружие", cost=100, damage=6, icon="bronze_sworld.png")
    $ silver_sworld = Weapon(name="Серебряный меч", desc="Против вампиров", cost=250, damage=15, icon="silver_sworld.png")
    $ gold_sworld = Weapon(name="Золотой меч", desc="Еврей ебаный 14 урона", cost=500, damage=24, icon="gold_sworld.png")
    $ emerald_sworld = Weapon(name="Емеральдовый клинок", desc="Ебаный еврей версия житель", cost=1000, damage=37, icon="emerald_sworld.png")
    $ obs_sworld = Weapon(name="Обсидиановый меч", desc="Собрав 12 таких можно вернутся в ад", damage=56, cost=2500, icon="obs_sworld.png")
    
    $ ring = Accessory(name="Ring", desc="A magical ring", cost=100, bonus={"atk": -10, "def": 50}, icon="bronze_sworld.png")

    $ items = [
        bronze_sworld, silver_sworld, gold_sworld, emerald_sworld, obs_sworld,
        shield, shield2,
        ring,
        hpotion, bighpotion, mpotion, bigmpotion, rpotion
    ]

    $ player_inv.take(hpotion)
    $ player_inv.take(bighpotion)

    "Загруска предметов завершена"
    return
    
init python:
    def getTarget(i):
        if 'targ' in i.tags:
            return i.tags['targ']
        else:
            return "self"

    def itemUsable(i):
        if getTarget(i) == "ko":
            deadplayers = 0
            for p in battle_players:
                if p.dead:
                    deadplayers += 1
            if deadplayers > 0:
                return True
            else:
                return False
        else:
            return True

    def useItem(i):
        global damage
        global mpdmg
        global mp_lost
        global atk_sfx
        global currentplayer
        global recover_hp
        global target
        global s_trans
        global msg_skill
        if 'targ' in i.tags:
            target = i.tags['targ']
        else:
            target = "self"
        if 'trans' in i.tags:
            s_trans = i.tags['targ']
        else:
            s_trans = None
        if 'pwr' in i.tags:
            damage = i.tags['pwr']
        if 'mp' in i.tags:
            mpdmg = i.tags['mp']
        atk_sfx = "audio/items/" + i.tags['sfx'] + ".ogg"
        msg_skill = i.name

screen inventory_inbattle(first_inventory):
    key "mouseup_3" action Hide("inv_tooltip"), Jump("player_skill")
    default crafting_screen = False
    tag menu
    modal True
    frame:
        style_group "invstyle"
        hbox:
            pos 10,10
            spacing 50
            vbox:
                label first_inventory.name
                use inventory_battleview(first_inventory)
                use view_nav(first_inventory)
                textbutton "Отмена" action Jump("player_skill")

screen inventory_battleview(inventory):
    side "c r":
        style_group "invstyle"
        area (0, 0, 700, 500)
        vpgrid id ("vp"+inventory.name):
            draggable True
            mousewheel True
            xsize 700 ysize 500
            if inventory.grid_view:
                cols 3 spacing 10
            else:
                cols 1 spacing 25
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])
                if item[0].type=="cons" and itemUsable(item[0]):
                    hbox:
                        $ icon = "images/inv/" + item[0].icon
                        $ hover_icon = im.Sepia(icon)
                        imagebutton:
                            idle LiveComposite((192,192), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((192,192), (0,0), hover_icon, (0,0), Text(qty))
                            action SetVariable("dropitem", item[0]), Return(item[0])
                            hovered Show("inv_tooltip",item=item)
                            unhovered Hide("inv_tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                text "[desc]"

            ## maintains spacing in empty inventories.
            if len(inventory.inv) == 0:
                add Null(height=192,width=192)

        vbar value YScrollValue("vp"+inventory.name)
