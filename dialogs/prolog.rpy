label start:
    $ state = "something"
    pause(2)
    $ _dismiss_pause = False
    scene main_menu
    with fade
    pause(3)
    $ renpy.notify(persistent.endings)
    $ persistent.main_menu = "gui/main_menu.png"
    $ persistent.main_menu_music = "music/disco.mp3"

    play music back
    scene bg shcool with dissolve
    show s smile at left 
    with dissolve
    s "Здарова"
    s "Как думаешь сегодня Денис прийдёт в школу?"
    show m at right
    with dissolve
    m "Конечно{w}, нет"
    m "Он за всё время появился всего 3 раза"
    m "И за эти 3 раза пропал весь 3-А класс"
    s "Да уж, это страшно"
    s "Хочешь шутку?"
    m "Давай"
    s "Денис"
    m "بالطبع! ما الذي ترغب في معرفته أو مناقشته باللغة العربي"
    m "Идём в школу, или сьёбёмся играть в CS?"
    menu:
        "Да, сьёбываем нахуй":
            jump uyti

        "Не, я хочу подрочить на уроке":
            jump ostatsa
    return

label uyti:
    hide m
    hide s
    scene bg spooke stairs with fade
    "Они ушли домой"
    "Но"
    with dissolve
    show d run
    "По пути на них напал Денис"
    play sound cum
    d " أو مناقشته باللغ"
    scene denis
    with fade
    pause 1.5
    $ ending("Умереть от Дениса")
    "Вы слишком слабенькие что бы убежать от Дениса.."
    "[end_message]"
    ''
    return

