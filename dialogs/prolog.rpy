label start:
    if persistent.new_games == 2:
        "Что не первый раз?"
        "Тебя не устроил прошлый конец?"
        "Хочешь что-то изменить?"
        "Хочешь начать всё заново?"
        menu resetInfo:
            "начать всё заново?"
            "Да":
                $ persistent.one_webhook_messages = []
                $ persistent.reset_games += 1
            "Нет":
                $ persistent.reset_games += 1
    $ OneDiscordMessage("Начал новую игру")
    $ state = "something"
    pause(2)
    $ _dismiss_pause = False
    scene main_menu
    with fade
    pause(3)

    $ persistent.new_games += 1
    $ persistent.main_menu = "gui/main_menu.png"
    $ persistent.main_menu_music = "music/disco.mp3"

    play music back
    scene bg shcool with dissolve
    show s smile at left 
    with dissolve
    $ config.rollback_enabled = False
    voice s0016
    s "Здарова"
    $ config.rollback_enabled = True
    voice s0017
    s "Как думаешь сегодня Денис прийдёт в школу?"
    show m at right
    with dissolve
    voice m0027
    m "Конечно{w=2.3}, нет"
    voice m0028
    m "Он за всё время появился всего 3 раза"
    voice m0029
    m "И за эти 3 раза пропал весь 3-А класс"
    voice s0018
    s "Да уж, это страшно"
    voice s0019
    s "Хочешь шутку?"
    voice m0030
    m "Давай"
    voice s0020
    s "Денис"
    m "بالطبع! ما الذي ترغب في معرفته أو مناقشته باللغة العربي"
    voice m0032
    m "Идём в школу, или сьёбёмся играть в CS?"
    menu:
        "Да, сьёбываем нахуй":
            jump uyti

        "Не, я хочу подрочить на уроке":
            jump ostatsa
    return

label uyti:
    $ persistent.first_game = False
    $ OneDiscordMessage("# Пролог 👇\nИдём в школу, или сьёбёмся играть в CS?\n> `Да, сьёбываем нахуй`")
    hide m
    hide s
    scene bg spooke stairs with fade
    "Они ушли домой"
    "Но"
    with dissolve
    $ persistent.remember_d = True
    show d run
    "По пути на них напал Денис"
    play sound cum
    $ persistent.end_game = True
    d " أو مناقشته باللغ"
    if persistent.end_game:
        "Вы вспоминаете что-то"
        show m oshko at right
        show s smile at left
        with dissolve
        "Что даёт вам силы избить Дениса"
        m "Пизди его"
        "Вы начали избивать Дениса"
        pause(1.0)
        "Спустя какое-то время вы закончили"
        s "Ну нахуй{w=1.8}, идём быстрее домой"
        s "Сдесь слишком страшно, педофилы всякие"
        m "Окей, пошли"
        scene bg alea
        with fade
        show m talk at right
        show s at left
        with dissolve
        m "Что будем делать?"
        s "Не знаю{w}, обычно мы идём к Денису когда съебываем"
        s "Но сегодня мы его избили"
        "Вы увидели Бориса который куда-то ищёл"
        show b oshko with dissolve
        m "Ебать{w=1.6} ты что тут делаешь"
        b "Гуляю"
        s "Почему ты не на уроках?"
        b "Уже как 2 урока идёт тревога"
        b "Мне стало скучно и я пошёл ходить"
        b "А вас почему не было сегодня в школе"
        s "У меня есть одна причина важная"
        m "Я спал"
        b "Максим, может мы к тебе что-то посмотрим?"
        m "Можем"
        s "Тогда идём"
        scene bg arka
        with fade
        show m talk at right
        show s at left
        show b oshko
        with dissolve
        b "Вы не когда не думали что будет после смерти?"
        m "Думаю я бы смог переродиться в дитя айдола и стать мега популярной звездой"
        s "Хотелось бы попасть в аниме мир, с магией и гаремом из мужиков"
        b "Круто, я бы тоже хотел попасть в другой мир"
        "Пока они говорили"
        "С зади подбирался всё ближе{w=1} и ближе{w=0.5} Денис"
        scene black
        with hpunch
        "Наступила темнота"
        $ persistent.remember_d = True
        d "Да как вы{w=.2} посмели"
        d "Я убью вас"
        voice s0114
        s "Блять Денис, беги!"
        b "Помогите он меня схватил!"
        menu end_game_boris:
            "Помочь Борису?"
            "Помочь":
                "Пока вы пытались его спасти, Денис убил его"
                "И переключился на вас"
                pass
            "Бежать!":
                "Бросив Бориса"
                jump pobeg
    scene denis
    with fade
    pause 1.5
    $ ending("Умереть от Дениса")
    "Вы слишком слабенькие что бы убежать от Дениса.."
    "[end_message]"
    ''
    return

