init python:
    def monstersFixed():
        global misstext
        global monsters_total
        global battle_monsters
        global m1
        global m2
        global m3
        global m4
        global m5
        global m6
        global m7
        global m8
        m1 = copy.deepcopy(empty)
        m2 = copy.deepcopy(empty)
        m3 = copy.deepcopy(empty)
        m4 = copy.deepcopy(empty)
        m5 = copy.deepcopy(empty)
        m6 = copy.deepcopy(empty)
        m7 = copy.deepcopy(empty)
        m8 = copy.deepcopy(empty)
        if fixedset == "set 1":
            m2 = copy.deepcopy(mon1)
            m3 = copy.deepcopy(mon2)
            m4 = copy.deepcopy(mon2)
            m5 = copy.deepcopy(mon3)
            m6 = copy.deepcopy(mon2)
            m7 = copy.deepcopy(mon1)
            battle_monsters = [m2,m3,m4,m5,m6,m7]
        elif fixedset == "zeleboba":
            m1 = copy.deepcopy(empty); m2 = copy.deepcopy(mon7); m3 = copy.deepcopy(mon10); m4 = copy.deepcopy(mon8)
            m5 = copy.deepcopy(mon8); m6 = copy.deepcopy(mon9); m7 = copy.deepcopy(mon9); m8 = copy.deepcopy(empty)
            battle_monsters = [m2,m3,m4,m5,m6,m7]
        elif fixedset == "lolis":
            m1 = copy.deepcopy(mon11); m2 = copy.deepcopy(mon13); m3 = copy.deepcopy(mon13); m4 = copy.deepcopy(mon11)
            m5 = copy.deepcopy(mon11); m6 = copy.deepcopy(mon12); m7 = copy.deepcopy(mon12); m8 = copy.deepcopy(mon11)
            battle_monsters = [m1,m2,m3,m4,m5,m6,m7,m8]
        elif fixedset == "lolisboss":
            m1 = copy.deepcopy(mon19); m2 = copy.deepcopy(mon14); m3 = copy.deepcopy(mon20); m4 = copy.deepcopy(mon19)
            m5 = copy.deepcopy(mon18); m6 = copy.deepcopy(mon17); m7 = copy.deepcopy(mon17); m8 = copy.deepcopy(mon18)
            battle_monsters = [m1,m2,m3,m4,m5,m6,m7,m8]
        elif fixedset == "finalpodval":
            m1 = copy.deepcopy(mon18); m2 = copy.deepcopy(ui22); m3 = copy.deepcopy(denis); m4 = copy.deepcopy(mon18)
            m5 = copy.deepcopy(mon16); m6 = copy.deepcopy(mon17); m7 = copy.deepcopy(mon17); m8 = copy.deepcopy(mon16)
            battle_monsters = [m1,m2,m3,m4,m5,m6,m7,m8]
        else:
            m1 = copy.deepcopy(mon1)
            battle_monsters = [m1]
        monsters_total = len(battle_monsters)
        for m in battle_monsters:
            if m.name:
                m._hp = m.hpmax

    def monstersRoll():
        global monsters_total
        global battle_monsters
        global m1
        global m2
        global m3
        global m4
        global m5
        global m6
        global m7
        global m8
        monsters_total = renpy.random.randint(1,8)
        m1 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m2 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m3 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m4 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m5 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m6 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m7 = copy.deepcopy(renpy.random.choice(wild_monsters))
        m8 = copy.deepcopy(renpy.random.choice(wild_monsters))
        battle_monsters = [m1,m2,m3,m4,m5,m6,m7,m8]
        total = monsters_total
        for m in battle_monsters:
            m._hp = m.hpmax
            m.dead = True
        for m in battle_monsters:
            if total > 0:
                m.dead = False
                total -= 1

    def monstersRollDef():
        global monsters_total
        global battle_monsters
        global m1
        global m2
        global m3
        global m4
        global m5
        global m6
        global m7
        global m8
        monsters_total = renpy.random.randint(1, 8)

        monsters = [copy.deepcopy(renpy.random.choice(wild_monsters)) for _ in range(monsters_total)]
        battle_monsters_real = [m for m in monsters if m is not empty]  
        battle_monsters = [empty] * 8 

        start_pos = 3
        if len(battle_monsters_real) >= 2:
            start_pos = 2
        if len(battle_monsters_real) >= 4:
            start_pos = 1
        if len(battle_monsters_real) >= 6:
            start_pos = 0

        battle_monsters_real.sort(key=lambda x: x.hpmax)

        first_monsters = battle_monsters_real[:len(battle_monsters_real)//2]
        end_monsters = battle_monsters_real[len(battle_monsters_real)//2:]
        battle_monsters[:4] = [empty] * start_pos + first_monsters[:len(first_monsters)] + [empty] * (4 - start_pos - len(first_monsters))
        battle_monsters[4:] = [empty] * start_pos + end_monsters[:len(end_monsters)] + [empty] * (4 - start_pos - len(end_monsters))
        
        print(battle_monsters)

        total = monsters_total
        m1, m2, m3, m4, m5, m6, m7, m8 = battle_monsters
        battle_monsters = [
            monster for monster in [m1, m2, m3, m4, m5, m6, m7, m8] if monster is not empty
        ]

        for m in battle_monsters:
            if m.name:
                m._hp = m.hpmax

    def asignPos():
        monster_slot[0].sprite_pos = 0
        monster_slot[1].sprite_pos = 256
        monster_slot[2].sprite_pos = 512
        monster_slot[3].sprite_pos = 768
        monster_slot[4].sprite_pos = 0
        monster_slot[5].sprite_pos = 256
        monster_slot[6].sprite_pos = 512
        monster_slot[7].sprite_pos = 768
        monster_slot[0].dmg_pos = (576,320)
        monster_slot[1].dmg_pos = (832,320)
        monster_slot[2].dmg_pos = (1088,320)
        monster_slot[3].dmg_pos = (1344,320)
        monster_slot[4].dmg_pos = (576,512)
        monster_slot[5].dmg_pos = (832,512)
        monster_slot[6].dmg_pos = (1088,512)
        monster_slot[7].dmg_pos = (1344,512)

    def swapSlot(old_slot, new_slot):
        renpy.hide_screen("display_monsters")
        monster_slot[old_slot], monster_slot[new_slot] = monster_slot[new_slot], monster_slot[old_slot]
        asignPos()
        renpy.show_screen("display_monsters")

    def partyRevive():
        for c in party_list:
            if c.dead == True:
                c.dead = False
                c._hp = 1

    def restorehp():
        a._hp = a.hpmax
        for c in party_list:
            c._hp = c.hpmax

    def restoremp():
        a._mp = a.mpmax
        for c in party_list:
            c._mp = c.mpmax

    def startPlayersTurn():
        for p in battle_players:
            p.turn = False
            p.defending = False

    def endTurn():
        global currentplayer
        global target
        global hp_lost
        global mp_lost
        global dropitem
        global message
        global misstext
        message = "other_skill"
        misstext = renpy.random.choice(misstext_list)
        if isinstance(b_skill, Skill):
            b_skill.useSkill(currentplayer)
        elif isinstance(b_skill, Item):
            useItem(b_skill)
        if target == "all":
            atkAll()
        if target == "enemy" or target == "row":
            atkEnemy()
        if target == "ally":
            atkAlly()
        if target == "self":
            atkSelf()
        if target == "ko":
            atkAlly()
        if target == "attack":
            Attack()
        if target == "defend":
            message = "defend"
            Defend()
        currentplayer.turn = True
        currentplayer._mp -= mp_lost
        currentplayer._hp -= hp_lost
        player_inv.drop(dropitem)
        renpy.pause(see_attack_speed * 2, hard=True)
        playersChk()
        renpy.hide_screen("monster_dmg")

    def startTurn():
        global damage
        global effects
        global mpdmg
        global mp_lost
        global hp_lost
        global atk_sfx
        global target
        global message
        global picked_targs
        global hit_t
        global missed_t
        global skill_t
        global dropitem
        global row1btn
        global row2btn
        row1btn = False
        row2btn = False
        target = "enemy"
        message = "skill"
        damage = 0
        mpdmg = 0
        mp_lost = 0
        hp_lost = 0
        atk_sfx = None
        dropitem = None
        picked_targs = []
        hit_t = [] 
        effects = []
        missed_t = []
        skill_t = []

    def playersCnt():
        global players
        global alive_players
        players = 0
        alive_players = []
        for p in battle_players:
            if p.hp > 0:
                p.dead = False
                players += 1
                alive_players.append(p)

    def playersChk():
        global message
        global koplayer
        global battleEnd
        global monsters_dead
        global msg_mons
        global win
        for p in battle_players:
            if p.hp <= 0 and not p.dead:
                renpy.pause(see_attack_speed)
                p.dead = True
                koplayer = p.name
                message = "player_ko"
                renpy.pause(attack_speed)
        for m in battle_monsters:
            if m.hp <= 0 and not m.dead:
                m.state = "dying"
                msg_mons = m.name
                message = "m_dead"
                renpy.play(sfx_monsterdead.draw())
                renpy.pause(kill_speed)
                message = "none"
                monsters_dead += 1
                m.dead = True
        if all(p.hp == 0 for p in battle_players):
            battleEnd = True
        if monsters_dead == monsters_total:
            message = "you_win"
            win = True
            battleEnd = True

    def getImage(i):
        if isinstance(i, Monster):
            return "images/monsters/"+ i.img+".png"
        if isinstance(i, Skill):
            return "images/skills/" + i.img + ".png"

    def playerAction(p):
        if not battleEnd and not p.turn and not p.dead:
            if renpy.get_screen("turn_select"):
                return Return(p)
            else:
                return NullAction()
        else:
            return NullAction()

    def runEvent():
        global eventrunning
        eventrunning = True
        config.allow_skipping = True
        config.rollback_enabled = True
        renpy.choice_for_skipping()
        renpy.hide_screen("tooltip")
        renpy.retain_after_load()
    def stopEvent():
        global eventrunning
        eventrunning = False
        config.allow_skipping = False
        config.rollback_enabled = False
        renpy.block_rollback()
        renpy.choice_for_skipping()
        preferences.afm_enable = False

default fixedset = None
default tt_timer = False
default damage = 0
default m_damage = 0
default dropitem = None
default atk_sfx = None
default mp_lost = 0
default hp_lost = 0
default players = 1
default monsters_total = 0
default monsters_dead = 0

default b_skill = "none"
default message = "none"
default target = "none"

default picked_targs = []
default party_list = []
default wild_monsters = []
default battle_players = []
default alive_players = []
default battle_monsters = []
default reserve_monsters = []
default misstext_list = ["Промазал!", "Не попал!", "Лох пормазал!", "Я ЖЕ БЛЯТЬ СТРЕЛЯЛ!", "Мимо", "Мимо?", "Да ты снайпер"]

default diss = Dissolve(.2)

# ACTIVE SKILLS (name, pwr, mp_cost, sfx, targ, targs, type='active', trans=None, img=None, back_row=False)

# База
default defenseup = ActiveSkill("Улучшить щит", 0, 25, "defend", "self") # use is in skill_effects

# Уник магия
default doubleattack = ActiveSkill("Двойная атака", 0, 25, "sword", "enemy", 2, img="double_attack") # two enemy targets
default attackall = ActiveSkill("Атаковать всех", 15, 75, "rock", "all", img="swordofdeath") # targets all enemies
default giftofangels = ActiveSkill("Подарок с небес", -3, 20, "heal", "ally", 2, img="giftofangels")
default loved = ActiveSkill("Влюбить 2 врагов", 3, 30, "ice", "enemy", 2, img="iceball") # attacks whole row
default souldrain = ActiveSkill("Секс рабство", 20, 60, "acid", img="souldrain")
default souldrain2 = ActiveSkill("Похищение", 2, 50, "acid", img="souldrain")

# Магия предметов
default cumshot = ActiveSkill("Кончить", 0, 25, "cum", "enemy", 2, img="arrowhail") # two enemy targets
# default cumshot = ActiveSkill("Тройной удар", 99999, 25, "sword", "enemy", 2, img="arrowhail") # two enemy targets
# default cumshot = ActiveSkill("Ядовитое лезвие", 0, 25, "sword", "enemy", 2, img="arrowhail") # two enemy targets
# default cumshot = ActiveSkill("Огненое лезвие", 0, 25, "sword", "enemy", 2, img="arrowhail") # two enemy targets
# default cumshot = ActiveSkill("Оглушение", 0, 25, "sword", "enemy", 2, img="arrowhail") # two enemy targets

# Полученная магия
default mindfreeze = ActiveSkill("Леденой шар", 7, 20, "ice", img="iceball", effects=[заморозка])
default mindfire = ActiveSkill("Огненный шар", 14, 35, "fire", img="asteroid")
default magicheal = ActiveSkill("Исцеление", -6, 25, "heal", "self", img="mindburn") # negative pwr to heal
default arrowhail = ActiveSkill("Обстрел", 10, 40, "bow", "all", img="arrowhail", back_row=True)
default lavaburst = ActiveSkill("Лавовой взрыв", 16, 55, "fire", img="lavaburst")
default swordofdeath = ActiveSkill("Голое фото дениса", 30, 100, "sword", img="hellrage", cost=0)
default spikeshield = ActiveSkill("Колючий щит", 4, 40, "block", "all", img="spikeshield")
default magicswap = ActiveSkill("Смена позиции", 0, 15, "heal", "enemy", 2, back_row=True, img="rockthrow") # can target back row
default lovedefence = ActiveSkill("Ослабить уровень", 0, 15, "lovedefence", "enemy", back_row=True, img="mindblast") # can target back row

# Проклятая магия
default meteorshower = ActiveSkill("Метеоритный дождь", 10, 70, "rock", "all", img="meteorshower", cost=12000)
default hellrage = ActiveSkill("Адская ярость", 14, 80, "fire", "all", img="deathmissile", cost=20000)
default lifedrain = ActiveSkill("Отсасование жизни", 10, 50, "acid", img="lifedrain", cost=10000)
default devastationbeam = ActiveSkill("Луч опустошения", 4, 45, "fire", "all", img="devastationbeam", cost=15000)
default energybeams = ActiveSkill("Энергетические лучи", 5, 50, "thunder", "all", img="energybeams", cost=16000)

default thunderbolt = ActiveSkill("Thunderbolt", 6, 10, "thunder", "enemy", 3, img="thunderbolt", back_row=True)
default asteroid = ActiveSkill("Asteroid", 5, 5, "rock", img="asteroid")
default rockthrow = ActiveSkill("Rock Throw", 4, 40, "rock", "enemy", 2, back_row=True, img="rockthrow")
default circleofhealing = ActiveSkill("Circle of Healing", -10, 10, "heal", "ally", img="circleofhealing")
default mindburn = ActiveSkill("Mindburn", 5, 15, "fire", img="mindburn")
default mindblast = ActiveSkill("Mindblast", 6, 5, "thunder", img="mindblast")
default deathmissile = ActiveSkill("Death Missile", 7, 45, "rock", img="deathmissile")

# Магия брони
default nike_pro_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="nike_pro_skill") 
default dead_slime_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="dead_slime_skill")

