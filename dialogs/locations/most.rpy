label most:
    play music "audio/music/old city theme.ogg"
    scene bg most
    with fade
    if talk_1denis and random_choise(30):
        $ OneDiscordMessage("# Глава 1 🌊\n{0} ходя по мосту на вас напал Денис".format(persistent.user_name))
        "Вы пришли на мост{w}, как вдруг"
        show pd
        with dissolve
        "На вас выскочил Денис"
        d "Я убью тебя"
        $ fixedset = "finalpodval"
        $ type_battle = "denis"
        $ final_battle = False
        call battle
    "Вы пршли к мосту"
    if random_choise(15):
        $ OneDiscordMessage("# Глава 1 🌊\n{0} приёшл к мосту и заметил какой-то код, где же ему его найти 🤔".format(persistent.user_name))
        "Как вдруг вы заметили какой-то код"
        if renpy.input("Ввести код ", length=4) == "5294":
            "Вы увидели самое страшное"
    menu mostm:
        "Любимый" if win_2les and not talk_2maxim and talk_1maxim:
            $ OneDiscordMessage("# Глава 1 🌊\nМакс пришёл на свидание с Любимым".format(persistent.user_name))
            $ talk_2maxim = True
            show pl cool at left
            show pm oshko at right
            with dissolve
            m "Здарова Любимый"
            l "Иди ко мне{w}, романтики хочется"
            m "Нам надо вместе обсудить как мы сюда попали"
            m "Я уже говорил со многими"
            m "Все по разному"
            l "Это странно"
            m "Да{w}, мы должны расследовать это"
            m "Например Тянка и Санёк как и ты сюда попали как-то"
            m "Борис я и Саша попали сюда через рай"
            m "Но как"
            l "Не знаю"
            l "Всё что я помню это.."
            l "Я не помню что происходила после последнего собрания с тобой"
            m "Помню ты пошёл к Кириллу"
            m "Дальше не знаю"
            l "Я этого не помню"
            m "Ладно"
            m "продолжим расследование позже"
            show pl great
            l "а сейчас?"
            m "Можем провести собрание как надо"
            l "оо"
            l "Это уже нормально"
            l "Посмотрим на сколько хорошо ты меня знаешь"
            menu round_1love:
                "Сколько часов у меня в КС?"
                "Около 500 часов":
                    l "Перебор{w}, я не задрот"
                "Окло 300 часов":
                    $ love_points += 2
                    l "Блиско"
                "Окло 200 часов":
                    $ love_points += 3
                    l "Да это правда"
                "Окло 100 часов":
                    $ love_points +=1 
                    l "Блиско"
                "Окло 50 часов":
                    l "Я только с тобой больше наиграл"
                "Окло 20 часов":
                    $ love_points -=1
                    l "Нет.."
            l "Давай поговорим про мой пк"
            menu round_2love:
                "Что недавно у меня ломалось?"
                "Видеокарта":
                    l "Нет.."
                "HDD":
                    $ love_points +=1 
                    l "Почти"
                "Мать":
                    l "Нет.."
                "БП":
                    l "Нет.."
                "сдд":
                    $ love_points += 3
                    l "Правда"
            menu round_3love:
                "На кого я учусь?"
                "Авиационный инженер":
                    l "Нет.."
                "Техник-диагност":
                    l "Нет.."
                "Инженер по технической поддержке":
                    l "Нет.."
                "Техник механик самолётов":
                    $ love_points += 3
                    l "Ого, ты знаешь это"
                "Авиатехнический специалист":
                    l "Нет.."
            $ FigthPointsToWin = 5
            if persistent.difficulty == 2:
                $ FigthPointsToWin = 3
            elif persistent.difficulty == 1:
                $ FigthPointsToWin = 1
            
            if love_points >= FigthPointsToWin:
                $ OneDiscordMessage("# Глава 1 🌊\nМакс провёл отличное свидание".format(persistent.user_name))
                l "Где проведём следующие свидание?"
                m "Предлагаю в бою"
                m "Сходим в лес"
                l "Можем попробовать"
                $ OneDiscordMessage("# Глава 1 🌊\nМаксим присоединился к отряду".format(persistent.user_name))
                $ party_list.append(maksim)
                $ maksim.exp = (maksim.lvl+1)**3 -100
            else:
                $ OneDiscordMessage("# Глава 1 🌊\nМакс провалил свидание".format(persistent.user_name))
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