label ostatsa:
    $ persistent.first_game = False
    $ OneDiscordMessage("# Пролог 👇\nИдём в школу, или сьёбёмся играть в CS?\n> `Не, я хочу подрочить на уроке`")
    voice s0020b
    s "Давай просто пойдём на уроки{w=2}, мы всё равно пропустили 5 уроков"
    voice m0033
    m "Ладно{w=1.5}, идём"
    scene bg shcool2
    pause(1)
    show m talk at right
    with dissolve
    voice m0034
    m "Может он умер{w=1.5}, и мы про это не знаем?"
    show s uwu at left
    with dissolve
    voice s0021
    s "Надеюсь"
    scene black
    "Так они пришли в класс Дениса, что бы проверить пришёл ли он"
    "Странно, но в коридоре не кого не было{w=0.5}. Даже у входа в школу"
    "Может это рук дела Дениса?"
    scene bg myclass
    "Вы пришли в класс"
    show m smile at left
    with dissolve
    voice m0035
    m "Здесь ни-кого нет"
    voice m0036
    m "Хотя урок только начался"
    show s uwu at right
    with dissolve
    voice s0022
    s "Может ещё никто не пришёл?"
    voice s0023
    s "Давай посидим подождём"
    scene black
    with ease
    "Прошло 20 минут"
    scene bg myclass with fade
    pause(1.0)
    voice s0024
    s "слышишь топот?"
    show s ogo
    with dissolve
    voice s0025
    s "Кто-то идёт сюда"
    show s ogo at left
    with move
    ""
    $ persistent.remember_d = True
    show d see at right
    with dissolve
    voice s0026 # ЗАПИСАТЬ
    s "Ух Ебать"
    voice m0037
    m "Ух Ебать"
    "Кто-то под партой Ух Ебать"
    voice m0038
    m "Ты что тут забыл?"
    hide d
    with dissolve
    "Денис молча посмотрел и ушёл"
    show m talk at right
    with dissolve
    voice s0027
    s "Что это было?"
    voice m0039
    m "Хуй его знает{w=2.0}, я сам вахуи"
    "Максим посмотрел в телефон"
    voice m0040
    m "Так уже как 2 урока идёт тревога"
    voice s0028 # ЗАПИСАТЬ
    s "Давай тогда по сьёбам{w=1.8}, тут ещё этот появился мне страшно"
    menu:
        "Пойти в бункер":
            jump bunker
        "Уйти пока не поздно":
            jump pobeg
    return

label bunker:
    scene black
    "Вы начали идти на первый этаж"
    "По пути были слышны крики детей"
    voice s0029
    s "Может нам лучше вернутся?"
    menu back:
        "Сбежать?"
        "Ну нахуй, слишком стрёмно":
            jump pobeg
        "Нет, идём до конца":
            $ OneDiscordMessage("# Пролог 👇\Пойти в бункер?\n> `Нет, идём до конца`")
            voice m0041
            m "Идём до конца"
            voice s0030 # ЗАПИСАТЬ
            s "Ладно"
            "Вы пришли в бункер"
            scene bg bonker
            show m sit at right 
            with dissolve
            show s sit at left
            with dissolve
            voice m0042
            m "Почему в бункере ни-кого нету?"
            voice s0031 # ЗАПИСАТЬ
            s "Хуй его знает"
            voice s0032 # ЗАПИСАТЬ
            s "Го секс"
            voice m0043 # ЗАПИСАТЬ
            m "Го"
            scene black
            "~ах-ах-ах"
            play sound cum
            "اقاقشته بشته باقشته بااقشته بقشته باقشاقشته بته ب"
            scene bg bonker
            show m sit at right
            with dissolve
            show s sit at left
            with dissolve
            voice s0033
            s "Что будем делать?"
            voice m0044
            m "Можем уходить"
            show d screem at center
            play sound cum
            d "قاقشته بشته باقشته بااقشته بقشته باقشاقشته بته ب"
            scene denis
            with fade
            pause 1.5
            $ ending("Умереть от Дениса")
            "Вы слишком слабенькие что бы убежать от Дениса.."
            "[end_message]"

    return

