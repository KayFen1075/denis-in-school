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
    if not fights_left_les > 0:
        scene black
        "Ты слишком часто сражался"
        "Сделай что-то другое"
        show screen map
        play music "music/Path to Lake Land.ogg"
        ''
    show screen select_les 
    with fade
    ''
    # menu les_chose():
        # "Куда вы хотите отправится?"
        # "Вход в лес" if a.lvl < 18:
            # $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Вход в лес".format(persistent.user_name))
            # $ wild_monsters = [mon1,mon2,mon3]
            # $ fixedset = "zeleboba"
            # $ type_battle = "1les"
        # "Чащя леса" if a.lvl > 9 and win_1les and a.lvl < 24 or True:
            # $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Чащя леса".format(persistent.user_name))
            # $ wild_monsters = [mon3, mon4,mon5,mon6]
            # $ type_battle = "2les"
        # "Озеро леса" if a.lvl > 13 and win_2les and a.lvl < 30:
            # $ OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Озеро леса".format(persistent.user_name))
            # $ wild_monsters = [mon5, mon7,mon8,mon9]
            # $ type_battle = "3les"
        # "Болото зелебобы" if a.lvl >= 25 and win_3les and talk_1denis:
            # $ OneDiscordMessage("# Глава 1 🌳\n{0} начал бой с зелебобой".format(persistent.user_name))
            # $ fixedset = "zeleboba"
            # $ type_battle = "4les"
        # "Уйти":
            # show screen map
            # play music "music/Path to Lake Land.ogg"
            # ''
    # call load_items
    return

label start_battle:
    call load_monsters
    call battle

init python:
    def start_battle_les(les):
        global wild_monsters
        global type_battle
        global fixedset
        if les == 1:
            OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Вход в лес".format(persistent.user_name))
            wild_monsters = [mon1,mon2,mon3]
            # $ fixedset = "zeleboba"
            type_battle = "1les"
            reserve_monsters = [mon12,mon11]
        elif les == 2:
            OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Чащя леса".format(persistent.user_name))
            wild_monsters = [mon3, mon4,mon5,mon6]
            type_battle = "2les"
        elif les == 3:
            OneDiscordMessage("# Глава 1 🌳\n{0} в первые штурмовал Озеро леса".format(persistent.user_name))
            wild_monsters = [mon5, mon7,mon8,mon9]
            type_battle = "3les"
        elif les == 4:
            OneDiscordMessage("# Глава 1 🌳\n{0} начал бой с зелебобой".format(persistent.user_name))
            fixedset = "zeleboba"
            type_battle = "4les"
        renpy.hide_screen("select_les")
        renpy.jump("start_battle")

screen select_les():
    modal True
    zorder 102

    imagebutton idle "gui/battle/les/{0}.png".format(last_les) action Hide("select_les")
    text "Текущий уровень леса: [last_les]" pos (0.5, 0.1)
    $ a.lvl = 16
    if last_les>1:
        imagebutton idle "gui/battle/arrow_left.png" pos 0.01, 0.4 action SetVariable("last_les", max(1, last_les - 1))
    if last_les == 1 and a.lvl > 9:
        imagebutton idle "gui/battle/arrow_right.png" pos 0.9, 0.4 action SetVariable("last_les", min(4, last_les + 1)) 
        if a.lvl < 18:
            imagebutton idle "gui/battle/battle.png" xpos 0.35 action Function(start_battle_les, last_les)  
    elif last_les == 2 and a.lvl > 13:
        imagebutton idle "gui/battle/arrow_right.png" pos 0.9, 0.4 action SetVariable("last_les", min(4, last_les + 1)) 
        if a.lvl < 24:
            imagebutton idle "gui/battle/battle.png" xpos 0.35 action Function(start_battle_les, last_les)
    elif last_les == 3 and a.lvl > 25:
        imagebutton idle "gui/battle/arrow_right.png" pos 0.9, 0.4 action SetVariable("last_les", min(4, last_les + 1)) 
        if a.lvl < 30:
            imagebutton idle "gui/battle/battle.png" xpos 0.35 action Function(start_battle_les, last_les)
    elif last_les == 4:
        imagebutton idle "gui/battle/battle.png" xpos 0.35 action Function(start_battle_les,last_les)