label ostatsa:
    s "Давай просто пойдём на уроки{w}, мы всё равно пропустили 5 уроков"
    m "Ладно{w}, идём"
    scene bg shcool2
    pause(1)
    show m talk at right
    with dissolve
    m "Может он умер{w}, и мы про это не знаем?"
    show s uwu at left
    with dissolve
    s "Надеюсь"
    scene black
    "Так они пришли в класс Дениса, что бы проверить пришёл ли он"
    "Странно, но в коридоре не кого не было{w}. Даже у входа в школу"
    "Может это рук дела Дениса?"
    scene bg myclass
    "Вы пришли в класс"
    show m smile at left
    with dissolve
    m "Здесь ни-кого нет"
    m "Хотя урок только начался"
    show s uwu at right
    with dissolve
    s "Может ещё никто не пришёл?"
    s "Давай посидим подождём"
    scene black
    with ease
    "Прошло 20 минут"
    scene bg myclass with fade
    "."
    " .  . . .  ."
    s "слышишь топот?"
    show s ogo
    with dissolve
    s "Кто-то идёт сюда"
    show s ogo at left
    with move
    ""
    show d see at right
    with dissolve
    s "Ух Ебать"
    m "Ух Ебать"
    "Кто-то под партой Ух Ебать"
    m "Ты что тут забыл?"
    hide d
    with dissolve
    "Денис молча посмотрел и ушёл"
    show m talk at right
    with dissolve
    s "Что это было?"
    m "Хуй его знает{w}, я сам вахуи"
    "Максим посмотрел в телефон"
    m "Так уже как 2 урока идёт тревога"
    s "Давай тогда по сьёбам{w}, тут ещё этот появился мне страшно"
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
    s "Может нам лучше вернутся?"
    menu back:
        "Сбежать?"
        "Ну нахуй, слишком стрёмно":
            jump pobeg
        "Нет, идём до конца":
            m "Идём до конца"
            s "Ладно"
            "Вы пришли в бункер"
            scene bg bonker
            show m sit at right 
            with dissolve
            show s sit at left
            with dissolve
            m "Почему в бункере ни-кого нету?"
            s "Хуй его знает"
            s "Го секс"
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
            s "Что будем делать?"
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
    
    scene black
    "Вы начали уходить"
    "Всё дальше и дальше"
    
    "Как вдруг"
    play music run
    "Вы услышали как кто-то начал бежать за вами!"
    "Вы ускорились"
    "На мнгновения Саша развернулся и увидел его.."
    show d screem at center
    with vpunch
    "От страха вы начали бежать ещё быстрее"
    "Вокруг не было не одного человека"
    "Хоть сейчас и был день"
    hide d
    "В глазах начало темнеть"
    "А он только ускорялся"
    ".{w}.{w}.{w}"
    "Вы добежали до какого-то заброшеного дома{w}, тут была она дырка"
    menu kto_idet:
        "Кто пойдёт"
        "Макс":
            "Максим зашёл в заброшенный дом"
            "В друг за ним закрываются двери"
            play music mansion
            play audio "volk.mp3"
            "На фоне он услышал вой одинокого волка"
            scene bg zd
            m "Он вроде от нас отстал"
            show m talk
            with dissolve
            m "Почему за мной закрылась дверь"
            "Макс решил осмотреться и найти выход"
            "? ? ?" "Стой"
            m "Динах"
            hide m
            "Макс продолжил ходить"
            "Как вдруг его кто-то схватил за плечё"
            show k 
            with dissolve
            k "Ты еблан?"
            show k at left
            with move
            show m at right
            with dissolve
            m "Да"
            k "Далбоёб ты как с Украины в Польшу прибижал"
            k "Ты один?"
            m "Нет, со мной был Саша"
            k "Где ты его проебал"
            m "Хуй его знает"
            "{i}Макс рассказал что было{/i}"
            k "А так блять"
            k "Пизда ему"
            m "Да"
            k "Пизда"
            with vpunch
            "{i}Кто-то начал выбивать дверь{/i}"
            m "Кто это"
            k "Та хуй его знает, доставка наверное"
            m "Так ебать{w}, идём откроем"
            scene bg door
            "Вы пошли к двери"
            m "Какого хуя у тебя дверь из золота{w}, а сам дом разьёбаный?"
            k "Тебя ебать не должно"
            "{i}Кто-открыл дверь{/i}"
            show d run
            with dissolve
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
            m "Вроде убежали"
            show k at right
            with moveinright
            if kHelp:
                k "Спасибо что помог"
                k "Без тебя меня бы трахнули"
            k "Переждём здесь, тут безопасно"
            "{i}Вы услышали какой-то звук{/i}"
            play music fight
            show s
            with pixellate
            "Появился Саша"
            s "Пидарас кинул меня, тоби пизда"
            "Fight!"
            "Round 1!"
            menu round1:
                "Когда у меня день рождение?"
                "27.07.2007":
                    $ FigthPoints -= 1
                    pass
                "26.06.2007":
                    s "Почти, пидарас"
                    $ FigthPoints -= 1
                    pass
                "27.06.2006":
                    s "Не верно"
                    $ FigthPoints -= 1
                    pass
                "26.06.2006":
                    s "Хоть это ты знаешь"
                    $ FigthPoints += 2
                    pass
                "28.07.2007":
                    s "Всё мимо"
                    $ FigthPoints -= 1
                    pass
            "Round 2"
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
                    s "Боже бот, иди нахуй"
                    s "Это мой не любимый цвет"
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
                            s "Ебать чёрт, всё знаешь"
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
            menu round3:
                "Кто стоит на обложке Sex Simulator?"
                "Денис":
                    s "Та хуй там"
                    $ FigthPoints -= 1
                    pass
                "Борис":
                    $ FigthPoints += 2
                    s "Это легко"
                    s "А теперь посмотрим запускал ли ты игру вообще"
                    menu skolko: 
                        "Сколько всего там концовок?"
                        "1":
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "2":
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "3":
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "4":
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                        "5": 
                            s "Вау{w}, я поражен"
                            s "Я даже сам не помнил сколько их"
                            $ FigthPoints += 2
                            pass
                        "6":
                            s "Неправильно"
                            $ FigthPoints -= 1
                            pass
                            pass
                "Макс":
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Саша":
                    s "Лол нет"
                    $ FigthPoints -= 1
                    pass
                "Рома":
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Кирилл":
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Тарас":
                    s "Нет"
                    $ FigthPoints -= 1
                    pass
                "Гитлер":
                    s "Пошёл нахуй уебан"
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
                    s "Ебать ты аутист"
                    $ FigthPoints -= 1
                    pass
            if FigthPoints >= 6:
                play audio "Intro.wav"
                stop music
                s "Вы ответили правильно на мои вопросы"
                show s smile
                play music mansion
                s "Ладно, сорян что хотел трахнуть вас"
                m "Та иди ты нахуй"
                k "А я и не против был"
                show d scream2 at right with vpunch
                hide k
                d "Я спиздел у вас Кирилла"
                d "Если хотите его"
                d "Идите на кладбище"
                hide d
                pause 1.0
                s "Может ну его нахуй"
                s "Просто уйдём домой и всё"
                menu posiobam:
                    "Уйти?"
                    "Да":
                        play music "music/BitWaves.wav"
                        m "Согласен"
                        m "Лучше не встревать во всю эту хуйню"
                        m "А Кирилл пусть сам разбераеться там"
                        s "Рил"

                        "Вы ушли по домам{w}, по забыв обо всём что сегодня произошло"
                        #Надо добавить концовку
                        $ ending("Уйти по домам")
                        "[end_message]"
                        return
                    "Пойти на кладбище":
                        pass
            else:
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
            "Саша зашёл в заброшенный дом"
            "В друг за ним закрываются двери"
            play music mansion
            play audio "volk.mp3"
            "На фоне он услышал вой одинокого волка"
            scene bg zd
            s "Он вроде от нас отстал"
            show s smile
            with vpunch
            s "Почему за мной закрылась дверь"
            "Саша решил осмотреться и найти выход"
            "? ? ?" "Крики детей"
            s "Хто ты нахуй?"
            "Саша развернулся и увидел его"
            show s smile at left
            with move
            show k at right
            with dissolve
            k "Ты шо тут забыл"
            s "Там педофил за мной и Максом бежал"
            k "И где Макс?"
            s "Тут был"
            k "Ладно{w}, а как ты блять с Украины в Польшу прибежал"
            s "Смог{w}, я сигма"
            with vpunch
            "Вы услышали что кто-то ломиться в дверь"
            s "Это этот, надо где-то спрятаться"
            k "Идём за мной, на чердак"
            scene black
            "{i}Вы начали подниматься на чердак{/i}"
            with vpunch
            "Как вдруг, Кирилл упал на резиновый член"
            menu ku2:
                "Помочь?"
                "Помочь":
                    $ kHelp = True
                    "{i}Вы помогли Кириллу{/i}"
                    "{i}Но могли бы не помогать{/i}"
                    $ renpy.notify("Кирилл это запомнит")
                    pass
                "Оставить хохла":
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
            s "Ебать"
            s "Какого хуя у тебя разьёбаный дом"
            show s ogo at left
            with move
            show k at right
            with move
            k "Нормальный{w}, ты даун просто"
            "{i}В углу комнаты, вы услышали шорох{/i}"
            "{i}Вы подошли посмотреть..{/i}"
            play music fight
            show m see
            with zoominout
            with pixellate
            m "Ах ты пидарас"
            m "Ты меня бросил"
            m "Я выебу вас обоих"
            k "Э{w}, а меня за что"
            "Fight"
            "Round 1"
            menu mfr1:
                "Кто был первым участником ХАЖАБЫ?"
                "Кирилл":
                    m "Нет, не правильно"
                    $ FigthPoints -= 1
                    pass
                "Борис":
                    m "Кто это?"
                    $ FigthPoints -= 2
                    pass
                "Денис":
                    m "Почти"
                    $ FigthPoints -= 1
                    pass
                "Саша":
                    m "Знаешь всё кроме меня пидар"
                    $ FigthPoints += 2
                    pass
                "Макс":
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
                    m "Правильно"
                    m "Но какой месяц"
                    menu datem:
                        "Месяц рождения"
                        "19 Января":
                            $ FigthPoints -= 1
                            pass
                        "19 Февраля":
                            $ FigthPoints += 2
                            m "Это все знают{w}, а год какой?"
                            menu yearm:
                                "В каком году"
                                "19 Февраля 2006г":
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
                                    m "Это информация была в боте"
                                    m "Во сколько я радился"
                                    menu hourm:
                                        "Во сколько я радился"
                                        "19 Февраля 2007г в 2:00":
                                            m "Вау, я поражён"
                                            m "Ты точно знаешь когда я родился"
                                            m "Честно даже я не знал об этом"
                                            $ FigthPoints += 2
                                        "19 Февраля 2007г в 4:00":
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "19 Февраля 2007г в 5:27":
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "19 Февраля 2007г в 6:00":
                                            m "Не правильно, а я уже поверил.."
                                            $ FigthPoints -= 1
                                            pass
                                        "Иди нахуй":
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
            k "Давай я тебе помогу"
            "Round 3"
            m "Когда была создана ХАЖАБА"
            if kHelp:
                k "Дай подумаю.."
                k "Ты мне помог, по этому я взломаю вселенную и найду ответ"
                k "Г жцмцп пну Хитцъ хфуесэ, цеш адт мнъимчнт ицу кыа ухнкъпбыч .. Денис"
                m "Не знаю почему{w}, но это правильный ответ"
                $ FigthPoints += 1
            else:
                k "Дай подумаю.."
                k "Я не знаю"
                m "Это не правильный ответ!"
            if FigthPoints >= 6:
                play audio "Intro.wav"
                stop music
                m "Вы ответили правильно на мои вопросы"
                hide m
                show m talk
                play music mansion
                m "Ладно простите что чуть не выебал вас"
                s "Ты аухел?"
                s "Чуть нас не выебал пидарас"
                hide k
                show d scream2 at right with vpunch
                d "Я спиздел у вас Кирилла"
                d "Если хотите его"
                d "Идите на кладбище"
            else:
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
    s "Нахуй мы за ним идём"
    s "Там Денис{w}, там опасно"
    m "Он мне шаурму должен"
    s "Достойная причина, тогда и мне"
    "{i}Так они трахались{w}, потом они пришли на кладбище{/i}"
    scene bg morg
    play music "music/Venus.wav"
    pause(3.5)
    show m talk
    with dissolve
    m "Он должен быть где-то здесь"
    hide m
    show m talk at right
    with move
    show s at left
    with move
    s "Предлагаю поискать"
    s "Я осмотрюсь здесь, ты иди дальше"
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
    s "Где я"
    s "Знакомая музыка"
    scene dbg shcool
    with fade
    show s
    s "Это же наша школа"
    s "Что я тут делаю"
    "{i}Саша посмотрел на часы{/i}"
    "8:14"
    s "Уроки только начались"
    s "Видимо то что произошло был всего лишь сон"
    s "Или я перебрал с мефедроном"
    s "В любом случае я опаздываю на урок{w}, хотя обычно это делает Макс"
    scene dbg shcool2
    "{i}Саша направился ближе ко входу{/i}"
    "Как вдруг он заметил Макса"
    show dm
    s "О еблан"
    s "Иди сюда"
    "{i}Макс не отреагировал на слова Саши{/i}"
    "{i}Он продолжил идти{/i}"
    hide dm
    s "Пидарас игнорит меня"
    "{i}Саша побежал за ним{/i}"
    scene black
    "{i}Саша зашёл в школу за ним{/i}"
    "К его удивлению он не пошёл в класс"
    "{i}Саша попытался дотронуться до Макса{/i}"
    "Но у него ни чего не получилось"
    "Рука прошла сквозь него к члену"
    "{i}Макс улыбнулся){/i}"
    s "Почему я не могу до него дотронутся"
    s "Может это всё сон?"
    s "И на самом деле сейчас я лежу от передоза"
    s "Ладно продолжу смотреть сон"
    scene dbg bonker
    with fade
    s "Стой"
    s "Что ты делаешь"
    s "Не призывай его"
    s "Он всю школу выебет"
    "{i}Макс проигнорировал его{/i}"
    m "حبًا بك في عالم اللغة العربيحبًا بك في عالم اللغة العربي"
    "Он призвал Дениса"
    show d aun
    play audio dk
    d "Нахуй ты меня призвал"
    d "В наказание я выебу тебя и всех кто тут есть"
    m "Стой"
    m "Я призвал тебя что бы ты помог"
    with fade
    "У Саши начало темнеть в глазах"
    with fade
    with fade
    with fade
    scene black
    stop music
    s "Видимо я начал просыпаться"
    play music "music/Venus.wav"
    scene bg morg
    with fade
    "{i}Саша очнулся{/i}"
    show s
    with dissolve
    s 'Я должен найти Кирилла'
    s "И узнать что произошло сегодня утром"
    s "Сначала осмотрюсь здесь"
    "Саша начал ходить по кладбищу"
    "{i}Он подошёл к одной могиле{/i}"
    scene mogb
    with fade
    s "Кого-то это напоминает"
    s "Но не помню кого"
    menu boris:
        "Fress F?"
        "F":
            "Саша выбрал отдать честь погибшему"
            "F"
            pass
        "Носань на могилу":
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
    s "Что ж, я ни чего не нашёл"
    s "Пойду к Максу"
    s "Узнаю что он нашёл"
    "{i}Саша пошёл в сторону склепа{/i}"
    scene black
    s "Интересно"
    s "Пятую минуту снаффа тут снимали?"
    scene bg scleb
    with fade
    pause(1)
    show m da
    with dissolve
    m "О здарова"
    m "Мне кажется они в этом гробу"
    show m da at right
    with moveinright
    "{i}Вы услышали тихие стоны{/i}"
    m "Эти пидары явно что-то там делают"
    s "Дай я послушаю"
    show s
    with dissolve
    "Саша послушал стоны"
    s "Ебать"
    s "Он Кирилла там трахает?"
    m "Хуй знает, может дрочит так"
    s "Давай откроем, посмотрим"
    show s at left
    with moveinleft
    "Вы подошли к гробу"
    menu:
        "Открыть крышку гроба?"
        "Открыть":
            "То что вы увидели"
            "Было ужасно"
            "Перед вами был расчленённый труп Кирилла"
            s "Что за хуйня"
            m "БДСМ с Денисом"
            s "Я вахуи"
            "Из гроба вы увидели луч света"
            "Как вдруг вас затянуло.."
            jump deadw
        "Сбежать":
            pass
    "Вы решили оставить их в покое"
    s "Слушай"
    s "Это их отношения или сношения"
    s "Пускай занимаются чем, хотят"
    m "Ладно, не будем мешать"
    m "Уходим"
    scene black
    with fade
    "Вы ушли из склеба"
    "Но на выходе{w}, был{w} он"
    scene bg morg
    with fade
    pause(1)
    show d scream2
    with dissolve
    d "Я вас выебу"
    s "Блять, беги!"
    with vpunch
    scene black
    stop music
    "{fi}Пролог пройден{/fi}"
    jump deadw
    return