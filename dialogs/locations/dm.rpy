label dm:
    play music "audio/music/SleepTalking.wav"
    if not talk_3maxim and win_3dan and talk_2maxim:
        $ OneDiscordMessage("# Глава 1 ❤️\nСаша и Борис пришли к Максиму домой".format(persistent.user_name))
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
        m "Что{w} я не один"
        m "Со мной любимый"
        voice s0181
        s "О чём ты"
        voice b0008
        b "Здесь не кого нет"
        m "Вы ебланы?"
        m "Вот он перед вами"
        voice s0182
        s "Борис{w=1.8} он шизик"
        voice b0009
        b "Да"
        m "Так нет, с вами что-то не так"
        m "Максим скажи им что-то"
        pause(1.5)
        m "Видите он настоящий"
        voice s0183
        s "Здесь только ты"
        voice b0010
        b "Саша{w} давай уходить от сюда"
        voice b0011
        b "Здесь слишком жутко"
        voice s0184
        s "Ладно уходим"
        m "Пиздец вы ебанутые"
        hide pb with moveoutright
        hide ps with moveoutleft
        scene bg dm_room
        show pm talk
        show pl cool at left
        with fade
        m "Что это было?"
        l "Не знаю"
        l "Оно нам не надо"
        m "Ладно продолжим собирать ядерную установку"
        scene black with fade
    scene bg dm
    with fade
    menu dm_что_делать:
        "Любимый" if win_1les and not talk_1maxim or win_4dan and not talk_4maxim:
            if win_1les and not talk_1maxim:
                $ talk_1maxim = True
                show pm talk
                with dissolve
                m "Что же"
                m "Я пришёл в дом любимого"
                m "Я знал что он тут есть"
                m "Как же давно я его не видел"
                m "Надеюсь он всё-таки сделал косплей гитлера как обещал"
                hide pm
                with dissolve
                "Макс подошёл ко входу"
                "Там стоял домофон"
                show pm talk
                with dissolve
                m "Ебать, ну ахули"
                m "Средневековье всё-таки"
                "Макс позвонил в него"
                "Кто-то взял трубку"
                "? ? ?" "Кто это?"
                m "Любимый это ты?"
                m "Открывай двери поговорим"
                "? ? ?" "Ооо{w}, дастиш фантастиш"
                "Любимый начал открывать двери"
                show pm talk at left
                with move
                $ OneDiscordMessage("# Глава 1 ❤️\nМакс встретился с любимым".format(persistent.user_name))
                $ persistent.remember_l = True
                show pl at right
                with dissolve
                l "Цколько лет цколько цим"
                m "Ебать"
                m "Ты успел отрастить усы как у моего кумира{w}(Гитлера)?"
                l "Да"
                l "Пройдём ко мне в дом"
                l "Мой третий рех построил его для меня"
                l "Проблемы с газом{w}, так что там холодно"
                m "Не чего страшного"
                m "Я уже привык"
                m "Мы с Сашей постоянно в лесу{w} в болоте{w} пиздимся против мостров"
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
                l "Здесь я живу"
                l "Со мной ещё один пидарас жил"
                l "Но его сейчас нет"
                l "Так что всё хорошо"
                m "Красиво у тебя тут"
                m "Лучше, чем в баре Бориса"
                l "Да ебать, я таких халуп как у него ещё не видел"
                l "Он думает что мы в средневековье"
                l "И всем об этом рассказывает"
                m "Так, а что не так?"
                l "Нет"
                l "Мы просто в селе"
                l "Для села это ещё и заебись, даже колледж есть"
                l "Идём я тебе свою комнату покажу{w}, она на втором этаже"
                scene black
                with fade
                "Вы начали подниматься по лестнице"
                "Как вдруг{w} Макс споткнулся на резиновый член"
                "{i}Где-то это было{/i}"
                "Любимый схватил его за руку"
                l "Я тебя не брошу"
                m "Спасибо"
                scene bg dm_room
                with fade
                show pm talk at left
                show pl cool at right
                with dissolve
                m "Это от кого такая привычка оставлять резиновые члене везде?"
                l "Кирилл{w}, он постоянно раскидывает их по всему дому"
                l "Правда его сейчас нет{w} и этим занимаюсь я"
                l "Можешь взять один если хочешь"
                m "Я возьму один"
                m "Опробую его"
                l "Расскажешь потом как ощущения"
                "Вы взяли резиновый член"
                $ OneDiscordMessage("# Глава 1 ❤️\n{0} получил резиновый член Кирилла".format(persistent.user_name))
                $ renpy.notify("Проверьте свой инвентарь")
                $ player_inv.take(resinoviy_chlen)
                m "Спасибо"
                l "Ты не знаешь куда пропал Кирилл?"
                m "Не знаю{w}, мы с ним виделись в темноте"
                m "Когда в рай летели"
                m "В итоге Денис и он пропали"
                l "С вами был Денис{w} и что{w} рай?"
                m "Да{w}, а у тебя не было встречи с богом?"
                l "Неа{w}, я просто оказался здесь"
                m "Странно у Бориса было это"
                l "Так он шизик"
                l "Говорит что он избранный и что-то длинное говорит"
                m "Походу"
                l "Может и ты?"
                m "Та нет{w}, Саша тоже самое видел"
                l "Допустим"
                l "В любом случае то как мы здесь оказались это странно"
                m "Может встретимся позже и обговорим это?"
                l "Ты хочешь сказать{w}, ты{w}, приглашаешь{w} меня на свидание!?!?!"
                m "Что-то вроде того"
                l "Я только за Любимый"
                m "Тогда встретимся на мосту в 18:00 через пару дней"
                show pl great
                l "Договорились"
                l "Буду ждать тебя там"
                m "Пойду до Саши{w}, он наверное меня уже заждался"
                l "Надеюсь это не измена"
                m "Не переживай, если что у меня есть твой резиновый член"
                m "Я пошёл"
                pass
            if win_4dan and not talk_4maxim:
                $ OneDiscordMessage("# Глава 1 ❤️\nКирилл вернулся домой после зелебобы".format(persistent.user_name))
                $ talk_4maxim = True
                show pm oshko at right with moveinright
                show pk sigma at left with moveinleft
                show pl with moveinbottom
                l "С возращением"
                k "Давно меня тут не было"
                l "Куда пропадал?"
                m "Его зелелоба в очко ебал"
                k "Так{w} тихо"
                k "Я был во вьетнаме"
                l "Ого и как оно"
                k "Та пиздец"
                m "Хотел тебе расказать Кирилл"
                k "Что"
                m "Короче{w} Максима не существует"
                m "Это твои воспоминания"
                k "Верю"
                l "Я тем более верю"
                m "Ну вот спроси то Максим знает, хотя он не может этого знать"
                m "Он знает всё что ты знаешь но не знает то что он знает"
                m "Короче пиздец"
                k "Допустим"
                k "Кто выебал мою кошку?"
                l "Я знаю это{w} ещё я знаю как это было и в какой позе"
                m "Кирилл{w} нахуй ты это запомнил?"
                k "Тебя ебать не должно"
                k "Так и кто это"
                l "Саша"
                k "Так ведь реально ты не мог этого знать.."
                m "Вот вот"
                m "Он не реальный"
                l "Не правда"
                m "Правда{w} иди нахуй"
                l "Ладно убидил"
                k "В любом случае"
                k "Пока меня не было ты не трогал мою коллекцию резиновых членов?"
                l "Немного{w}, я их положил в ящик"
                l "И один отдал Максу в использование"
                m "Могу сказать он мне понравился"
                k "Тогда я не против"
                l "Что там с тем аутистом?"
                m "Скоро мы его разьебём"
                k "Да, наш \"Отряд\" скоро отправиться в его логово"
                m "Мы уже освободили всех детей из его подалов"
                l "Ого"
                l "Это получаеться мы скоро сможем выбраться от сюда"
                k "Ты нет"
                m "Иди нахуй"
                m "Любимый с нами"
                l "Спасибо"
                if love_points >= 5:
                    l "Слушай Макс"
                    l "Может останемся здесь и у нас всё будет чипи чипи чапа чапа?"
                    menu chipi:
                        "Остаться с Любимым в этом мире"
                        "Чипи чипи чапа чапа":
                            $ OneDiscordMessage("# Глава 1 ❤️\nОстаться с Любимым в этом мире?\n> `Чипи чипи чапа чапа`".format(persistent.user_name))
                            l "Урааа"
                            m "Чипи чипи чапа чапа"
                            k "Руби руби даба даба"
                            scene bg
                            with fade
                            pause 1.5
                            $ ending("Чипи чипи чапа чапа")
                            "Теперь у вас всё чипи чипи чапа чапа"
                            $ renpy.movie_cutscene('videos/chipi.mpg')
                            "[end_message]"
                            return
                        "Нет, надо отпиздить Дениса":
                            $ OneDiscordMessage("# Глава 1 ❤️\nОстаться с Любимым в этом мире?\n> `Нет, надо отпиздить Дениса`".format(persistent.user_name))
                            l "Ладно"
                            pass
                l "Давай-те тогда"
                k "Отправляемся в последний путь"
                m "Идём пиздить Дениса!!!"
            pass
    scene black
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return
