label battle:
    hide screen world_time
    $ stopEvent()
    if fixedset:
        $ monstersFixed()
        $ monster_slot = [m1,m2,m3,m4,m5,m6,m7,m8]
        $ fixedset = None
    else:
        $ monstersRoll()
        $ monster_slot = [m1,m2,m3,m4,m5,m6,m7,m8]
        $ renpy.random.shuffle(monster_slot)
    $ asignPos()
    $ row1btn = False
    $ row2btn = False
    $ missed_t = []
    $ win = False
    $ battleEnd = False
    $ monsters_dead = 0
    $ currentplayer = None
    show screen battle_tooltip

    call battle_music

    random:
        scene bb1
        scene bb2
        scene bb3
    with pixellate
    if not first_pola:
        show px
        with dissolve
        x "Это место для боя{w}, выбери себе команду"
        x "С ней будет проще сражаться"
        hide px
        with dissolve
    call player_select
    show screen display_monsters with diss
    show screen battle_message
    show screen battle_overlay with diss
    if not first_pola:
        show px
        with dissolve
        x "Вот и они"
        x "У врагов нету жизней{w}, они состоят из маны"
        x "По этому атакуя ты понижаешь их жизненную энергию"
        x "Выбери кем будешь атаковать и способность"
        hide px
        with dissolve
    jump battling

label player_select:
    $ battle_players = [a]
    $ a.img_pos = 512
    $ a.bar_pos = 944
    $ a.dmg_pos = 1136
    call screen select_p1
    if _return != "none":
        $ p1 = _return
        $ battle_players.append(p1)
        $ p1.img_pos = 0
        $ p1.bar_pos = 432
        $ p1.dmg_pos = 624
    else:
        $ p1 = None
    call screen select_p2
    if _return != "none":
        $ p2 = _return
        $ battle_players.append(p2)
        $ p2.img_pos = 1024
        $ p2.bar_pos = 1456
        $ p2.dmg_pos = 1648
    else:
        $ p2 = None
    return

screen select_p1():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "Выбрать напарника"
            for c in party_list:
                if c != a:
                    textbutton "[c.name]" xalign 0.5 action Return(c)
            textbutton "Без напарника" xalign 0.5 action Return("none")

screen select_p2():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "Выбрать второго напарника"
            for c in party_list:
                if c != p1 and c != a:
                    textbutton "[c.name]" xalign 0.5 action Return(c)
            textbutton "Без напарника" xalign 0.5 action Return("none")

screen battle_tooltip():
    zorder 20
    $ tooltip = GetTooltip()
    if tooltip:
        timer 1 action SetVariable("tt_timer", True)
        if tt_timer:
            add MouseTooltip()
            $ mouse_pos = renpy.get_mouse_pos()
            $ renpy.set_mouse_pos(mouse_pos[0], mouse_pos[1])
    else:
        timer 0.001 action SetVariable("tt_timer", False)

screen battle_overlay():
    fixed:
        xoffset 192
        for p in battle_players:
            if currentplayer == p:
                add p.img + "_battle" yalign 1.05 xpos p.img_pos at char_sway
            else:
                imagebutton:
                    focus_mask True
                    yalign 1.1 xpos p.img_pos
                    idle p.img + "_battle"
                    tooltip "{0}\nATK: {1}\nDFN: {2}\n{3}".format(p.name, p.atk, p.dfn, p.p_skills[0].name)
                    action  Function(playerAction(p))
            fixed:
                pos p.bar_pos, 896
                vbox:
                    if currentplayer == p:
                        text "[p.name!u]" anchor (1.0,1.0) xoffset 110 style_group "battle_playername" color "#ffcc66"
                    else:
                        text "[p.name!u]" anchor (1.0,1.0) xoffset 110 style_group "battle_playername"
                    text "LVL.[p.lvl] " anchor (1.0,1.0) yoffset -12 xoffset 120 style_group "battle_playerlvl"
                    fixed:
                        yoffset -24
                        bar style "bar_hp" value AnimatedValue(value=p.hp, range=p.hpmax, delay=0.25) xanchor .5
                        bar style "bar_mp" value AnimatedValue(value=p.mp, range=p.mpmax, delay=0.25) xanchor .5 yalign 0.05
                        text "[p.hp]/[p.hpmax]" xanchor .5 yalign 0.0075
                        text "[p.mp]/[p.mpmax]" xanchor .5 yalign 0.0575