default banana_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="banana_skill")
default list_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="list_skill")
default gold_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="gold_skill")
default capert_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="capert_skill")
default god_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="god_skill")
default black_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="black_skill")
default ice_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="ice_skill")
default druid_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="druid_skill")

default magic_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="magic_skill")
default woin_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="woin_skill")
default adic_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="adic_skill")
default dildo_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="dildo_skill")
default feja_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="feja_skill")

# Магия оружия
default resinoviy_chlen_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="resinoviy_chlen_skill")

default kulak_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="kulak_sworld_skill")
default zerkalo_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="zerkalo_sworld_skill")

default gold_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="gold_sworld_skill")
default bow_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="bow_sworld_skill")
default sheild_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="sheild_sworld_skill")
default ice_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="ice_sworld_skill")
default klin_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="klin_sworld_skill")
default poduszka_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="poduszka_sworld_skill")

default vibrator_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="vibrator_sworld_skill")
default knut_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="knut_sworld_skill")

default obs_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="obs_sworld_skill")
default biblia_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="biblia_sworld_skill")
default doom_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="doom_sworld_skill")
default czerep_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="czerep_sworld_skill")
default ices_sworld_skill = ActiveSkill("Слабый удар", 7, 20, "ice", img="ices_sworld_skill")

# Аксы
default assc_list_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_list_skill")
default assc_zeleboba_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_zeleboba_skill")