label pobeg:
    $ OneDiscordMessage("# Пролог 👇\nПойти в бункер?\n> `Уйти`")
    
    scene black
    "Вы начали уходить"
    "Всё дальше и дальше"
    
    "Как вдруг"
    play music run
    "Вы услышали как кто-то начал бежать за вами!{w=0.4}{nw}"
    "Вы ускорились{w=0.4}{nw}"
    "На мнгновения Саша развернулся и увидел его..{w=0.4}{nw}"
    show d screem at center
    with vpunch
    "От страха вы начали бежать ещё быстрее{w=0.6}{nw}"
    "Вокруг не было не одного человека{w=0.5}{nw}"
    "Хоть сейчас и был день{w=0.5}{nw}"
    hide d
    "В глазах начало темнеть{w=0.4}{nw}"
    "А он только ускорялся{w=0.3}{nw}"
    ".{w=0.1}.{w=0.1}.{w=0.1}{nw}"
    "Вы добежали до какого-то заброшеного дома{w=0.4}, тут была она дырка{w=0.6}{nw}"
    menu kto_idet:
        "Кто пойдёт"
        "Макс":
            $ OneDiscordMessage("# Пролог 👇\nКто пойдёт?\n> `Макс`")
            "Максим зашёл в заброшенный дом"
            "В друг за ним закрываются двери"
            play music mansion
            play audio "volk.mp3"
            "На фоне он услышал вой одинокого волка"
            scene bg zd
            voice m0045
            voice m0046
            m "Он вроде от нас отстал"
            show m talk
            with dissolve
            voice m0047
            m "Почему за мной закрылась дверь"
            "Макс решил осмотреться и найти выход"
            "? ? ?" "Стой"
            voice m0048
            m "Динах"
            hide m
            "Макс продолжил ходить"
            "Как вдруг его кто-то схватил за плечё"
            $ persistent.remember_k = True
            show k 
            with dissolve
            voice k0001
            k "Ты еблан?"
            show k at left
            with move
            show m at right
            with dissolve
            voice m0049
            m "Да"
            voice k0002
            k "Далбоёб ты как с Украины в Польшу прибижал"
            voice k0003
            k "Ты один?"
            voice m0050
            m "Нет, со мной был Саша"
            voice k0004
            k "Где ты его проебал"
            voice m0051
            m "Хуй его знает"
            "{i}Макс рассказал что было{/i}"
            voice k0005
            k "А так блять"
            voice k0006
            k "Пизда ему"
            voice m0052
            m "Да"
            voice k0007
            k "Пизда"
            with vpunch
            "{i}Кто-то начал выбивать дверь{/i}"
            voice m0053
            m "Кто это"
            voice k0008
            k "Та хуй его знает, доставка наверное"
            voice m0054
            m "Так ебать{w=1.2}, идём откроем"
            scene bg door
            "Вы пошли к двери"
            voice m0055
            m "Какого хуя у тебя дверь из золота{w=2.2}, а сам дом разьёбаный?"
            voice k0009
            k "Тебя ебать не должно"
            "{i}Кто-открыл дверь{/i}"
            show d run
            with dissolve
            voice k0010
            k "ЗА МНОЙ"
            "{i}Вы начали убегать{/i}"
            scene black
            with vpunch
            "Бежав Кирилл споткнулся"
            menu ku:
                "Помочь?"
                "Помочь":
                    $ kHelp = True
                    "{i}Вы помогли Кириллу{/i}"
                    $ renpy.notify("Кирилл это запомнит")
                    pass
                "Оставить хохла":
                    "{i}Вы не помогли Кириллу{/i}"
                    "{i}Вы посчитали что ваша девственность важнее{/i}"
                    "{i}Кирилл побежал дальше{/i}"
                    $ renpy.notify("Кирилл это запомнит")
                    pass
            "{i}Вы добежали до подвала и закрыли дверь{/i}"
            scene bg podval
            with fade
            show m talk at left
            with moveinleft
            voice m0096
            m "Вроде убежали"
            show k at right
            with moveinright
            if kHelp:
                voice k0011
                k "Спасибо что помог"
                voice k0012
                k "Без тебя меня бы трахнули"
            voice k0013
            k "Переждём здесь, тут безопасно"
            "{i}Вы услышали какой-то звук{/i}"
            play music fight
            show s
            with pixellate
            "Появился Саша"
            voice s0034
            s "Пидарас кинул меня, тоби пизда" # ЗАПИСАТЬ
            "Fight!"
            "Round 1!"
            voice s0035
            s "Когда у меня день рождение?"
            menu round1:
                "Когда у меня день рождение?"
                "27.07.2007":
                    $ FigthPoints -= 1
                    pass
                "26.06.2007":
                    voice s0035b 
                    s "Почти, пидарас" # ЗАПИСАТЬ
                    $ FigthPoints -= 1
                    pass
                "27.06.2006":
                    voice s0035c 
                    s "Не верно" # ЗАПИСАТЬ
                    $ FigthPoints -= 1
                    pass
                "26.06.2006":
                    voice s0035v 
                    s "Хоть это ты знаешь" # ЗАПИСАТЬ
                    $ FigthPoints += 2
                    pass
                "28.07.2007":
                    voice s0035z 
                    s "Всё мимо" # ЗАПИСАТЬ
                    $ FigthPoints -= 1
                    pass
            "Round 2"
            voice s0036
            s "Какой мой любимый цвет?"
            menu optional_name:
                "Какой мой любимый цвет?"
                "Синий":
                    $ FigthPoints -= 1
                    pass
                "Красный":
                    $ FigthPoints -= 1
                    pass
                "Фиолетовый":
                    $ FigthPoints -= 1
                    pass
                "Коричневый":
                    voice s0037 # ЗАПИСАТЬ
                    s "Боже бот, иди нахуй"
                    voice s0038 # ЗАПИСАТЬ
                    s "Это мой не любимый цвет"
                    voice s0039 # ЗАПИСАТЬ
                    s "Иди повесья"
                    scene black
                    "Вы выбрали не тот цвет"
                    "Саша призвал Дениса"
                    show d screem
                    "Смертельная концовка"
                    return
                "Черный":
                    $ FigthPoints -= 1
                    pass
                "Желтый":
                    $ FigthPoints -= 1
                    pass
                "Зелёный":
                    voice s0040
                    s "Да но какой отеннок"
                    menu optional_name2:
                        "Какой любимый отеннок зелёного"
                        "Лесной":
                            $ FigthPoints -= 1
                            pass
                        "Весений":
                            $ FigthPoints -= 1
                            pass
                        "Яблоко-гренни":
                            $ FigthPoints -= 1
                            pass
                        "Лайм":
                            voice s0041
                            s "Ебать чёрт, всё знаешь" # ЗАПИСАТЬ
                            $ FigthPoints += 2
                            pass
                        "Нефритовый":
                            $ FigthPoints -= 1
                            pass
                        "Морской":
                            $ FigthPoints -= 1
                            pass
                        
                    pass
                "Белый":
                    $ FigthPoints -= 1
                    pass
                "Розовый":
                    $ FigthPoints -= 1
                    pass
                "Голубой":
                    $ FigthPoints -= 1
                    pass
            "Round 3"
            voice s0042 # ЗАПИСАТЬ
            s "Кто стоит на обложке Sex Simulator?"
            menu round3:
                "Кто стоит на обложке Sex Simulator?"
                "Денис":
                    voice s0043
                    s "Та хуй там" # ЗАПИСАТЬ
                    $ FigthPoints -= 1
                    pass
                "Борис":
                    $ FigthPoints += 2
                    voice s0044
                    s "Это легко"
                    voice s0045
                    s "А теперь посмотрим запускал ли ты игру вообще"
                    voice s0046
                    s "Сколько всего там концовок?"
                    menu skolko: 
                        "Сколько всего там концовок?"
                        "1":
                            voice s0047
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "2":
                            voice s0047
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "3":
                            voice s0047
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "4":
                            voice s0047
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "5": 
                            voice s0048
                            s "Вау{w=0.4}, я поражен"
                            voice s0049
                            s "Я даже сам не помнил сколько их"
                            $ FigthPoints += 2
                            pass
                        "6":
                            voice s0047
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                            pass
                "Макс":
                    voice s0050
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Саша":
                    voice s0051
                    s "Лол нет"
                    $ FigthPoints -= 1
                    pass
                "Рома":
                    voice s0050
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Кирилл":
                    voice s0050
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Тарас":
                    voice s0050
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Гитлер":
                    voice s0052
                    s "Пошёл нахуй уебан" # ЗАПИСАТЬ
                    "{i}Саша призвал дениса{/i}"
                    show d scream2
                    hide m
                    hide s
                    hide k
                    play audio cum
                    d "مرحبًا بك في عالم اللغة العربية!"
                    scene denis
                    with fade
                    pause 1.5
                    $ ending("Умереть от Дениса")
                    "Вы слишком слабенькие что бы убежать от Дениса.."
                    "[end_message]"
                    return
                    pass
                "Пригожин":
                    voice s0053 # ЗАПИСАТЬ
                    s "Ебать ты аутист"
                    $ FigthPoints -= 1
                    pass
            $ FigthPointsToWin = 6
            if persistent.difficulty == 2:
                $ FigthPointsToWin = 4
            elif persistent.difficulty == 1:
                $ FigthPointsToWin = 2
                
            if FigthPoints >= FigthPointsToWin:
                play audio "Intro.wav"
                stop music
                voice s0054
                s "Вы ответили правильно на мои вопросы"
                show s smile
                play music mansion
                voice s0055 # ЗАПИСАТЬ
                s "Ладно, сорян что хотел трахнуть вас"
                voice m0056
                m "Та иди ты нахуй"
                voice k0014
                k "А я и не против был"
                show d scream2 at right with vpunch
                hide k
                d "Я спиздел у вас Кирилла"
                d "Если хотите его"
                d "Идите на кладбище"
                hide d
                pause 1.0
                voice s0056
                s "Может ну его нахуй"
                voice s0057
                s "Просто уйдём домой и всё"
                menu posiobam:
                    "Уйти?"
                    "Да":
                        play music "music/BitWaves.wav"
                        voice m0057
                        m "Согласен"
                        voice m0058
                        m "Лучше не встревать во всю эту хуйню"
                        voice m0059
                        m "А Кирилл пусть сам разбераеться там"
                        voice s0058
                        s "Рил"

                        "Вы ушли по домам{w=0.4}, по забыв обо всём что сегодня произошло"
                        #Надо добавить концовку
                        $ ending("Уйти по домам")
                        "[end_message]"
                        return
                    "Пойти на кладбище":
                        pass
            else:
                voice s0059
                s "Вы не ответели правильно.."
                "{i}Саша призвал дениса{/i}"
                show d scream2
                hide m
                hide s
                hide k
                play audio cum
                d "مرحبًا بك في عالم اللغة العربية!"
                scene denis
                with fade
                pause 1.5
                $ ending("Умереть от Дениса")
                "Вы слишком слабенькие что бы убежать от Дениса.."
                "[end_message]"
                return
            pass
        "Саша":
            $ OneDiscordMessage("# Пролог 👇\nКто пойдёт?\n> `Саша`")
            "Саша зашёл в заброшенный дом"
            "В друг за ним закрываются двери"
            play music mansion
            play audio "volk.mp3"
            "На фоне он услышал вой одинокого волка"
            scene bg zd
            voice s0060
            s "Он вроде от нас отстал"
            show s smile
            with vpunch
            voice s0061
            s "Почему за мной закрылась дверь"
            "Саша решил осмотреться и найти выход"
            "? ? ?" "Крики детей"
            voice s0062 # ЗАПИСАТЬ
            s "Хто ты нахуй?"
            "Саша развернулся и увидел его"
            show s smile at left
            with move
            $ persistent.remember_k = True
            show k at right
            with dissolve
            voice k0015
            k "Ты шо тут забыл"
            voice s0063
            s "Там педофил за мной и Максом бежал"
            voice k0016
            k "И где Макс?"
            voice s0064
            s "Тут был"
            voice k0017
            k "Ладно{w=1.4}, а как ты блять с Украины в Польшу прибежал"
            voice s0065
            s "Смог{w=1.2}, я сигма"
            with vpunch
            "Вы услышали что кто-то ломиться в дверь"
            voice s0066
            s "Это этот, надо где-то спрятаться"
            voice k0018
            k "Идём за мной, на чердак"
            scene black
            "{i}Вы начали подниматься на чердак{/i}"
            with vpunch
            "Как вдруг, Кирилл упал на резиновый член"
            menu ku2:
                "Помочь?"
                "Помочь":
                    $ OneDiscordMessage("# Пролог 👇\nПомочь кириллу?\n> `Помочь`")
                    $ kHelp = True
                    "{i}Вы помогли Кириллу{/i}"
                    "{i}Но могли бы не помогать{/i}"
                    $ renpy.notify("Кирилл это запомнит")
                    pass
                "Оставить хохла":
                    $ OneDiscordMessage("# Пролог 👇\nПомочь кириллу?\n> `Оставить хохла`")
                    "{i}Вы не помогли Кириллу{/i}"
                    "{i}Вы посчиитали что ваша девственность важнее{/i}"
                    "{i}У Кирилла встал{/i}"
                    $ renpy.notify("Кирилл это запомнит")
                    pass
            "{i}Вы поднялись на чердак{/i}"
            scene bg cherdak
            with fade
            show s uwu
            with dissolve
            voice s0067 # ЗАПИСАТЬ
            s "Ебать"
            voice s0068 # ЗАПИСАТЬ
            s "Какого хуя у тебя разьёбаный дом"
            show s ogo at left
            with move
            show k at right
            with move
            voice k0019
            k "Нормальный{w=1.2}, ты даун просто"
            "{i}В углу комнаты, вы услышали шорох{/i}"
            "{i}Вы подошли посмотреть..{/i}"
            play music fight
            show m see
            with zoominout
            with pixellate
            voice m0060
            m "Ах ты пидарас"
            voice m0061
            m "Ты меня бросил"
            voice m0062
            m "Я выебу вас обоих"
            voice k0020
            k "Э{w=1.0}, а меня за что"
            "Fight"
            "Round 1"
            voice m0063
            menu mfr1:
                "Кто был первым участником ХАЖАБЫ?"
                "Кирилл":
                    voice m0064
                    m "Нет, не правильно"
                    $ FigthPoints -= 1
                    pass
                "Борис":
                    voice m0065
                    m "Кто это?"
                    $ FigthPoints -= 2
                    pass
                "Денис":
                    voice m0066
                    m "Почти"
                    $ FigthPoints -= 1
                    pass
                "Саша":
                    voice m0067
                    m "Знаешь всё кроме меня пидар"
                    $ FigthPoints += 2
                    pass
                "Макс":
                    voice m0068
                    m "Умный пидарас"
                    hide m
                    hide s
                    hide k
                    show d scream2
                    play audio cum
                    m "ا بك في عالم اللغة العر"
                    scene denis
                    with fade
                    pause 1.5
                    $ ending("Умереть от Дениса")
                    "Вы слишком слабенькие что бы убежать от Дениса.."
                    "[end_message]"
                    return
            "Round 2"
            voice m0069
            menu dasd:
                "Когда у меня день рождение?"
                "16 числа":
                    $ FigthPoints -= 1
                    pass
                "18 числа":
                    $ FigthPoints -= 1
                    pass
                "19 числа":
                    $ FigthPoints += 2
                    voice m0069b
                    m "Правильно"
                    voice m0070
                    m "Но какой месяц"
                    menu datem:
                        "Месяц рождения"
                        "19 Января":
                            $ FigthPoints -= 1
                            pass
                        "19 Февраля":
                            $ FigthPoints += 2
                            voice m0071
                            m "Это все знают{w=1.8}, а год какой?"
                            menu yearm:
                                "В каком году"
                                "19 Февраля 2006г":
                                    voice m0072
                                    m "Ты ахуел"
                                    show d scream2
                                    "{i}Макс призвал дениса{/i}"
                                    hide m
                                    hide s
                                    hide k
                                    play audio cum
                                    d "مرحبًا بك في عالم اللغة العربية!"
                                    scene denis
                                    with fade
                                    pause 1.5
                                    $ ending("Умереть от Дениса")
                                    "Вы слишком слабенькие что бы убежать от Дениса.."
                                    "[end_message]"

                                    return
                                "19 Февраля 2007г":
                                    voice m0073
                                    m "Это информация была в боте"
                                    voice m0074
                                    m "Во сколько я радился"
                                    menu hourm:
                                        "Во сколько я радился"
                                        "19 Февраля 2007г в 2:00":
                                            voice m0075
                                            m "Вау, я поражён"
                                            voice m0076
                                            m "Ты точно знаешь когда я родился"
                                            voice m0077
                                            m "Честно даже я не знал об этом"
                                            $ FigthPoints += 2
                                        "19 Февраля 2007г в 4:00":
                                            voice m0078
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "19 Февраля 2007г в 5:27":
                                            voice m0078
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "19 Февраля 2007г в 6:00":
                                            voice m0078
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "Иди нахуй":
                                            voice m0072
                                            m "Ты ахуел"
                                            show d scream2
                                            hide m
                                            hide s
                                            hide k
                                            "{i}Макс призвал дениса{/i}"
                                            play audio cum
                                            d "مرحبًا بك في عالم اللغة العربية!"
                                            scene denis
                                            with fade
                                            pause 1.5
                                            $ ending("Умереть от Дениса")
                                            "Вы слишком слабенькие что бы убежать от Дениса.."
                                            "[end_message]"
                                            return
                            pass
                        "19 Марта":
                            $ FigthPoints -= 1
                            pass
                        "19 Апреля":
                            $ FigthPoints -= 1
                            pass
                        "19 Мая":
                            $ FigthPoints -= 1
                            pass
                    pass
                "20 числа":
                    $ FigthPoints -= 1
                    pass
                "21 числа":
                    $ FigthPoints -= 1
                    pass
                "22 числа":
                    $ FigthPoints -= 1
                    pass
            voice k0021
            k "Давай я тебе помогу"
            "Round 3"
            voice m0079
            m "Когда была создана ХАЖАБА"
            if kHelp:
                voice k0022
                k "Дай подумаю.."
                voice k0023
                k "Ты мне помог, по этому я взломаю вселенную и найду ответ"
                voice k0024
                k "Г жцмцп пну Хитцъ хфуесэ, цеш адт мнъимчнт ицу кыа ухнкъпбыч .. Денис"
                $ OneDiscordMessage("# Пролог 😈\nКирилл помог Саше")
                voice m0080
                m "Не знаю почему{w=1.8}, но это правильный ответ"
                $ FigthPoints += 1
            else:
                voice k0022
                k "Дай подумаю.."
                voice k0025
                k "Я не знаю"
                $ OneDiscordMessage("# Пролог 😈\nКирилл не помог Саше")
                voice m0081
                m "Это не правильный ответ!"
            
            $ FigthPointsToWin = 6
            if persistent.difficulty == 2:
                $ FigthPointsToWin = 4
            elif persistent.difficulty == 1:
                $ FigthPointsToWin = 2

            if FigthPointsToWin >= FigthPointsToWin:
                $ OneDiscordMessage("# Пролог 😈\nСаша смог одолеть Макса")
                play audio "Intro.wav"
                stop music
                voice m0082
                m "Вы ответили правильно на мои вопросы"
                hide m
                show m talk
                play music mansion
                voice m0083
                m "Ладно простите что чуть не выебал вас"
                voice s0068b # ЗАПИСАТЬ
                s "Ты аухел?"
                voice s0069 # ЗАПИСАТЬ
                s "Чуть нас не выебал пидарас"
                hide k
                show d scream2 at right with vpunch
                d "Я спиздел у вас Кирилла"
                d "Если хотите его"
                d "Идите на кладбище"
            else:
                $ OneDiscordMessage("# Пролог 😈\nСаша не смог одолеть Макса")
                voice m0083b
                m "Вы не ответили правильно.."
                "{i}Макс призвал Дениса{/i}"
                show d scream2
                hide m
                hide s
                hide k
                play audio cum
                d "مرحبًا بك في عالم اللغة العربية!"
                scene denis
                with fade
                pause 1.5
                $ ending("Умереть от Дениса")
                "Вы слишком слабенькие что бы убежать от Дениса.."
                "[end_message]"
                return
            pass
    jump morg

