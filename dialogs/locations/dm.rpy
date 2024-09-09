label dm:
    play music "audio/music/SleepTalking.wav"
    if not talk_3maxim and win_3dan and talk_2maxim:
        $ OneDiscordMessage("# Глава 1 ❤️\nСаша и Борис пришли к Максиму домой".format(persistent.user_name))
        call restoreos()
        scene black
        $ talk_3maxim = True
        voice s0175
        s "Борис как думаешь кто этот Максим?"
        voice b0003
        b "Не знаю{w}, я его ещё не видел"
        voice b0004
        b "Только слышал про него от Макса и Кирилла"
        voice s0176
        s "Макс что-то у него сегодня задержался"
        voice s0177
        s "Идём к ним"
        scene bg rdm with fade
        "Перед нами был заброшенный дом"
        "По среди путынного поля"
        show ps at left
        show pb at right with dissolve
        voice s0178
        s "Ебать"
        voice b0005
        b "Так он бомж походу"
        voice s0178b
        s "Зачем он выбрал жить здесь?"
        voice b0006
        b "Не знаю{w}, у всех свои вкусы"
        voice s0179
        s "Ладно заходим внутрь"
        scene bg rdm_vhod with fade
        "Внутри было пусто"
        "Здание уже давно начало разрушаться"
        "Сверху был слышен чей-то голос"
        "Вы решили подняться на верх"
        scene bg rdm_room with fade
        "Вы увидели чью-то фигуру"
        show pm talk with dissolve
        voice s0180
        s "Макс?"
        show ps at left with moveinleft
        show pb at right with moveinright
        voice b0007
        b "Почему ты здесь один?"
        $ OneDiscordMessage("# Глава 1 ❤️\nУ Макса шиза".format(persistent.user_name))
        voice m0349
        m "Что{w} я не один"
        voice m0350
        m "Со мной любимый"
        voice s0181
        s "О чём ты"
        voice b0008
        b "Здесь не кого нет"
        voice m0351
        m "Вы ебланы?"
        voice m0352
        m "Вот он перед вами"
        voice s0182
        s "Борис{w=1.8} он шизик"
        voice b0009
        b "Да"
        voice m0353
        m "Так нет, с вами что-то не так"
        voice m0354
        m "Максим скажи им что-то"
        pause(1.5)
        voice m0355
        m "Видите он настоящий"
        voice s0183
        s "Здесь только ты"
        voice b0010
        b "Саша{w} давай уходить от сюда"
        voice b0011
        b "Здесь слишком жутко"
        voice s0184
        s "Ладно уходим"
        voice m0356
        m "Пиздец вы ебанутые"
        hide pb with moveoutright
        hide ps with moveoutleft
        scene bg dm_room
        show pm talk
        show pl cool at left
        with fade
        voice m0357
        m "Что это было?"
        voice l0001
        l "Не знаю"
        voice l0002
        l "Оно нам не надо"
        voice m0358
        m "Ладно продолжим собирать ядерную установку"
        scene black with fade
    scene bg dm
    with fade
    menu dm_что_делать:
        "Любимый" if win_1les and not talk_1maxim or win_4dan and not talk_4maxim:
            if win_1les and not talk_1maxim:
                $ talk_1maxim = True
                call restoreos()
                show pm talk
                with dissolve
                voice m0359
                m "Что же"
                voice m0360
                m "Я пришёл в дом любимого"
                voice m0361
                m "Я знал что он тут есть"
                voice m0362
                m "Как же давно я его не видел"
                voice m0363
                m "Надеюсь он всё-таки сделал косплей гитлера как обещал"
                hide pm
                with dissolve
                "Макс подошёл ко входу"
                "Там стоял домофон"
                show pm talk
                with dissolve
                voice m0364
                m "Ебать, ну ахули"
                voice m0365
                m "Средневековье всё-таки"
                "Макс позвонил в него"
                "Кто-то взял трубку"
                "? ? ?" "Кто это?"
                voice m0366
                m "Любимый это ты?"
                voice m0367
                m "Открывай двери поговорим"
                "? ? ?" "Ооо{w}, дастиш фантастиш"
                "Любимый начал открывать двери"
                show pm talk at left
                with move
                $ OneDiscordMessage("# Глава 1 ❤️\nМакс встретился с любимым".format(persistent.user_name))
                $ persistent.remember_l = True
                show pl at right
                with dissolve
                voice l0003
                l "Цколько лет цколько цим"
                voice m0368
                m "Ебать"
                voice m0369
                m "Ты успел отрастить усы как у моего кумира{w}(Гитлера)?"
                voice l0004
                l "Да"
                voice l0005
                l "Пройдём ко мне в дом"
                voice l0006
                l "Мой третий рех построил его для меня"
                voice l0007
                l "Проблемы с газом{w}, так что там холодно"
                voice m0370
                m "Не чего страшного"
                voice m0371
                m "Я уже привык"
                voice m0372
                m "Мы с Сашей постоянно в лесу{w=1.4} в болоте{w=.5} пиздимся против мостров"
                voice l0008
                l "Страшно"
                scene black
                with fade
                "Вы прошли в дом"
                "По пути на вас лаял борис"
                scene bg dm_vhod
                with fade
                show pm talk at left
                show pl cool at right
                with dissolve
                voice l0009
                l "Здесь я живу"
                voice l0010
                l "Со мной ещё один пидарас жил"
                voice l0011
                l "Но его сейчас нет"
                voice l0012
                l "Так что всё хорошо"
                voice m0373
                m "Красиво у тебя тут"
                voice m0374
                m "Лучше, чем в баре Бориса"
                voice l0013
                l "Да ебать, я таких халуп как у него ещё не видел"
                voice l0014
                l "Он думает что мы в средневековье"
                voice l0015
                l "И всем об этом рассказывает"
                voice m0375
                m "Так, а что не так?"
                voice l0016
                l "Нет"
                voice l0017
                l "Мы просто в селе"
                voice l0018
                l "Для села это ещё и заебись, даже колледж есть"
                voice l0019
                l "Идём я тебе свою комнату покажу{w}, она на втором этаже"
                scene black
                with fade
                "Вы начали подниматься по лестнице"
                play sound упалначлен
                "Как вдруг{w} Макс споткнулся на резиновый член"
                "{i}Где-то это было{/i}"
                "Любимый схватил его за руку"
                voice l0020
                l "Я тебя не брошу"
                voice m0376
                m "Спасибо"
                scene bg dm_room
                with fade
                show pm talk at left
                show pl cool at right
                with dissolve
                voice m0377
                m "Это от кого такая привычка оставлять резиновые члене везде?"
                voice l0021
                l "Кирилл{w}, он постоянно раскидывает их по всему дому"
                voice l0022
                l "Правда его сейчас нет{w} и этим занимаюсь я"
                voice l0023
                l "Можешь взять один если хочешь"
                voice m0378
                m "Я возьму один"
                voice m0378b
                m "Опробую его"
                voice l0024
                l "Расскажешь потом как ощущения"
                "Вы взяли резиновый член"
                $ OneDiscordMessage("# Глава 1 ❤️\n{0} получил резиновый член Кирилла".format(persistent.user_name))
                $ renpy.notify("Проверьте свой инвентарь")
                $ player_inv.take(resinoviy_chlen)
                voice m0379
                m "Спасибо"
                voice l0025
                l "Ты не знаешь куда пропал Кирилл?"
                voice m0380
                m "Не знаю{w=1}, мы с ним виделись в темноте"
                voice m0381
                m "Когда в рай летели"
                voice m0382
                m "В итоге Денис и он пропали"
                voice l0026
                l "С вами был Денис{w} и что{w} рай?"
                voice m0383
                m "Да{w}, а у тебя не было встречи с богом?"
                voice l0027
                l "Неа{w}, я просто оказался здесь"
                voice m0384
                m "Странно у Бориса было это"
                voice l0028
                l "Так он шизик"
                voice l0029
                l "Говорит что он избранный и что-то длинное говорит"
                voice m0385
                m "Походу"
                voice l0030
                l "Может и ты?"
                voice m0386
                m "Та нет{w=1}, Саша тоже самое видел"
                voice l0031
                l "Допустим"
                voice l0032
                l "В любом случае то как мы здесь оказались это странно"
                voice m0387
                m "Может встретимся позже и обговорим это?"
                voice l0033
                l "Ты хочешь сказать{w}, ты{w}, приглашаешь{w} меня на свидание!?!?!"
                voice m0388
                m "Что-то вроде того"
                voice l0034
                l "Я только за Любимый"
                voice m0389
                m "Тогда встретимся на мосту в 18:00 через пару дней"
                show pl great
                voice l0035
                l "Договорились"
                voice l0036
                l "Буду ждать тебя там"
                voice m0390
                m "Пойду до Саши{w=1}, он наверное меня уже заждался"
                voice l0037
                l "Надеюсь это не измена"
                voice m0391
                m "Не переживай, если что у меня есть твой резиновый член"
                voice m0392
                m "Я пошёл"
                pass
            if win_4dan and not talk_4maxim:
                $ OneDiscordMessage("# Глава 1 ❤️\nКирилл вернулся домой после зелебобы".format(persistent.user_name))
                call restoreos()
                $ talk_4maxim = True
                show pm oshko at right with moveinright
                show pk sigma at left with moveinleft
                show pl with moveinbottom
                voice l0038
                l "С возращением"
                voice k0122
                k "Давно меня тут не было"
                voice l0039
                l "Куда пропадал?"
                voice m0393
                m "Его зелелоба в очко ебал"
                voice k0123
                k "Так{w=1} тихо"
                voice k0124
                k "Я был во вьетнаме"
                voice l0040
                l "Ого и как оно"
                voice k0125
                k "Та пиздец"
                voice m0394
                m "Хотел тебе расказать Кирилл"
                voice k0126
                k "Что"
                voice m0395
                m "Короче{w=1.2} Максима не существует"
                voice m0396
                m "Это твои воспоминания"
                if persistent.user_name == "Кирилл":
                    voice k0127b
                    k "Верю"
                else:
                    voice k0127
                    k "Верю"
                voice l0041
                l "Я тем более верю"
                voice m0397
                m "Ну вот спроси то Максим знает, хотя он не может этого знать"
                voice m0398
                m "Он знает всё что ты знаешь но не знает то что он знает"
                voice m0399
                m "Короче пиздец"
                voice k0128
                k "Допустим"
                voice k0129
                k "Кто выебал мою кошку?"
                voice l0042
                l "Я знаю это{w} ещё я знаю как это было и в какой позе"
                voice m0400
                m "Кирилл{w} нахуй ты это запомнил?"
                voice k0130
                k "Тебя ебать не должно"
                voice k0131
                k "Так и кто это"
                voice l0043
                l "Саша"
                voice k0132
                k "Так ведь реально ты не мог этого знать.."
                voice m0401
                m "Вот вот"
                voice m0402
                m "Он не реальный"
                voice l0044
                l "Не правда"
                voice m0403
                m "Правда{w} иди нахуй"
                voice l0045
                l "Ладно убидил"
                voice k0133
                k "В любом случае"
                if persistent.user_name == "Кирилл":
                    voice k0134b
                    k "Пока меня не было ты не трогал мою коллекцию резиновых членов?"
                else:
                    voice k0134
                    k "Пока меня не было ты не трогал мою коллекцию резиновых членов?"
                voice l0046
                l "Немного{w}, я их положил в ящик"
                voice l0047
                l "И один отдал Максу в использование"
                voice m0404
                m "Могу сказать он мне понравился"
                voice k0135
                k "Тогда я не против"
                voice l0048
                l "Что там с тем аутистом?"
                voice m0405
                m "Скоро мы его разьебём"
                voice k0136
                k "Да, наш \"Отряд\" скоро отправиться в его логово"
                voice m0406
                m "Мы уже освободили всех детей из его подалов"
                voice l0049
                l "Ого"
                voice l0050
                l "Это получаеться мы скоро сможем выбраться от сюда"
                voice k0137
                k "Ты нет"
                voice m0407
                m "Иди нахуй"
                voice m0408
                m "Любимый с нами"
                voice l0051
                l "Спасибо"
                if love_points >= 5:
                    voice l0052
                    l "Слушай Макс"
                    voice l0053
                    l "Может останемся здесь и у нас всё будет чипи чипи чапа чапа?"
                    menu chipi:
                        "Остаться с Любимым в этом мире"
                        "Чипи чипи чапа чапа":
                            $ OneDiscordMessage("# Глава 1 ❤️\nОстаться с Любимым в этом мире?\n> `Чипи чипи чапа чапа`".format(persistent.user_name))
                            voice l0054
                            l "Урааа"
                            voice m0409
                            m "Чипи чипи чапа чапа"
                            voice k0138
                            k "Руби руби даба даба"
                            scene bg
                            with fade
                            pause 1.5
                            $ ending("Чипи чипи чапа чапа")
                            "Теперь у вас всё чипи чипи чапа чапа"
                            # $ renpy.movie_cutscene('videos/chipi.mpg')
                            "[end_message]"
                            return
                        "Нет, надо отпиздить Дениса":
                            $ OneDiscordMessage("# Глава 1 ❤️\nОстаться с Любимым в этом мире?\n> `Нет, надо отпиздить Дениса`".format(persistent.user_name))
                            voice l0055
                            l "Ладно"
                            pass
                voice l0056
                l "Давай-те тогда"
                voice k0139
                k "Отправляемся в последний путь"
                voice m0410
                m "Идём пиздить Дениса!!!"
            pass
        "Уйти":
            scene black
            show screen map
            play music "music/Path to Lake Land.ogg"
            ''
            return
    scene black
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return
