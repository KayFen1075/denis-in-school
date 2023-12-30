label battle:
    if autohil:
        $ restorehp()
        $ restoremp()
    hide screen world_time
    $ stopEvent()
    $ misstext = renpy.random.choice(misstext_list)
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

    call battle_music from _call_battle_music

    scene battle_background
    with pixellate
    if not first_pola:
        show px
        with dissolve
        x "Это место для боя{w}, выбери себе команду"
        x "С ней будет проще сражаться"
        hide px
        with dissolve
    call player_select from _call_player_select
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
    if type_battle == "lolis":
        "Лоли" "Помогите!"
        "Лоли" "Он использует нас"
        "Лоли" "Он управляет нами"
        "Лоли" "Освободите нас"
    if fixedset == "zeleboba":
        "Зелебоба" "Что вы забыли на моём болоте!"
        "Зелебоба" "Я буду его защищать!"
        "? ? ?" "Помогите!"
        "Зелебоба" "Молчать!"
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
                    tooltip "{0}\nАтака: {1}\nЗащита: {2}".format(p.name, p.atk+p.bonus_atk, p.dfn+p.bonus_dfn)
                    action Function(playerAction(p))
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
                        text "[p.hp]/[p.hpmax]" font "fonts/damages.ttf" size 25 xanchor .5 yalign 0.009
                        text "[p.mp]/[p.mpmax]" font "fonts/damages.ttf" size 25 xanchor .5 yalign 0.0575

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
                        tooltip "{0} Мана монстра: {1}".format(m.name, m.hp)
                    bar style "bar_mhp" value AnimatedValue(value=m.hp, range=m.hpmax, delay=0.25) anchor (0.5,1.0)
                    text "[m.hp]" font "fonts/damages.ttf" size 25 outlines [(2, "#00000080", 1, 1)] xanchor 0.5 yanchor 1.2
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
                    text "[m.hp]" font "fonts/damages.ttf" size 25 outlines [(2, "#00000080", 1, 1)] xanchor 0.5 yanchor 1.2

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
        call turn_actions from _call_turn_actions
        $ message = "none"
        if not first_pola:
            x "Теперь ходят монстры"
        $ monsterTurns()

