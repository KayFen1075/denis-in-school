label pola:
    play music "music/Faint Courage (Game Over).mp3"
    scene bg pola
    with fade
    if not first_pola and game_time == 24 and barmen:
        call restoreos()
        show px see
        with fade
        voice x0229
        x "Вот вы и пришли"
        voice x0230
        x "Сейчас у вас будет первый бой"
        voice x0231
        x "В это время обычно появляются всякие твари"
        voice s0169
        s "Например Денис?"
        voice x0232
        x "Да"
        voice x0233
        x "Я его регулярно пиздю"
        voice x0234
        x "Этот еблан пиздит пшеницу"
        voice m0426
        m "Скоро и мы его будем пиздить"
        voice x0235
        x "И так"
        voice x0236
        x "Сейчас"
        voice x0237
        x "Начнём первый бой"
        "Вы услышали какой-то звук из кустов"
        voice x0238
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
        voice x0239
        x "Вы пришли"
        voice x0240
        x "Сейчас мы изучим новый элемент в магии"
        voice x0241
        x "И это огонь{w}, а точнее огненный шар"
        voice s0170
        s "В чём разница от ледяного"
        voice x0242
        x "Нет"
        voice m0427
        m "Мы это поле сожгём?"
        voice x0243
        x "Скорее всего да"
        voice x0244
        x "По этому мы сюда и пришли"
        "Вы услышали шорох в кустах"
        hide px
        call horror_effect
        show pd scream2
        with dissolve
        play sound dk
        voice d0055
        d "Я всех вас убью"
        voice x0245
        x "Блять{w}, опять он"
        voice x0246
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
        voice x0247
        x "Как же он уже надоел"
        voice x0248
        x "Появился хрен знает от куда"
        voice x0249
        x "И делает набеги"
        voice m0428
        m "Саш может сегодня ночью прийдём и отпиздим его?"
        voice s0172
        s "Давай"
        voice s0173
        s "Можем так каждый день делать"
        voice m0429
        m "Ну всё{w=1.2}, жду тебя там"
        voice x0250
        x "Так"
        voice x0251
        x "Начнём урок"
        menu magic4:
            "Кто получит заклинание \"Огненный шар\""
            "Давай я([name])":
                $ OneDiscordMessage("# Глава 1 🌻\n[name] изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide pm
                with dissolve
                show ps at left
                with move
            "Саша" if sasha in party_list:
                $ OneDiscordMessage("# Глава 1 🌻\nСаша изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide pm
                with dissolve
                show ps at left
                with move
            "Макс" if maks in party_list:
                $ OneDiscordMessage("# Глава 1 🌻\nМакс изучил заклинание \"Огненный шар\"".format(persistent.user_name))
                hide ps
                with dissolve
                show pm oshko at left
                with move
        call lb_by_magic(mindfire, free=True)
        $ renpy.notify("В новой версии всец могут выбрать эту магию")

        scene black
        with fade
        "Так как вы знали основы, вы быстро освоили эту магию"
        scene bg pola
        with fade
        show px
        show pm see at right
        show ps at left
        with dissolve
        voice x0252
        x "Всё, я пойду в коледж"
        voice m0430
        m "Давай"
        voice s0174
        s "Идём прямо сейчас его пиздить"
        voice m0431
        m "Пошли"
    $ addDictionary("Поле", "Чёрная дыра очка Дениса")
    "Вы слышите как ветер колыхает траву"
    "Вам больше него делать{w}, вы уходите"
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return
