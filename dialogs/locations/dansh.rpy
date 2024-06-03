label dansh:
    scene bg dan
    play music "audio/music/Casual 8-bit.wav"
    if not fights_left_dan > 0:
        scene black
        "Ты слишком часто сражался"
        "Сделай что-то другое"
        show screen map
        play music "music/Path to Lake Land.ogg"
        ''
    if not talk_2boris:
        "Зловейщяя аура отпигивает тебя"
        show screen map
        play music "music/Path to Lake Land.ogg"
        ''
    if talk_2boris and not first_dan:
        $ OneDiscordMessage("# Глава 1 💀\n{0} нашёл подвалы Дениса, что бы спасти друга".format(persistent.user_name))
        call restoreos()
        $ first_dan = True
        show pk
        with fade
        voice k0103
        k "Вот я и пришёл"
        voice k0104
        k "Это то самое жуткое место"
        voice k0105
        k '"Подвалы Дениса"'
        voice k0106
        k "Самое опасное место"
        voice k0107
        k "Мы должны спасти его"
        voice k0108
        k "И добратся до самого низа"
        voice k0109
        k "До ядра земли"
        hide pk
        with moveoutbottom
        "Вы пришли к подземелью"
    $ bb = 2
    menu dan_chose():
        "Куда вы хотите отправится?"
        'Подвал "Арнаутова"' if a.lvl < 32:
            $ OneDiscordMessage("# Глава 1 💀\n{0} в первые зашёл в Подвал \"Арнаутова\"".format(persistent.user_name))
            $ wild_monsters = [mon11,mon12,mon13]
            $ type_battle = "1dan"
        'Подвал 18' if a.lvl > 29 and a.lvl < 44:
            $ OneDiscordMessage("# Глава 1 💀\n{0} в первые зашёл в Подвал 18".format(persistent.user_name))
            $ wild_monsters = [mon13, mon14,mon15,mon16]
            $ type_battle = "2dan"
        'Подвал "Попова"' if a.lvl > 35:
            $ OneDiscordMessage("# Глава 1 💀\n{0} в первые зашёл в Подвал \"Попова\"".format(persistent.user_name))
            $ wild_monsters = [mon15, mon17,mon18,mon19]
            $ type_battle = "3dan"
        'Подвал "Металлургов 12"' if a.lvl > 50 and win_3dan and talk_2sasha:
            $ OneDiscordMessage("# Глава 1 💀\n{0} в первые зашёл в Подвал \"Металлургов 12\"".format(persistent.user_name))
            $ fixedset = "lolisboss"
            $ type_battle = "4dan"
        "Уйти":
            show screen map
            play music "music/Path to Lake Land.ogg"
            ''
    call load_monsters from _call_load_monsters_4
    #call load_items

    call battle from _call_battle_4
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return

