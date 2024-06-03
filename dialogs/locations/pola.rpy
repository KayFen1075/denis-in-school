label pola:
    play music "music/Faint Courage (Game Over).mp3"
    scene bg pola
    with fade
    if not first_pola and game_time == 24 and barmen:
        call restoreos()
        show px see
        with fade
        x "Вот вы и пришли"
        x "Сейчас у вас будет первый бой"
        x "В это время обычно появляются всякие твари"
        voice s0169
        s "Например Денис?"
        x "Да"
        x "Я его регулярно пиздю"
        x "Этот еблан пиздит пшеницу"
        voice m0426
        m "Скоро и мы его будем пиздить"
        x "И так"
        x "Сейчас"
        x "Начнём первый бой"
        "Вы услышали какой-то звук из кустов"
        x "Вот и оно"
        $ OneDiscordMessage("# Глава 1 🌻\n{0} попал в первый бой-обучение".format(persistent.user_name))
        $ party_list.append(sanek)
        $ fixedset = "set 1"
        call battle from _call_battle_2
        $ restorehp()
        $ restoremp()
        $ party_list.remove(sanek)
    
    if not talk_3sanek and win_3les and talk_2sanek:
        $ OneDiscordMessage("# Глава 1 🌻\n{0} пришёл на урок в поле".format(persistent.user_name))
        $ talk_3sanek = True
        call restoreos()
        show px
        show pm see at right
        show ps at left
        with dissolve
        x "Вы пришли"
        x "Сейчас мы изучим новый элемент в магии"
        x "И это огонь{w}, а точнее огненный шар"
        voice s0170
        s "В чём разница от ледяного"
        x "Нет"
        voice m0427
        m "Мы это поле сожгём?"
        x "Скорее всего да"
        x "По этому мы сюда и пришли"
        "Вы услышали шорох в кустах"
        hide px
        call horror_effect
        show pd scream2
        with dissolve
        play sound dk
        voice d0055
        d "Я всех вас убью"
        x "Блять{w}, опять он"
        x "Пиздите его, он слаб, он нам не чего не сделает"
        voice s0171
        s "Поняли"
        scene black
        with fade
        "Вы начали пиздить Дениса"
        "Удар за ударом"
        "Вскоре он упал на землю"
        scene bg pola
        with fade
        show px
        show pm see at right
        show ps at left
        with dissolve
        x "Как же он уже надоел"
        x "Появился хрен знает от куда"
        x "И делает набеги"
        voice m0428
        m "Саш может сегодня ночью прийдём и отпиздим его?"
        voice s0172
        s "Давай"
        voice s0173
        s "Можем так каждый день делать"
        voice m0429
        m "Ну всё{w}, жду тебя там"
        x "Так"
        x "Начнём урок"
        menu magic4:
            "Кто получит заклинание \"Огненный шар\""
            "Давай я([name])":
                $ OneDiscordMessage("# Глава 1 🌻\n[name] изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide pm
                with dissolve
                show ps at left
                with move
                $ a.addSkill(mindfire)
            "Саша" if sasha in party_list:
                $ OneDiscordMessage("# Глава 1 🌻\nСаша изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide pm
                with dissolve
                show ps at left
                with move
                $ sasha.addSkill(mindfire)
            "Макс" if maks in party_list:
                $ OneDiscordMessage("# Глава 1 🌻\nМакс изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide ps
                with dissolve
                show pm oshko at left
                with move
                $ maks.addSkill(mindfire)
        scene black
        with fade
        "Так как вы знали основы, вы быстро освоили эту магию"
        scene bg pola
        with fade
        show px
        show pm see at right
        show ps at left
        with dissolve
        x "Всё, я пойду в коледж"
        voice m0430
        m "Давай"
        voice s0174
        s "Идём прямо сейчас его пиздить"
        voice m0431
        m "Пошли"
        
    "Вы слышите как ветер колыхает траву"
    "Вам больше него делать{w}, вы уходите"
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return
