label most:
    play music "audio/music/old city theme.ogg"
    scene bg most
    with fade
    if talk_1denis and random_choise(30):
        $ OneDiscordMessage("# Глава 1 🌊\n{0} ходя по мосту на вас напал Денис".format(persistent.user_name))
        "Вы пришли на мост{w}, как вдруг"
        call horror_effect
        show pd
        with dissolve
        "На вас выскочил Денис"
        voice d0056
        d "Я убью тебя"
        $ fixedset = "finalpodval"
        $ type_battle = "denis"
        $ final_battle = False
        call battle
    "Вы пршли к мосту"
    if random_choise(15):
        $ OneDiscordMessage("# Глава 1 🌊\n{0} приёшл к мосту и заметил какой-то код, где же ему его найти 🤔".format(persistent.user_name))
        "Как вдруг вы заметили какой-то код"
        $ code = renpy.input("Ввести код ", length=4)
        if code == "5294":
            "Вы увидели самое страшное"
    menu mostm:
        "Любимый" if win_2les and not talk_2maxim and talk_1maxim:
            $ OneDiscordMessage("# Глава 1 🌊\nМакс пришёл на свидание с Любимым".format(persistent.user_name))
            $ talk_2maxim = True
            call restoreos()
            show pl cool at left
            show pm oshko at right
            with dissolve
            voice m0410b
            m "Здарова Любимый"
            voice l0057
            l "Иди ко мне{w}, романтики хочется"
            voice m0411
            m "Нам надо вместе обсудить как мы сюда попали"
            voice m0412
            m "Я уже говорил со многими"
            voice m0413
            m "Все по разному"
            voice l0058
            l "Это странно"
            voice m0414
            m "Да{w}, мы должны расследовать это"
            voice m0415
            m "Например Тянка и Санёк как и ты сюда попали как-то"
            voice m0416
            m "Борис я и Саша попали сюда через рай"
            voice m0417
            m "Но как"
            voice l0059
            l "Не знаю"
            voice l0060
            l "Всё что я помню это.."
            voice l0061
            l "Я не помню что происходила после последнего собрания с тобой"
            voice m0418
            m "Помню ты пошёл к Кириллу"
            voice m0419
            m "Дальше не знаю"
            voice l0062
            l "Я этого не помню"
            voice m0421
            m "Ладно"
            voice m0422
            m "продолжим расследование позже"
            show pl great
            voice l0063
            l "а сейчас?"
            voice m0423
            m "Можем провести собрание как надо"
            voice l0064
            l "оо"
            voice l0065
            l "Это уже нормально"
            voice l0066
            l "Посмотрим на сколько хорошо ты меня знаешь"
            menu round_1love:
                "Сколько часов у меня в КС?"
                "Около 500 часов":
                    voice l0067
                    l "Перебор{w}, я не задрот"
                "Окло 300 часов":
                    $ love_points += 2
                    voice l0068
                    l "Блиско"
                "Окло 200 часов":
                    $ love_points += 3
                    voice l0069
                    l "Да это правда"
                "Окло 100 часов":
                    $ love_points +=1 
                    voice l0068
                    l "Блиско"
                "Окло 50 часов":
                    voice l0070
                    l "Я только с тобой больше наиграл"
                "Окло 20 часов":
                    $ love_points -=1
                    voice l0071
                    l "Нет.."
            voice l0079
            l "Давай поговорим про мой пк"
            menu round_2love:
                "Что у меня ломалось?"
                "Видеокарта":
                    voice l0071
                    l "Нет.."
                "HDD":
                    $ love_points +=1 
                    voice l0072
                    l "Почти"
                "Мать":
                    voice l0071
                    l "Нет.."
                "БП":
                    voice l0071
                    l "Нет.."
                "сдд":
                    $ love_points += 3
                    voice l0073
                    l "Правда"
            menu round_3love:
                "На кого я учусь?"
                "Авиационный инженер":
                    voice l0071
                    l "Нет.."
                "Техник-диагност":
                    voice l0071
                    l "Нет.."
                "Инженер по технической поддержке":
                    voice l0071
                    l "Нет.."
                "Техник механик самолётов":
                    $ love_points += 3
                    voice l0074
                    l "Ого, ты знаешь это"
                "Авиатехнический специалист":
                    voice l0071
                    l "Нет.."
            $ FigthPointsToWin = 5
            if persistent.difficulty == 2:
                $ FigthPointsToWin = 3
            elif persistent.difficulty == 1:
                $ FigthPointsToWin = 1
            
            if love_points >= FigthPointsToWin:
                $ OneDiscordMessage("# Глава 1 🌊\nМакс провёл отличное свидание".format(persistent.user_name))
                voice l0075
                l "Где проведём следующие свидание?"
                voice m0424
                m "Предлагаю в бою"
                voice m0425
                m "Сходим в лес"
                voice l0076
                l "Можем попробовать"
                $ OneDiscordMessage("# Глава 1 🌊\nМаксим присоединился к отряду".format(persistent.user_name))
                $ party_list.append(maksim)
                $ maksim.exp = (maksim.lvl+1)**3 -100
            else:
                $ OneDiscordMessage("# Глава 1 🌊\nМакс провалил свидание".format(persistent.user_name))
                voice l0077
                l "Ну что{w}, увидимся ещё"
        "Подождать" if wait_most > 0:
            scene black
            with fade
            pause(1.5)
            $ wait_most -= 2
            random:
                "Вы постаяли так 6 часов.."
                "Вы подождали 6 часов.."
                "Вы единственный кто стоит тут 6 часов.."
                "Время идёт, а вы всё ещё стоите{w} прошло 6 часов.."
                "Вас приследовали мысли{w}, а прыгнуть мне с моста?{w} Прошло 6 часов.."
            $ addTime()
            jump most
        "Уйти":
            show screen map
            play music "music/Path to Lake Land.ogg"
            scene black
            ''
    show screen map
    play music "music/Path to Lake Land.ogg"
    scene black
    ''
