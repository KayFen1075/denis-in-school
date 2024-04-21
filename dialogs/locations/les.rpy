label les:
    scene black
    play music "audio/music/8-bit-arcade-138828.mp3"
    $ bb = 1
    if not first_libriary:
        scene black
        "Ты не можешь пойти в лес"
        "Сделай что-то другое"
        show screen map
        play music "music/Path to Lake Land.ogg"
        ''
    menu les_chose():
        "Куда вы хотите отправится?"
        "Вход в лес" if a.lvl < 18:
            $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Вход в лес".format(persistent.user_name))
            $ wild_monsters = [mon1,mon2,mon3]
            $ type_battle = "1les"
        "Чащя леса" if a.lvl > 9 and win_1les and a.lvl < 24:
            $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Чащя леса".format(persistent.user_name))
            $ wild_monsters = [mon3, mon4,mon5,mon6]
            $ type_battle = "2les"
        "Озеро леса" if a.lvl > 13 and win_2les and a.lvl < 30:
            $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Озеро леса".format(persistent.user_name))
            $ wild_monsters = [mon5, mon7,mon8,mon9]
            $ type_battle = "3les"
        "Болото зелебобы" if a.lvl >= 25 and win_3les and talk_1denis:
            $ OneDiscordMessage("# Глава 1 🌳\n{0} начал бой с зелебобой".format(persistent.user_name))
            $ fixedset = "zeleboba"
            $ type_battle = "4les"
        "Уйти":
            show screen map
            play music "music/Path to Lake Land.ogg"
            ''
    call load_monsters from _call_load_monsters_3
    #call load_items

    call battle from _call_battle_1
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return