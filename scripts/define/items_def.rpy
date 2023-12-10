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
    
    # arrmory
    $ arrmory_wood = Armor(name="Берёзовые штаны", desc="Мама сшила мне штаны из берёзовой коры", defense=20, cost=100, icon="bronze_helmet.png")
    $ arrmory_kolk = Armor(name="Кольчуга", desc="Столько дырок сколько и в сюжете этой игры..", defense=60, cost=700, icon="silver_arr.png")
    $ arrmory_diamond = Armor(name="Алмазная броня", desc="Богатый?", defense=170, cost=2700, icon="blue_arr.png")
    $ arrmory_gold = Armor(name="Золотоя броня про", desc="Лучшая броня в мире", defense=320, cost=6000, icon="gold_arr.png")
    $ arrmory_god = Armor(name="Броня бога", desc="Кто-то раздел юй", defense=600, cost=15000, icon="god_arr.png")

    # Sworlds
    $ bronze_sworld = Weapon(name="Бронзовый меч", desc="Слабое оружие", cost=100, damage=12, icon="bronze_sworld.png")
    $ silver_sworld = Weapon(name="Серебряный меч", desc="Против вампиров", cost=500, damage=36, icon="silver_sworld.png")
    $ gold_sworld = Weapon(name="Золотой меч", desc="Еврей ебаный 14 урона", cost=2000, damage=76, icon="gold_sworld.png")
    $ emerald_sworld = Weapon(name="Емеральдовый клинок", desc="Ебаный еврей версия житель", cost=5500, damage=125, icon="emerald_sworld.png")
    $ obs_sworld = Weapon(name="Обсидиановый меч", desc="Собрав 12 таких можно вернутся в ад", damage=180, cost=15000, icon="obs_sworld.png")
    $ resinoviy_chlen = Weapon(name="Резиновый член", desc="Когда-то он пренадлижал Кириллу", damage=24, cost=1, icon="resinoviy_chlen.png")

    # assc
    $ ass_silver = Accessory(name="Серебренное кольцо", desc="Одевают на член", cost=100, bonus={"atk": 6, "def": 8}, icon="silver_acc.png")
    $ ass_blue = Accessory(name="Голубое кольцо", desc="Геи одевают на член", cost=650, bonus={"atk": 22, "def": 16}, icon="blue_acc.png")
    $ ass_demon = Accessory(name="Деманическое кольцо", desc="Король деманов сам его создал", cost=2500, bonus={"atk": 115, "def": -50}, icon="demon_acc.png")
    $ ass_red = Accessory(name="Ожелеье из боли", desc="Когда-то носил Денис", cost=9000, bonus={"atk": -50, "def": 95}, icon="red_acc.png")
    $ ass_oh = Accessory(name="Идеал", desc="Нету изьянов", cost=20000, bonus={"atk": 85, "def": 55}, icon="oh_acc.png")

    $ items = [
        arrmory_wood, arrmory_kolk, arrmory_diamond, arrmory_gold, arrmory_god,
        bronze_sworld, silver_sworld, gold_sworld, emerald_sworld, obs_sworld,
        ass_silver, ass_blue, ass_demon, ass_red, ass_oh,
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