screen display_monsters():
    fixed:
        pos (576, 448)
        for m in monster_slot[0:4]:
            fixed:
                xpos m.sprite_pos
                if not m.dead:
                    imagebutton at m.anim:
                        hover im.MatrixColor(getImage(m), im.matrix.brightness(0.1))
                        action Return(m), SensitiveIf(canTarget(m))
                        idle monsterImg(m) anchor (0.5,1.0)
                        if renpy.get_screen("select_monster"):
                            insensitive im.MatrixColor(getImage(m), im.matrix.saturation(0.1))
                        tooltip "{0} HP: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" xanchor 0.5
    fixed:
        pos (576, 640)
        for m in monster_slot[4:8]:
            fixed:
                xpos m.sprite_pos
                if not m.dead:
                    imagebutton at m.anim:
                        hover im.MatrixColor(getImage(m), im.matrix.brightness(0.1))
                        action Return(m), SensitiveIf(canTarget(m))
                        idle monsterImg(m) anchor (0.5,1.0)
                        if renpy.get_screen("select_monster"):
                            insensitive im.MatrixColor(getImage(m), im.matrix.saturation(0.1))
                        tooltip "{0} HP: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" xanchor 0.5

screen battle_message():
    add "images/battle/messagebox.png"
    hbox:
        xpos 110 yalign 0.07
        if message == "attack":
            text "Кто будет атаковать?"
        elif message == "skill":
            text "Что будет делать {0}?".format(currentplayer.name)
        elif message == "item":
            text "Выбрать предмет"
        elif message == "other_skill":
            text "{0} использовал [msg_skill]!".format(currentplayer.name)
        elif message == "attack_skill":
            text "{0} атаковал [msg_mons]!".format(currentplayer.name)
        elif message == "defend":
            text "{0} защитился!".format(currentplayer.name)
        elif message == "m_skill":
            text "[msg_mons] атака использя [msg_skill]!"
        elif message == "m_atk":
            text "[msg_mons] атаковал {0}!".format(roll_target.name)
        elif message == "target_who":
            text "Выбери цель?"
        elif message == "m_dead":
            text "[msg_mons] умер!"
        elif message == "player_ko":
            text "[koplayer] изнасиловали монстры!"
        elif message == "you_win":
            text "Поздровляю! Ты выиграл!"
        elif message == "lost":
            text "Ты проиграл... лох"
        elif message == "use_on_who":
            text "На кого использовать навык?"
        elif message == "none":
            text ""

label battling:
    $ inCombat = True
    while inCombat:
        if battleEnd == True:
            $ inCombat = False
            jump end_battle
        $ startPlayersTurn()
        $ message = "attack"
        call turn_actions
        $ message = "none"
        if not first_pola:
            x "Теперь ходят монстры"
        $ monsterTurns()

label end_battle:
    hide screen battle_overlay
    with dissolve
    if win:
        stop music
        play sound fanfare
        "Ты выиграл!"
        if not first_pola:
            x "Отлично!"
            x "Это был ваш первый бой"
            x "Больше я не буду вам помагать"
            x "Вы немного прокачались"
            x "Прийдите в библиотеку я вас обучу новым способностям"
            $ addTime()
            $ first_pola = True
        stop sound
        $ expFormula()
    else:
        $ message = "lost"
        "Ты проиграл."
        if not first_pola:
            x "Не знаю как, но мы проиграли"
            x "Приходи завтра в тоже время"
            $ addTime()
    show screen world_time
    hide screen battle_message
    hide screen display_monsters
    $ partyRevive()
    return