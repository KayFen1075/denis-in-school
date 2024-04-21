label daun:
    play music "music/8-bit-moonlight-sonata-music-loop.mp3"
    if talk_2maxim and talk_1boris and otpizdeli_denisa >= 2 and game_time == 24 and not talk_1denis:
        $ talk_1denis = True
        scene black
        pause(1.0)
        show pd aun
        with dissolve
        d "За что"
        d "За что меня не кто понимает"
        d "Почему все меня пиздят"
        d "Где бы я не был{w} все{w} меня"
        pause(1.0)
        with hpunch
        d "{sc}НЕНАВИДЯТ{/sc}"
        with hpunch
        d "{sc}ИЗБЕВАЮТ{/sc}"
        with hpunch
        d "{sc}ПРИЗЕРАЮТ{/sc}"
        with hpunch
        d "{sc}НЕ СЧИТАЮТ ЗА ЧЕЛОВЕКА{/sc}"
        scene bg pola
        show pm see at right
        show ps at left
        with fade
        "Они услышали тебя"
        show pd scream2
        with dissolve
        play sound dk
        d "Пожалуйста не трогайте меня"
        x "Блять{w}, опять он"
        x "Пиздите его, он слаб, он нам не чего не сделает"
        d "Не надо"
        voice s0440
        s "Поняли"
        scene black
        with fade
        "Они начали избивать тебя"
        "Удар за ударом"
        "Вскоре ты пал"
        d "За что.."
        scene bg shop
        with fade
        show pd scream2 at left
        d "Может я смогу купить что-то из еды"
        d "Я получил 13 грывень из монстров"
        show pb open 
        with moveinleft
        voice b0119
        b "БЛЯТЬ{w=1.5} что ты тут делаешь"
        voice b0120
        b "Как стража вообще впустила в город"
        d "Пожалуйста продай немного еды"
        scene black
        with fade
        "Борис начал избивать тебя"
        with hpunch
        "Безжалостно"
        "Была бы у него сила он бы тебя убил"
        $ OneDiscordMessage("# Глава 1 👹\n{0} узнал историю Дениса".format(persistent.user_name))
        scene bg koledsh
        with fade
        show pd screem
        with dissolve
        d "Может я смогу получить образование"
        d "Пользоваться магией"
        d "Вступить в гильдию и найти тех кто будет меня любить"
        show px at left
        with moveinleft
        x "Ах ты тварь"
        x "Подошёл к моему колледжу"
        scene black
        with fade
        "Они начали избивать тебя"
        "Удар за ударом"
        "Вскоре ты пал"
        d "За что.."
        show pd aun
        with dissolve
        d "За что.."
        d "{sc}За что..{/sc}"
        d "Я отправляюсь к владыке демонов"
        scene bg demon
        with fade
        show pd aun
        with dissolve
        "Ты пришёл к нему"
        "Давай{w} {sc}сделай это{/sc}"
        "{sc}Убей его{w} забери его силу{w} и отомсти всем кто тебя избивал{/sc}"
        "{sc}Ты всё равно уже не человек{/sc}"
        $ OneDiscordMessage("# Глава 1 👹\n{0} узнал про голос в голове Дениса".format(persistent.user_name))
        d "Да.."
        d "Я должен это сделать"
        d "Я убью короля демонов"
        hide pd aun
        with dissolve
        "Ты зашёл в здание"
        "Владыка демонов спал в своей комнате"
        d "Время пришло"
        "Ты начал душить его"
        "Бес жалостно"
        "Без капли сомнения"
        "В какой-то момент он перестал сопротивляться"
        $ OneDiscordMessage("# Глава 1 👹\nДенис убил короля демонов".format(persistent.user_name))
        "Ты вышел на улицу"
        show pd aun
        with dissolve
        d "Я{w}, {sc}я чувствую новую силу{/sc}"
        "Денис получил новый 3 уровень!"
        "Денис получил новый 14 уровень!"
        "Денис получил новый 26 уровень!"
        "Денис получил новый 46 уровень!"
        "Денис получил новый 175 уровень!"
        "{sc}Денис получил новый 9999999 уровень!{/sc}"
        show lolidance at left
        with dissolve
        u "Ты э.. {w} Ух ебать"
        u "Кхм"
        u "Ты это сделал"
        u "Ты одолел короля демонов"
        u "В замен я дарую тебе силу"
        u "Ты герой этого мира"
        u "Я обратно в небеса"
        u "Можешь меня позвать я всегда помогу"
        hide lolidance
        with dissolve  
        d "Я буду мстить"
        d "Всем за то что они сделали"
        d "Но сначала.."
        scene black
        with fade
        if maks in party_list:
            d "{sc}Я УБЬЮ МАКСА{/sc}"
            $ OneDiscordMessage("# Глава 1 👹\nМакс пропал".format(persistent.user_name))
            $ party_list.remove(maks)
        else:
            d "{sc}Я УБЬЮ САШУ{/sc}"
            $ OneDiscordMessage("# Глава 1 👹\nСаша пропал".format(persistent.user_name))
            $ party_list.remove(sasha)
        scene bg koledsh_room
        with fade
        "На утро его уже не было"
        if name == "Саша":
            show ps
            with dissolve
            voice s0441
            s "Где Макс"
            voice s0442
            s "Говорил что сходит к Максиму и вернётся"
            voice s0443
            s "Я лег без него"
            voice s0444
            s "Но куда он пропал"
            "Саша заметил записку"
            "Хочешь его вернуть{w}, иди в поле утром"
            m "Пиздец"
            m "Цыгани спиздили коня"
        else:
            show pm
            with dissolve
            m "Где Саша"
            m "Говорил что сходит к Борису и вернётся"
            m "Я лег без него"
            m "Но куда он пропал"
            "Макс заметил записку"
            "Хочешь его вернуть{w}, иди в поле утром"
            m "Пиздец"
            m "Цыгани спиздили коня"
        $ addTime()
        scene black
        with fade
        "[name] пришёл в поле утром"
        scene bg pola
        with fade
        show pd
        with dissolve
        d "Ты пришёл сюда"
        d "Я получил силу которая мне и не снилась"
        d "Теперь моя очередь вас всех пиздить"
        $ OneDiscordMessage("# Глава 1 👹\n{0} увидел первый бой с лолями".format(persistent.user_name))
        $ type_battle = "lolis"
        $ fixedset = "lolis"
        $ restorehp()
        $ restoremp()
        call battle from _call_battle_3
        
        show screen map
        play music "music/Path to Lake Land.ogg"
        scene black
        ''
    if talk_3sanek and game_time == 24 and not talk_1denis:
        $ OneDiscordMessage("# Глава 1 👹\n{0} нашёл дом Дениса".format(persistent.user_name))
        scene bg dd
        with fade
        m "Вот мы и нашли его дом"
        voice s0445
        s "Готов его отпиздить?"
        menu pizdetDenisa:
            "Отпиздить Дениса пока он спит?"
            "ХУЯРИТЬ НАДО ТОЛЬКО НОГАМИ":
                $ OneDiscordMessage("# Глава 1 👹\n{0} отпиздел Дениса".format(persistent.user_name))
                $ otpizdeli_denisa += 1
                scene bg dd_room
                with fade
                m "Смотри какой слабенький"
                m "Наверное у него уровень первый или второй"
                voice s0446
                s "АХАха, динахуй"
                voice s0447
                s "Ты вообще только хилять умеешь"
                m "Ладно давай начнём"
                play music raindow_adventure
                "Вы начали пиздить Дениса"
                "Вы настолько увлеклись что в глазах потемнело.."
                scene black
                with fade
                "Вы бесжалосно наносили один удар за другим"
                with hpunch
                "Один"
                with hpunch
                "За другим"
                with hpunch
                "По законам этого мира"
                "Тот кто спит{w} тот лох"
                with hpunch
                "Сон для слабых"
                "Так что можно убить кого угодно если он спит"
                with hpunch
                "Но сон необязательный"
                with hpunch
                "Про это знают не все"
                "Вы закончили пиздить Дениса"
                play music "music/8-bit-moonlight-sonata-music-loop.mp3"
                scene bg dd
                with fade
                m "Нормально мы его отхуярили"
                voice s0448
                s "Да, надо будет повторить"
                voice s0449
                s "Уходим пока не наступило утро"
                voice s0450
                s "Он даже не узнает что мы здесь были"
                m "Обожаю это"
                scene black
                with fade
            "Нет":
                pass
    if game_time == 24 and win_4dan and talk_6sanek and talk_5boris and talk_3tank and talk_3sasha and talk_4maxim and talk_2taras:
        "Вы пришли в последний бой"
        "Вы ТОЧНО готовы?"
        menu finalbost:
            "Да":
                pass
            "Я ещё не готов..":
                show screen map
                play music "music/Path to Lake Land.ogg"
                scene black
                ''
        show pm oshko at right with moveinright
        show ps uwu at left with moveinleft
        show pk with moveinbottom
        voice s0451
        s "Ну вот мы и на месте"
        m "Спустя пол года.."
        k "Пиздец дохуя времени прошло"
        voice s0452
        s "А вроде так быстро"
        voice s0453
        s "Ну ладно"
        voice s0454
        s "Сейчас мы зайдём к этому педофилу"
        voice s0455
        s "И выебим его"
        m "Действуйем же по плану?"
        k "Да ебать"
        k "Которого у нас нету"
        voice s0456
        s "Та похуй"
        voice s0457
        s "Залетаем и выёбываем его"
        hide pk
        show pd scream2 with hpunch
        d "Я спиздел у вас Кирилла!"
        k "Та ты заебал меня пиздить"
        k "Гандон ебаный"
        "Кирилл оталкнул Дениса"
        k "Иди нахуй"
        d "Вам всё равно не одолеть меня!"
        hide pd with moveouttop
        show u zov with moveintop
        "Перед вами появилась \"u zov\""
        u "{bt=3}Я вам запрещяю трогать героя!{/bt}"
        m "Ты вообще знаешь чем он занимаеться?"
        u "{bt=3}Мне не нужно это знать{/bt}"
        u "{bt=3}Если вы зайдёте в подвал то будите иметь дело с великим божеством!{/bt}"
        hide u with moveouttop
        show pk with dissolve
        k "Мы точно справимся?"
        k "Я готов отпиздить Дениса"
        k "Но божество.."
        voice s0458
        s "Та похуй"
        m "Что оно нам сделает"
        k "Но всё таки.."
        k "Ладно"
        k "Заходим!"
        $ OneDiscordMessage("# Глава 1 👹\n{0} начал послдний бой против Дениса".format(persistent.user_name))
        $ fixedset = "finalpodval"
        $ type_battle = "denis"
        $ final_battle = True
        call battle from _call_battle_5
    "Нет..{w} ещё рано.."
    show screen map
    play music "music/Path to Lake Land.ogg"
    scene black
    ''

