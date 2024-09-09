default cookbook = list()
default inv = Inventory("Inventory")

label load_items:
    $ cookbook = list()
    $ player_inv = Inventory("[a.name]")
    # var = Item(name, desc, icon=False, value=0, act=Show("inventory_popup", message="Nothing happened!"), type="item", recipe=False, tags={})
    $ hpotion = Item("Малое лечебное зелье", "Востанавливает 30 хп", 50, "hpotion.png", 20, type="cons", tags={'pwr': -30,'sfx': "potion"})
    $ bighpotion = Item("Большое лечебное зелье", "Востанавливает 100 хп", 150, "bighpotion.png", 20 , type="cons", tags={'pwr': -100,'sfx': "potion"})
    
    $ comboheal = Item("Комбо меню", "Востанавливает 20 маны и 20 хп", 50, "comboheal.png", 20, type="cons", tags={'mp': -50,'sfx': "potion"})

    $ mpotion = Item("Манная каша", "Востанавливает 50 маны", 50, "mpotion.png", 20, type="cons", tags={'mp': -50,'sfx': "potion"})
    $ bigmpotion = Item("Большая манная каша", "Востанавливает 100 маны", 150, "bigmpotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    
    $ shieldpotion = Item("Зелье железной кожи", "Повышает защиту", 150, "shieldpotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    $ doublepotion = Item("Зелье повтора", "Даёт возможность походить 2 раза за одного персонажа", 150, "doublepotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    
    $ firepotion = Item("Зелье огнестойкости", "Вас не могут поджечь 5 ходов", 150, "firepotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    $ friezpotion = Item("Зелье теплоты", "Вас не могут заморозить 5 ходов", 150, "friezpotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})
    
    $ rpotion = Item("Второй шанц", "Воскрешает умершего", 450, "rpotion.png", 300, type="cons", tags={'pwr': -200,'sfx': "potion",'targ': "ko"})
    $ rpotions = Item("Третий шанц ZOV", "Воскрешает весь отряд", 450, "rpotions.png", 300, type="cons", tags={'pwr': -200,'sfx': "potion",'targ': "ko"})
    
    $ yadpotion = Item("Ядовитый яд", "Выпев его можно умереть", 150, "yadpotion.png", 20, type="cons", tags={'mp': -100,'sfx': "potion"})

    $ bow = Weapon(name="Ебейший лук", desc="A sharp sword", cost=100, damage=199, icon="bronze_sworld.png")
    $ pizdezbow = Weapon(name="Ещё более Ебейший лук", desc="A sharp sword", cost=100, damage=1999)
    
    # arrmory
    ## 1 act
    $ arrmory_kora = Armor(
        name="Порватые трусы",
        desc="Столько дырок сколько и в сюжете этой игры..",
        defense=60, cost=700,
        icon="silver_arr.png")
    $ arrmory_pants = Armor(
        name="Берёзовые штаны",
        desc="Мама сшила мне штаны из берёзовой коры",
        defense=20, cost=100,
        icon="bronze_helmet.png")
    
    $ arrmory_lists = Armor(
        name="Броня из листочков",
        desc="Идеальный камуфляж в лесу",
        dependencies = [arrmory_kora, arrmory_pants],
        defense=60, cost=700,
        icon="silver_arr.png")
    $ arrmory_hot_pants = Armor(
        name="Горячие плавки",
        desc="Настолько горячие что вас не могут заморозить 😎",
        dependencies = [arrmory_kora, arrmory_pants],
        defense=20, cost=100,
        icon="bronze_helmet.png")

    $ arrmory_nike_pro = Armor(
        name="Nike Pro",
        desc="А у тебя щовел или персик?",
        dependencies = [arrmory_lists, arrmory_hot_pants],
        defense=20, cost=100,
        icon="bronze_helmet.png")
    $ arrmory_dead_slime = Armor(
        name="Мёртвый слизень",
        desc="Липкий и не приятный, но возможно он поглатит удар",
        defense=20, cost=100,
        icon="bronze_helmet.png")
    ## 2 act
    $ arrmory_banana = Armor(
        name="Сладенький бананчик",
        desc="Не резиновый член, но тоже вкусный",
        descending = [arrmory_nike_pro, arrmory_dead_slime],
        defense=20, cost=100,
        icon="bronze_helmet.png")
    $ arrmory_list = Armor(
        name="Листочик",
        desc="Легко рвётсья, но стоит его сложить..",
        descending = [arrmory_nike_pro, arrmory_dead_slime],
        defense=20, cost=100,
        icon="bronze_helmet.png")

    $ arrmory_gold = Armor(
        name="Золотая броня",
        desc="Золото это не только деньги, но и защита",
        descending = [arrmory_banana, arrmory_list],
        defense=20, cost=100,
        icon="bronze_helmet.png")
    $ arrmory_capert = Armor(
        name="Плащь невидимка",
        desc="Надев его вы становитесь невидимыми, монжо трахнуть Дениса",
        descending = [arrmory_banana, arrmory_list],
        defense=20, cost=100,
        icon="bronze_helmet.png")

    $ arrmory_god = Armor(
        name="Священная защита",
        desc="Бог Юй благослоил эту броню",
        descending = [arrmory_banana, arrmory_list],
        defense=20, cost=100,
        icon="bronze_helmet.png")
    $ arrmory_black = Armor(
        name="Астральная броня",
        desc="Негры сделали эту броню, некоторые говорят что она проклята",
        descending = [arrmory_banana, arrmory_list],
        defense=20, cost=100,
        icon="bronze_helmet.png")

    $ arrmory_black = Armor(
        name="Леденая броня",
        desc="Её защита равняеться холоду души 💙",
        descending = [arrmory_banana, arrmory_list],
        defense=20, cost=100,
        icon="bronze_helmet.png")
    ## 3 act

    # sworlds
    ## 1 act
    $ palka_sworld = Weapon(
        name="Палка",
        desc="Раз в год и палка стреляет",
        cost=100, damage=12,
        icon="palka_sworld.png")
    $ rogatka_sworld = Weapon(
        name="Рогатка",
        desc="Было бы круто если бы она стреляла, но увы нету снарядов.",
        cost=500, damage=36,
        icon="rogatka_sworld.png")
    
    $ lesh_sworld = Weapon(
        name="Лещ",
        desc="Если дать человеку рыбу, он будет сыт один день. Если дать человеку лещ, он пойдёт нахуй.",
        cost=500, damage=36,
        icon="lesh_sworld.png")
    $ samoletik_sworld = Weapon(
        name="Самолётик",
        desc="Истребитель который может уничтожить всё живое, если бы умел летаь. Он перестал летать после того как на нём поставили X.",
        cost=500, damage=36,
        icon="samoletik_sworld.png")
    
    $ kulak_sworld = Weapon(
        name="Слабый кулак",
        desc="Может его удары и слабы, но он понижает защиту врагов.",
        cost=500, damage=36,
        skill=kulak_sworld_skill,
        icon="kulak_sworld.png")
    $ zerkalo_sworld = Weapon(
        name="Зеркало правды",
        desc="Если посмотреть в него можно увидеть истенного себя.",
        cost=500, damage=36,
        skill=zerkalo_sworld_skill,
        icon="zerkalo_sworld.png")

    ## 2 act
    $ gold_sworld = Weapon(
        name="Золотой меч",
        desc="Еврей ебаный 14 урона",
        cost=2000, damage=76,
        skill=gold_sworld_skill,
        icon="gold_sworld.png")
    $ bow_sworld = Weapon(
        name="Лук",
        desc="Жаль не ебейщий лук, он тоже вкусный 🧅",
        cost=5500, damage=125,
        skill=bow_sworld_skill,
        icon="bow_sworld.png")
    
    $ sheild_sworld = Weapon(
        name="Щит",
        desc="Крестоносец ебучий",
        cost=5500, damage=125,
        skill=sheild_sworld_skill,
        icon="sheild_sworld.png")
    $ ice_sworld = Weapon(
        name="Сосулька XXXS",
        desc="Такой длинннной сосульки ещё не кто не видел",
        cost=5500, damage=125,
        skill=ice_sworld_skill,
        icon="ice_sworld.png")
    
    $ klin_sworld = Weapon(
        name="Кинжал",
        desc="Быстрый и сильный",
        cost=5500, damage=125,
        skill=klin_sworld_skill,
        icon="klin_sworld.png")
    $ poduszka_sworld = Weapon(
        name="Подушка",
        desc="На вид не отлечить от обычной, но она сделана из бетона",
        cost=5500, damage=125,
        skill=poduszka_sworld_skill,
        icon="poduszka_sworld.png")

    $ vibrator_sworld = Weapon(
        name="Вибратор",
        desc="Возбуждает, штука прикольная. Лолям нравиться.",
        cost=5500, damage=125,
        skill=vibrator_sworld_skill,
        icon="vibrator_sworld.png")
    $ knut_sworld = Weapon(
        name="Кнут",
        desc="После использования остаютсья порезы. Ним когда-то били Дениса.",
        cost=5500, damage=125,
        skill=knut_sworld_skill,
        icon="knut_sworld.png")

    ## 3 act 
    $ obs_sworld = Weapon(
        name="Обсидиановый меч",
        desc="Собрав 12 таких можно вернутся в ад",
        damage=180, cost=15000,
        skill=obs_sworld_skill,
        icon="obs_sworld.png")
    $ biblia_sworld = Weapon(
        name="Библия",
        desc="Уверуй в бога атеист ебаный, почему? Тебя ебать не должно, большие города",
        damage=180, cost=15000,
        skill=biblia_sworld_skill,
        icon="biblia_sworld.png")
    $ doom_sworld = Weapon(
        name="Doom slayer sword",
        desc="Идеальное оружие для истребление нечести",
        damage=180, cost=15000,
        skill=doom_sworld_skill,
        icon="doom_sworld.png")
    $ czerep_sworld = Weapon(
        name="Череп Дениса",
        desc="В какой-то день Денис понял что череп ему не нужен и он его выкинул. Поэтому у него такая форма лица\nВ этом оружии запечата страшная магия.",
        damage=180, cost=15000,
        skill=czerep_sworld_skill,
        icon="doom_sworld.png")
    $ ices_sworld = Weapon(
        name="Меч Эсдес",
        desc="Перед смертью Эсдес она создала меч, в который запечатала всю свою силу.\nСамое холодное оружие.",
        damage=180, cost=15000,
        skill=ices_sworld_skill,
        icon="ices_sworld.png")
    
    $ resinoviy_chlen = Weapon(
        name="Резиновый член",
        desc="Когда-то он пренадлижал Кириллу",
        damage=24, cost=1,
        skill=resinoviy_chlen_skill,
        icon="resinoviy_chlen.png")

    # assc

    ## 1 act

    ## 2 act

    ## 3 act 

    $ ass_silver = Accessory(name="Серебренное кольцо", desc="Одевают на член", cost=100, bonus={"atk": 6, "def": 8}, icon="silver_acc.png")
    $ ass_blue = Accessory(name="Голубое кольцо", desc="Геи одевают на член", cost=650, bonus={"atk": 22, "def": 16}, icon="blue_acc.png")
    $ ass_demon = Accessory(name="Деманическое кольцо", desc="Король деманов сам его создал", cost=2500, bonus={"atk": 115, "def": -50}, icon="demon_acc.png")
    $ ass_red = Accessory(name="Ожелеье из боли", desc="Когда-то носил Денис", cost=9000, bonus={"atk": -50, "def": 95}, icon="red_acc.png")
    $ ass_oh = Accessory(name="Идеал", desc="Нету изьянов", cost=20000, bonus={"atk": 85, "def": 55}, icon="oh_acc.png")

    $ items = [
        palka_sworld, rogatka_sworld, lesh_sworld, samoletik_sworld, kulak_sworld, zerkalo_sworld,
        gold_sworld, bow_sworld, sheild_sworld, ice_sworld, klin_sworld, poduszka_sworld, vibrator_sworld, knut_sworld,
        obs_sworld,biblia_sworld,doom_sworld,czerep_sworld,ices_sworld,
        hpotion, bighpotion, mpotion, bigmpotion, rpotion
    ]

    $ player_inv.take(hpotion)
    $ player_inv.take(bighpotion)
    
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