label end_battle:
    hide screen battle_overlay
    with dissolve
    if win:
        if type_battle == "1les":
            $ win_1les = True
            $ max_level = max(max_level, 16)
            $ renpy.notify("Доступны новые действия!")
        elif type_battle == "2les":
            $ win_2les = True
            $ max_level = max(max_level, 22)
            $ renpy.notify("Доступны новые действия!")
        elif type_battle == "3les":
            $ win_3les = True
            $ max_level = max(max_level, 26)
            $ renpy.notify("Доступны новые действия!")
        elif type_battle == "4les":
            $ win_4les = True
            $ max_level = max(max_level, 30)
            if not first_win4les:
                $ first_win4les = True
                if name == "Кирилл":
                    with fade
                    "Вы оделили зелебобу"
                    "Вы заметили клетку"
                    if friend == "sasha":
                        $ party_list.append(maks)
                        $ maks.lvl = 23
                        $ maks.exp = (maks.lvl+1)**3 -100
                        show pm
                        with dissolve
                        m "Здарова"
                        k "Как ты здесь оказался?"
                        m "Долгая история"
                        m "Можешь освободить?"
                        k "Да конечно"
                        show pm oshko
                        with dissolve
                        "Вы открыли клетку"
                        k "Нам надо спасти Макса"
                        k "Он в заточении в подвале"
                        m "Я спиздел то что колекционировал зелебоба"
                    else:
                        $ party_list.append(sasha)
                        $ sasha.lvl = 23
                        $ sasha.exp = (sasha.lvl+1)**3 -100
                        show ps
                        with dissolve
                        s "Здарова"
                        k "Как ты здесь оказался?"
                        s "Долгая история"
                        s "Можешь освободить?"
                        k "Да конечно"
                        show ps smile
                        with dissolve
                        "Вы открыли клетку"
                        k "Нам надо спасти Макса"
                        k "Он в заточении в подвале"
                        s "Я спиздел то что колекционировал зелебоба"
                    k "Не знаю что это"
                    k "Но выглядит как что-то для магии"
                    k "Отправлюсь к Саньку"
                    k "Он знает что с этим делать"
                else:
                    scene black
                    with fade
                    "Вы оделили зелебобу"
                    "Вы заметили клетку"
                    show pk stoika
                    with dissolve
                    k "Здарова"
                    "[name]" "Как ты здесь оказался?"
                    k "Долгая история"
                    k "Можешь освободить?"
                    "[name]" "Да конечно"
                    "Вы открыли клетку"
                    show pk product
                    with dissolve
                    k "Я спиздел то что колекционировал зелебоба"
                    k "Не знаю что это"
                    k "Но выглядит как что-то для магии"
                    "[name]" "Это надо показать Саньку{w}, он знает что с этим делать"
                    k "Хорошо"
        elif type_battle == "1dan":
            $ win_1dan = True
            $ max_level = max(max_level, 45)
            if first_win1dan == False:
                $ first_win1dan = True
                "Вы смогли освободить лолей из секс рабства Дениса"
                "Вы заметили что кого-то они тащили куда-то в глубь"
                "Так как вы освободили лолей вы решили развязать мешок"
                if friend == "maks":
                    $ party_list.append(maks)
                    show pm
                    with dissolve
                    m "Вы меня спасли"
                    s "Что они с тобой сделали?"
                    m "Они хотели меня выебать"
                    m "Зря вы меня спасли"
                    k "Так это{w}, мы тоже можем тебя трахнуть"
                    s "С радостью{w}, у меня меня уже встал"
                    m "Так давайте)"
                else:
                    $ party_list.append(sasha)
                    show ps
                    with dissolve
                    s "Вы меня спасли"
                    m "Что они с тобой сделали?"
                    s "Они хотели меня выебать"
                    s "Зря вы меня спасли"
                    k "Так это{w}, мы тоже можем тебя трахнуть"
                    m "С радостью{w}, у меня меня уже встал"
                    s "Так давайте)"
                scene black
                with fade
                "Так они трахались"
        elif type_battle == "2dan":
            $ win_2dan = True
            $ max_level = max(max_level, 60)
        elif type_battle == "3dan":
            $ win_3dan = True
        elif type_battle == "4dan":
            $ win_4dan = True
            if not first_win4dan:
                $ first_win4dan = True
                "Вы смогли зачистить всё подземелье"
                "Теперь вам здесь не чего делать"
                "Лоли" "Вы спасли нас"
                "Генерал Лоли" "Мы можем помочь найти Дениса"
                s "Где он"
                "Лоли" "Он в самом ужасном месте"
                "Генерал Лоли" "Он обидает в своём подвале у себя дома"
                m "Вот мы его и нашли!"
                "Генерал Лоли" "Будьте окуратны"
                "Генерал Лоли" "Все кто бунтовали против него не могли ему не чего сделать"
                "Генерал Лоли" "Хоть там и были наши самые сильные отряды"
                "Лоли" "Я чуствую что ваша магия поможет его одолеть"
                k "Я уверен у нас получиться его одолеть"
                s "Ну что"
                m "Закупаемся и в последний путь"
        elif type_battle == "denis" and final_battle:
            $ win_denis == True
            scene black
            hide screen world_time
            play music "music/videoplayback.mp3"
            u "{bt=1}Да как вы посмели..{/bt}"
            d "Экхе"
            "Вы смогли одолеть их"
            s "Наконец-то мы сможем выбраться от сюда!"
            m "Хоть это было и сложно{w} зато весело"
            k "Я поебался с мухомором"
            k "Оно того стоило"
            l "А я с тобой Макс"
            t "Сейчас я докажу вам что я настоящия"
            z "Я знал что всё привидёт к этому!"
            b "Вы же не забыли про меня?"
            menu ostavit_borisa:
                "Оставить его здесь":
                    $ action_ostavit_borisa = True
                    "Все сделали вид что его тут нету"
                "Взять с собой":
                    s "Конечно"
                    m "Ты идёшь с нами"
                    "Вы взяли с собой Бориса"
            $ renpy.notify("Это действие будет иметь последствия")
            scene bg koledsh
            with fade
            "Больше ни кто не изучит магию в колледже"
            scene bg shop
            with fade
            "Ни кто не купить запрещённое оружие"
            scene 1
            with fade
            "В лесу теперь спокойно"
            scene bg dd
            with fade
            "Старый дом Дениса скоро обвалиться"
            scene bg demon
            with fade
            "Замок короля демонов полностью оброс листвой"
            scene black
            with fade
            stop music
            "Но"
            "?" "Ты ещё не исправил будующие"
            scene whitle
            with Fade(1,4,1,color="#fff")
            "{fi}Первая глава пройдена{/fi}"
            "{fi}Второй главы пока нет{w}, можете перепройти на другие концовки{/fi}"
            scene parish
            with diss
            play audio iavparish
            pause 8
            scene black with fade
            return
        stop music
        play sound fanfare
        random:
            "[name]" "Сосать боты"
            "[name]" "Легчайшая"
            "[name]" "Меня ебали"
            "[name]" "Изи"
            "[name]" "Ez"
            "[name]" "Боже боты"
            "[name]" "Я ебал вас"
            "[name]" "Побэда"
            "[name]" "Без потерь"
            "[name]" "Более кринжовых фраз я ещё не говорил.."
            "[name]" "Нихуя себе, победа"
            "[name]" "ЕЗЗЗ"
            "[name]" "Подайте сыр мисье"
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
        "Ты проебал"
        if not first_pola:
            x "Не знаю как, но мы проиграли"
            x "Приходи завтра в тоже время"
            $ addTime()
    if type_battle == "lolis":
        "Лоли" "Он заточил нас в данжах"
        "Лоли" "Он называет их подвалами с многими этажами"
        "[name]" "Я должен спасти их"
        "[name]" "Но сначала{w}, я должен одолеть зелебобу"
    show screen world_time
    hide screen battle_message
    hide screen display_monsters
    with fade
    $ partyRevive()
    return