label morg:
    scene black
    "Прошёл час"
    play music shag
    "Макс и Саша отправились на кладбище"
    voice s0070 # ЗАПИСАТЬ
    s "Нахуй мы за ним идём"
    voice s0071
    s "Там Денис{w=1.4}, там опасно"
    voice m0084
    m "Он мне шаурму должен"
    voice s0072
    s "Достойная причина, тогда и мне"
    "{i}Так они трахались{w=0.4}, потом они пришли на кладбище{/i}"
    $ OneDiscordMessage("# Пролог 🚶\nСаша и Макс пришли на кладбище")
    scene bg morg
    play music "music/Venus.wav"
    pause(3.5)
    show m talk
    with dissolve
    voice m0085
    m "Он должен быть где-то здесь"
    hide m
    show m talk at right
    with move
    show s at left
    with move
    voice s0073
    s "Предлагаю поискать"
    voice s0074
    s "Я осмотрюсь здесь, ты иди дальше"
    voice m0086
    m "Ладно пойду до того не разу не подозрительного склеба"
    hide m
    show s at center
    "{i}Саша начал осматриваться{/i}"
    "{i}Как вдруг к нему кто-то подошёл{/i}"
    "{i}И схватил его за плечё{/i}"
    stop music
    with fade
    "{i}У него потемнело в глазах..{/i}"
    with fade
    with fade
    with fade
    with fade
    scene black
    play audio "peremena1.mp3" volume 0.1
    pause(3)
    "Саша услышал звук deti.m4a"
    play music back
    voice s0074b
    s "Где я"
    voice s0075
    s "Знакомая музыка"
    scene dbg shcool
    with fade
    show s
    voice s0076
    s "Это же наша школа"
    voice s0077
    s "Что я тут делаю"
    "{i}Саша посмотрел на часы{/i}"
    voice s0078
    "8:14"
    voice s0079
    s "Уроки только начались"
    voice s0080
    s "Видимо то что произошло был всего лишь сон"
    voice s0081
    s "Или я перебрал с мефедроном"
    voice s0082
    s "В любом случае я опаздываю на урок{w=2.4}, хотя обычно это делает Макс"
    scene dbg shcool2
    "{i}Саша направился ближе ко входу{/i}"
    if persistent.end_game:
        "? ? ?" "Давай ты сможешь"
    "Как вдруг он заметил Макса"
    show dm
    voice s0083 # ЗАПИСАТЬ
    s "О еблан"
    voice s0084 # ЗАПИСАТЬ
    s "Иди сюда"
    "{i}Макс не отреагировал на слова Саши{/i}"
    "{i}Он продолжил идти{/i}"
    hide dm
    voice s0085 # ЗАПИСАТЬ
    s "Пидарас игнорит меня"
    "{i}Саша побежал за ним{/i}"
    scene black
    "{i}Саша зашёл в школу за ним{/i}"
    "К его удивлению он не пошёл в класс"
    "{i}Саша попытался дотронуться до Макса{/i}"
    "Но у него ни чего не получилось"
    "Рука прошла сквозь него к члену"
    "{i}Макс улыбнулся){/i}"
    voice s0086
    s "Почему я не могу до него дотронутся"
    voice s0087
    s "Может это всё сон?"
    voice s0088
    s "И на самом деле сейчас я лежу от передоза"
    voice s0089
    s "Ладно продолжу смотреть сон"
    scene dbg bonker
    with fade
    voice s0090
    s "Стой"
    voice s0091
    s "Что ты делаешь"
    voice s0092
    s "Не призывай его"
    voice s0093
    s "Он всю школу выебет"
    "{i}Макс проигнорировал его{/i}"
    m "حبًا بك في عالم اللغة العربيحبًا بك في عالم اللغة العربي"
    "Он призвал Дениса"
    if persistent.end_game:
        "? ? ?" "Я надеюсь ты всё правильно поймёшь"
    show d aun
    play audio dk
    $ OneDiscordMessage("# Пролог 🫢\nСаша узнал прошлое")
    d "Нахуй ты меня призвал"
    d "В наказание я выебу тебя и всех кто тут есть"
    voice m0087
    m "Стой"
    voice m0088
    m "Я призвал тебя что бы ты помог"
    with fade
    if persistent.end_game:
        "? ? ?" "Удачи тебе"
    "У Саши начало темнеть в глазах"
    with fade
    with fade
    with fade
    scene black
    stop music
    voice s0094
    s "Видимо я начал просыпаться"
    play music "music/Venus.wav"
    scene bg morg
    with fade
    "{i}Саша очнулся{/i}"
    show s
    with dissolve
    voice s0095
    s 'Я должен найти Кирилла'
    voice s0096
    s "И узнать что произошло сегодня утром"
    voice s0097
    s "Сначала осмотрюсь здесь"
    "Саша начал ходить по кладбищу"
    "{i}Он подошёл к одной могиле{/i}"
    scene mogb
    with fade
    voice s0098
    s "Кого-то это напоминает"
    voice s0099
    s "Но не помню кого"
    menu boris:
        "Fress F?"
        "F":
            $ OneDiscordMessage("# Пролог 👇\nСаша отдал честь Борису")
            "Саша выбрал отдать честь погибшему"
            "F"
            pass
        "Нассать на могилу":
            $ OneDiscordMessage("# Пролог 👇\nСаша нассал на могилу")
            "Саша ссал на правила"
            "{i}Саша обсосал могилу{/i}"
            $ mogila_borisa = True
            $ cost_multiplate += 0.15
            pass
    $ renpy.notify("Это действие будет иметь последствия")
    scene bg morg
    with fade
    show s
    with dissolve
    voice s0100
    s "Что ж, я ни чего не нашёл"
    voice s0101
    s "Пойду к Максу"
    voice s0102
    s "Узнаю что он нашёл"
    "{i}Саша пошёл в сторону склепа{/i}"
    scene black
    voice s0103
    s "Интересно"
    voice s0104
    s "Пятую минуту снаффа тут снимали?"
    scene bg scleb
    with fade
    pause(1)
    show m da
    with dissolve
    voice m0089
    m "О здарова"
    voice m0090
    m "Мне кажется они в этом гробу"
    show m da at right
    with moveinright
    "{i}Вы услышали тихие стоны{/i}"
    voice m0091
    m "Эти пидары явно что-то там делают"
    voice s0105
    s "Дай я послушаю"
    show s
    with dissolve
    "Саша послушал стоны" # КИРИЛЛ ОЗВУЧ
    voice s0106 # ЗАПИСАТЬ
    s "Ебать"
    voice s0107 # ЗАПИСАТЬ
    s "Он Кирилла там трахает?"
    voice m0092
    m "Хуй знает, может дрочит так"
    voice s0108
    s "Давай откроем, посмотрим"
    show s at left
    with moveinleft
    "Вы подошли к гробу"
    menu:
        "Открыть крышку гроба?"
        "Открыть":
            $ OneDiscordMessage("# Пролог 👇\n{0} открыл гроб..".format(persistent.user_name))
            "То что вы увидели"
            "Было ужасно"
            "Перед вами был расчленённый труп Кирилла"
            voice s0109
            s "Что за хуйня"
            voice m0093
            m "БДСМ с Денисом"
            voice s0110
            s "Я вахуи"
            "Из гроба вы увидели луч света"
            "Как вдруг вас затянуло.."
            jump deadw
        "Сбежать":
            $ OneDiscordMessage("# Пролог 👇\n{0} решил сбежать".format(persistent.user_name))
            pass
    "Вы решили оставить их в покое"
    voice s0111
    s "Слушай"
    voice s0112
    s "Это их отношения или сношения"
    voice s0113
    s "Пускай занимаются чем, хотят"
    voice m0094
    m "Ладно, не будем мешать"
    voice m0095
    m "Уходим"
    scene black
    with fade
    "Вы ушли из склеба"
    "Но на выходе{w=0.4}, был{w=0.2} он{w=0.4}{nw}"
    scene bg morg
    with fade
    pause(1)
    show d scream2
    with dissolve
    d "Я вас выебу{w=0.6}{nw}"
    voice s0114
    s "Блять Денис, беги!{w=0.6}{nw}"
    with vpunch
    scene black
    stop music
    "{fi}Пролог пройден{/fi}{w=6}{nw}"
    jump deadw
    $ OneDiscordMessage("# Пролог 🏅\n{0} завершил пролог!".format(persistent.user_name))
    return