default assc_gold_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_gold_skill")
default assc_lune_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_lune_skill")
default assc_bb_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_bb_skill")
default assc_roshen_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_roshen_skill")
default assc_sans_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_sans_skill")
default assc_prizrak_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_prizrak_skill")
default assc_cum_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_cum_skill")
default assc_mes_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_mes_skill")

default assc_photo_album_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_photo_album_skill")
default assc_hell_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_hell_skill")
default assc_prisma_skill = ActiveSkill("Защита брони", 0, 25, "defend", "self", img="assc_prisma_skill")

default magics = [
    meteorshower, hellrage, lifedrain, devastationbeam, energybeams
]

label lb_by_magic(magic, free=False):
    if not free:
        $ player_inv.money -= magic.cost
    hide screen by_magic
    hide screen magic_shop_menu
    $ player_inv.take_skill(magic)
    # menu select_player:
        # "Кого вы хотите научить [magic.name]?"
        # "[name]" if not len(a.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\n{1} изучил магию {2}".format(persistent.user_name, name, magic.name))
            # $ a.addSkill(magic)
        # "Макс" if maks in party_list and not len(maks.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\nМакс изучил магию {1}".format(persistent.user_name, magic.name))
            # $ maks.addSkill(magic)
        # "Саша" if sasha in party_list and not len(sasha.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\nСаша изучил магию {1}".format(persistent.user_name, magic.name))
            # $ sasha.addSkill(magic)
        # "Кирилл" if lox in party_list and not len(lox.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\nКирилл изучил магию {1}".format(persistent.user_name, magic.name))
            # $ lox.addSkill(magic)
        # "Любимый" if maksim in party_list and not len(maksim.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\nЛюбимый изучил магию {1}".format(persistent.user_name, magic.name))
            # $ maksim.addSkill(magic)
        # "Тянка" if tanka in party_list and not len(tanka.skills) >= 8:
            # $ OneDiscordMessage("# Глава 1 🔮\nТянка изучил магию {1}".format(persistent.user_name, magic.name))
            # $ tanka.addSkill(magic)




# Скрытая



# PASSIVE SKILLS (name, sfx=None, img=None, trans=None, lvl=0)
default pas_mask = PassiveSkill("Хилинг", "Пасивно вылизывает совё очко", act=pas_mask_akt)
default pas_sasha = PassiveSkill("Получатель пизды", "С большим шанцом враги атакуют его", "heal") 
default pas_boris = PassiveSkill("Алкоголик", "Пасивно бухает", "heal")
default pas_lox = PassiveSkill("Passive Skill 2", "", "heal") 
default pas_sanek = PassiveSkill("Passive Skill 1", "", "heal")
default pas_tanka = PassiveSkill("Passive Skill 2", "", "heal") 
default pas_maksim = PassiveSkill("Passive Skill 2", "", "heal") 