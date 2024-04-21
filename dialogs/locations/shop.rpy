label shop:
    play music "audio/music/Woodland Fantasy.mp3"
    if not student:
        "Вы не можете войти"
        "Возможно вам надо сделать что-то другое"
        show screen map
        play music "music/Path to Lake Land.ogg"
        scene black
        ''
    if game_time > 18:
        if talk_1boris and action_1tank and not talk_2tank and win_3les:
            $ OneDiscordMessage("# Глава 1 🪙\nМакс и Саша пришли грабить Бориса ночью".format(persistent.user_name))
            $ talk_2tank = True
            scene bg shop
            with fade
            "Вы пришли ночью к Тянке"
            show tank
            with dissolve
            voice t0008
            t "Вы пришли"
            voice t0009
            t "Сейчас будем его грабить"
            voice t0010
            t "Он уже уснул крепким сном"
            voice t0011
            t "Так что может тут хоть до утра сидеть"
            voice s0317
            s "Погнали"
            scene black
            with fade   
            "Вы зашли в здание"
            "Свет работал, но не кого кроме вас не было"
            scene bg shop_bar
            with fade
            show tank
            with dissolve
            voice t0012
            t "Можем начать выносить деньги"
            hide tank
            with dissolve
            "Вы начали копаться в вещах Бориса"
            m "Я нашёл 200 грын у него в пиджаке"
            voice s0318
            s "Забирай всё{w=1.8} пиджак тоже"
            voice t0013
            t "Я заберу всю кассу"
            voice s0319
            s "Надо оставить следы{w=2.1}, что бы он подумал что это зелебоба его ограбил"
            voice t0014
            t "Да, у меня всегда есть мешок с болотом для этого"
            "Вы оставили следы в виде квадратов из грязи"
            voice t0015
            t "Он тупой не догадается"
            show ps at right
            show pm at left
            show tank 
            with dissolve
            voice s0320
            s "Сколько у нас по итогу получилось?"
            m "У меня 200 грын и пиджак"
            voice t0016
            t "Сегодня он что-то мало продал{w}, 500 грын"
            voice s0321
            s "Понятно у меня 300"
            m "Отсоси у меня"
            voice s0322
            s "Ночью уже"
            m "Договорились"
            m "Сегодня зайдёшь к Саньку?"
            m "Мы будем тебя ждать там"
            voice t0017
            t "Да конечно"
            voice t0018
            t "Спасибо что пришли"
            voice t0019
            t "А теперь сьёбывайте нахуй"
            $ player_inv.money += 1000
            scene black
            with fade
        "Уже слишком поздно"
        "Приходи в другое время"
        show screen map
        play music "music/Path to Lake Land.ogg"
        scene black
        ''
    if not first_barmen:
        $ first_barmen = True
        scene bg shop
        with fade
        show pm talk at left
        show ps smile at right
        with dissolve
        voice s0323
        s "Вот мы и пришли"
        voice s0324
        s "Мы пришли к этому мега гею"
        m "Щя мы его трахнем"
        voice s0325
        s "Интересно{w=1.5}, сколько он тут?"
        m "Не знаю{w}, я его уже давно не видел"
        m "Ходят шлюхи{w}, что у него были похороны"
        m "Он умер от какой-то болезни аутизм"
        voice s0326
        s "Да"
        voice s0327
        s "Я видел его могилу"
        m "И что ты сделал?"
        $ OneDiscordMessage("# Глава 1 🪙\nМакс и Саша познакомились с Борисом".format(persistent.user_name))
        $ persistent.remember_b = True
        if mogila_borisa:
            voice s0328
            s "Когда я увидел её"
            voice s0329
            s "Я не смог пройти мимо"
            m "И что ты сделал"
            voice s0330
            s "Обоссал его могилу"
            m "Лучший"
            show pb open
            with dissolve
            voice b0022
            b "Что ты сделал!?!?"
            voice b0023
            b "Как ты посмел осквернить мою могилу!"
            voice s0331
            s "Я крутой{w=2}, так что динах"
            m "Правильно он всё сделал"
            voice b0024
            b "Вам всё будет дороже!"
            voice b0025
            b "Вообще желательно не приходите"
        else:
            voice s0332
            s "Просто прошёл мимо.."
            m "а ведь ты мог.."
        show pb oshko
        voice b0026
        b "Ладно"
        voice b0027
        b "Проходите{w}, я вам всё покажу"
        m "Идём"
        scene bg shop_bar
        with fade
        show pb oshko
        with dissolve
        voice b0028
        b "Это мой магазин"
        voice b0029
        b "Не особо популярный"
        m "я конечно знаю что ты умер"
        m "Но знаешь ли ты об этом?"
        voice b0030
        b "Конечно{w}, как я могу не знать об этом"
        voice b0031
        b "Я видел иисуса"
        voice b0032
        b "Он мне показал всё что тут есть"
        voice b0033
        b "И дал {b}название{/b} моему приключению"
        voice b0034
        b "Бескрайний круг судеб Бориса: Реинкарнация торговца в мире, где каждый оборот в его жизни — новая сделка! Следите за захватывающим путем Бориса, чьи перерождения приводят его к таинственному магическому рынку, где он торгует не только товарами, но и своим собственным прошлым. От древних базаров до космических торговых постов, он исследует грани коммерческой реинкарнации, сталкиваясь с загадками, клиентами из разных измерений и разнообразием товаров от магических зелий до космических артефактов. В этом захватывающем аниме 'Борис: Реинкарнация Торговца', каждая сделка — это шаг к раскрытию его судьбы и великому богатству, ожидающему его в конце каждой жизни!"
        voice s0333
        s "Нахуй ты его выучил?"
        voice s0334
        s "Оно даже на экран не помещается"
        m "Реально"
        voice b0035
        b "Захотел"
        voice b0036
        b "Осмотритесь и подойдите ко мне"
        voice b0037
        b "Я покажу чем торгую"
        hide pb
        with dissolve
        "Борис пошёл нахуй"
        show pm talk at left
        show ps smile at right
        with dissolve
        voice s0335
        s "Видимо он уже давно тут"
        voice s0336
        s "И почему он видел иисуса?"
        m "Не знаю"
        m "Юй говорила что недавно, стала великим божеством"
        m "Может быть по этому"
        $ persistent.remember_t = True
        show tank
        with dissolve
        $ OneDiscordMessage("# Глава 1 🪙\nМакс и Саша познакомились с Тянкой".format(persistent.user_name))
        t "Здравствуйте"
        t "Я вас где-то видела"
        m "Саша это же она"
        voice s0337
        s "Да"
        t "Отец и отчим это вы?"
        m "Что ты наделал?"
        voice s0338
        s "Я её создал"
        voice s0339
        s "Не знаю как она сюда попала"
        t "Я тебя не видела больше года.."
        voice s0340
        s "Знаю{w=1.8}, я за хлебом уходил"
        m "Сигма"
        voice s0341
        s "Поговорим с тобой попозже"
        t "Хорошо alexmantos!"
        hide tank
        with dissolve
        m "Как она сюда попала?"
        m "Она же нереальна"
        voice s0342
        s "Я сам вахуи"
        voice s0343
        s "Позже позадаём ей вопросы"
        voice s0344
        s "Сейчас идём до Бориса"
    scene bg shop
    with fade
    if random_choise(5):
        if win_1les and OneEventCheck("Избиение Дениса Борисом") and not talk_1denis:
                show pd screem at left
                with dissolve
                "Подойдя к бару вы увидили Дениса"
                "Он стоял возле окна и смотрел в него"
                play sound door
                show pb open
                with hpunch
                voice b0119
                b "БЛЯТЬ{w=1.5} что ты тут делаешь"
                voice b0120
                b "Как стража вообще впустила в город"
                d "Я тебя убью!"
                "Борис начал избиать Дениса"
                scene black
                with fade
                "Позже он вернулся в бар"
                scene bg shop_bar
                with fade
                pass
    "Текст: Лавка Бориса"
    scene bg shop_bar
    with fade
    if not talk_2sasha and talk_3maxim:
        $ talk_2sasha = True
        show pk dshentelmen
        show ps smile at left with dissolve
        voice s0345
        s "Помнишь у тебя не кто не лайкал в давинчике?"
        k "Да потому что Борис далбоёб не смог сделать нормальную анкету"
        voice s0346
        s "Вообще-м"
        voice s0347
        s "Хочу тебя познакомить с Тянкой"
        k "Ого{w} и как её зовут?"
        voice s0348
        s "Тянка"
        k "ага"
        k "Допустим"
        voice s0349
        s "О вот и она"
        pause(2)
        k "И где она?"
        voice s0350
        s "Не перебивай её"
        voice s0351
        s "Стоп что?"
        k "Нихуя не понял"
        voice s0352
        s "Ты её не видишь?"
        k "Кого"
        voice s0353
        s "Тянку еблан"
        voice s0354
        s "Так ты помолчи пока"
        k "Ты о чём"
        k "Здесь не кого нету"
        $ OneDiscordMessage("# Глава 1 🪙\nСаша понял секрет мира".format(persistent.user_name))
        voice s0355
        s "Мне кажется я всё понял"
        voice s0356
        s "Кирилл нам надо выйти"
        scene bg shop
        with fade
        show pk
        show ps smile at left with dissolve
        voice s0357
        s "Что ты видишь перед собой"
        k "Магазин"
        voice s0358
        s "Какой именно"
        k "Обычный АТБ"
        voice s0359
        s "Так и знал"
        voice s0360
        s "Что в этом мире всё нереально"
        k "Это как"
        voice s0361
        s "Каждый видит его по своему"
        voice s0362
        s "Я вижу здесь магазин из скайрима"
        k "Ебать"
        k "Это как"
        voice s0363
        s "Хз"
        voice s0364
        s "Теперь я понял почему мы с Борисом не видели Максима"
        voice s0365
        s "Его для нас не существует"
        voice s0366
        s "Точно так же"
        k "Как и для меня Тянки"
        voice s0367
        s "Да"
        voice s0368
        s "Нам нужно выбраться от сюда"
        show pm oshko at right with dissolve
        m "Я подслушал ваш диалог"
        k "И как оно"
        m "Я больше не кому не доверяю"
        m "Каждый второй может быть не настоящим"
        voice s0369
        s "Нам нужно быть окуратнее"
        voice s0370
        s "Мы не знаем что они могут сделать"
        k "Предлагаю с такими больше не общаться"
        k "В плодь до нашего побега из этого места"
        voice s0371
        s "Договорились"
        m "Кстати"
        m "3 штурмова бригада нашла проход на последний уровень в подвале"
        k "Значит отправляемся туда"
        voice s0372
        s "Возможно там будет Денис"
        voice s0373
        s "Так что надо закупиться"
        show screen map
        play music "music/Path to Lake Land.ogg"
        scene black
        ''
    if random_choise(5):
        if win_3dan and OneEventCheck("ТБ"):
            "Подходя к бару вы увидели Бориса"
            "Он говорил с Тарасом"
            "Вы решили подслушать диалог"
            show pb at left
            show pz at right
            with dissolve
            b "Я вот подумываю заказать бригаду строителей"
            b "Что бы они переделали дверь под тебя"
            z "Уёбак, ты заебал"
            z "Если ты раньше это мог сделать"
            z "То какого хуя ты это не сделал"
            b "Не знаю"
            b "Постоянные клиенты всегда хорошо"
            z "А не чё что я у тебя не чего не покупал"
            b "Вот именно, по этому и хочу заказать бригаду"
            z "Бригада{w=1} ты даун просто"
            hide pb
            hide pz
            jump shop_bar
    if game_time < 12:
        $ OneDiscordMessage("# Глава 1 🪙\nСаша и Макс пришли утром в бар".format(persistent.user_name))
        show pb
        with dissolve
        voice b0038
        b "Ого"
        voice b0039
        b "Вы сегодня первые кто пришли в мой бар"
        m "Сегодня я не дрочил"
        hide pb
        with dissolve
    if not autohil and player_inv.money >= 3000 and random_choise(5):
        $ OneDiscordMessage("# Глава 1 🪙\nБорис предложил купить авто хилку".format(persistent.user_name))
        show pb
        with dissolve
        b "Я вижу что вы часто ко мне ходите лечиться"
        b "Хотити я вам продам пиво которое не портиться за пределами лавки?"
        menu infpivo:
            "Купить бесконечное пиво за 3 000 грывень"
            "Да(-3 000)":
                $ OneDiscordMessage("# Глава 1 🪙\n{0} купил авто хилку".format(persistent.user_name))
                $ player_inv.money -= 3000
                b "О отлично"
                b "Вы купили бесконечное пиво"
                b "Удачных вам боёв"
                $ autohil = True
            "Нет":
                b "Как хотите"
        hide pb
        with dissolve
    menu shop_bar:
        "Продавец":
            show pb open
            with dissolve
            voice b0040
            b "Что вы хотите купить?"
            menu shop23:
                "Оружие":
                    $ OneDiscordMessage("# Глава 1 🪙\n{0} ознакомился с арсеналом".format(persistent.user_name))
                    show screen shop_menu
                    'Нажми что бы продолжить'
                    jump shop23
                "Исцели меня бухлом":
                    $ OneDiscordMessage("# Глава 1 🪙\nПервое исцеление".format(persistent.user_name))
                    voice b0041
                    b "Знатно вас избили"
                    voice b0042
                    b "Ладно бухайте"
                    "Вы бухали 2 дня"
                    $ restorehp()
                    $ restoremp()
                    jump shop23
                "Поговорить":
                    if not barmen:
                        $ OneDiscordMessage("# Глава 1 🪙\nПервый разговор с Борисом".format(persistent.user_name))
                        voice b0043
                        b "Вы уже тут?"
                        voice s0372b
                        s "Да"
                        m "Показывай что у тебя тут есть"
                        voice b0044
                        b "Значит смотрите, я продаю оружие и бухло для них"
                        voice b0045
                        b "Большего в жизни не надо"
                        voice s0373b
                        s "Можешь дать что-то бесплатно для начала"
                        m "Да, нам надо уровень повысить, а денег 0"
                        voice b0046
                        b "Не чем не могу помочь"
                        voice b0047
                        b "Будут деньги приходите"
                        voice b0048
                        b "Здесь ещё есть Тарас"
                        voice b0049
                        b "Он часто тут появляется днём, часов где-то в 12"
                        voice b0050
                        b "Можете с ним попробовать поговорить"
                        $ barmen = True
                        jump shop23
                    if not talk_1boris and win_2les and talk_1tank:
                        $ OneDiscordMessage("# Глава 1 🪙\nСаша пришёл к Борису".format(persistent.user_name))
                        $ talk_1boris = True
                        show pb
                        with dissolve
                        voice b0051
                        b "Привет Саша"
                        voice b0052
                        b "Что хочешь?"
                        show pb
                        show ps at left
                        with dissolve
                        if action_1tank:
                            voice s0374
                            s "Это правда что зелебоба тебя грабит?"
                            voice b0053
                            b "Да"
                            voice b0054
                            b "Я вахуи"
                            voice b0055
                            b "Он каждые 3-4 дня приходит пока меня нету"
                            voice b0056
                            b "И ворует деньги"
                            voice b0057
                            b "Мне про это Тянка рассказывала"
                            voice s0375
                            s "Круто"
                        else:
                            voice s0376
                            s "Что с Тянкой?"
                            voice b0058
                            b "Она наказана"
                            voice b0059
                            b "Думаю оно ещё не скоро выйдет из комнаты"
                        voice b0060
                        b "а где Макс?"
                        voice b0061
                        b "Обычно ты с ним ходишь"
                        voice s0376b
                        s "Он до Максима пошёл"
                        voice s0377
                        s "Думаю он уже в колледже"
                        voice b0062
                        b "Могу рассказать как попасть в болото зелебобы"
                        voice s0378
                        s "Давай, рассказывай"
                        voice b0063
                        b "Вообще м"
                        voice b0064
                        b "Вам нужно пробраться в озеро среди леса"
                        voice b0065
                        b "Зачистить там монстров"
                        voice b0066
                        b "И дальше будет болото"
                        voice b0067
                        b "Вот там он и живёт"
                        $ OneDiscordMessage("# Глава 1 🪙\nСаша узнал как попасть к зелебобе".format(persistent.user_name))
                        voice s0379
                        s "Пойду с ним познакомлюсь"
                        voice s0380
                        s "Сделаю ZELEBOBA ADVENTURE REMASTERED"
                        voice b0068
                        b "Жду"
                        voice b0069
                        b "Но он довольно агрессивный"
                        voice b0070
                        b "Защищает своё болто"
                        voice b0071
                        b "Он переманил всех монстров в болоте на свою сторону{w}, после этого они и стали заходить в лес поля и нападать на нас"
                        voice s0381
                        s "Думаю справлюсь"
                        voice b0072
                        b "Покупайте снаряжение особенно броню"
                        voice b0073
                        b "Без неё вас будут убивать с одного удара"
                        voice s0382
                        s "Знаю{w=1.8}, я не даун"
                        voice b0074
                        b "Ладно"
                        voice s0383
                        s "Пойду до Макса"
                        voice s0384
                        s "Секса хочется"
                        hide ps
                        hide pb
                        with dissolve
                    if not talk_2boris and talk_2kirill:
                        $ OneDiscordMessage("# Глава 1 🪙\nКирилл пришёл к Борису".format(persistent.user_name))
                        $ talk_2boris = True
                        show pk auf at left
                        with moveoutleft
                        show pb at right
                        with moveoutright
                        k "Здорова{w}, я хотел узнать больше про бдсм лолей"
                        voice b0075
                        b "Фу{w} лоликонч"
                        k "Та блять нет"
                        k "Я про похищение то"
                        voice b0076
                        b "а"
                        k "Ты не знаешь куда он мог пропасть?"
                        voice b0077
                        b "Есть одно место"
                        voice b0078
                        b "Оно очень опасное"
                        voice b0079
                        b "Я не слышал что бы из него возвращались живыми"
                        voice b0080
                        b "Подземелье{w}, там обитали самые опасные существа"
                        voice b0081
                        b "С ними справлялись{w}, но после последних событий"
                        voice b0082
                        b "От туда не кто не возращялся"
                        $ OneDiscordMessage("# Глава 1 🪙\nКирилл узнал про БДСМ лолей".format(persistent.user_name))
                        k "Ты хочешь сказать что он может быть там?"
                        voice b0083
                        b "Да"
                        k "Что же{w}, схожу туда проверю"
                        voice b0084
                        b "Когда успел вернутся?"
                        k "Недавно"
                        k "Меня спас [name] от зелебобы"
                        k "Я был у него в клетке"
                        k "Он чуть не выебал меня"
                        voice b0085
                        b "Понял"
                        voice b0086
                        b "Не буду спрашивать как ты туда попал"
                        k "Пойду в подземелье"
                        hide pk with moveoutleft
                        hide pb with moveoutright
                        jump shop23
                    if not talk_3boris and win_2dan:
                        $ OneDiscordMessage("# Глава 1 🪙\nБорис отблагодарил отряд за победу над зелебобай".format(persistent.user_name))
                        $ talk_3boris = True
                        show pb with dissolve
                        voice b0087
                        b "Здравствуй Кирилл"
                        show pk dshentelmen at left with moveinleft
                        voice b0088
                        b "Я видел вы одолели зелебобу"
                        voice b0089
                        b "Деньги из моей кассы больше не пропадают"
                        voice b0090
                        b "Спасибо вам"
                        k "Мы смогли собрать всю команду"
                        k "Очень скоро мы сможем попасть в логово Дениса"
                        k "Ты бы хотел выбраться от сюда?"
                        voice b0091
                        b "Знаешь"
                        voice b0092
                        b "Как бы этот мир не был прекрасен"
                        voice b0093
                        b "Это всё же средневековье"
                        voice b0094
                        b "И мне здесь делать не чего"
                        voice b0095
                        b "Я бы хотел выбраться с вами"
                        k "Отлично"
                        k "Как тебе идея показать себя в боях?"
                        voice b0096
                        b "Не знаю{w}, я не пробовал себя в магии или чём-то таком"
                        k "Так что?"
                        voice b0097
                        b "Можем"
                        k "Тогда встретимся у Санька"
                        voice b0098
                        b "Договорились"
                        hide pk with moveoutleft
                        hide pb with moveoutright
                    if not talk_5boris and win_4dan:
                        $ OneDiscordMessage("# Глава 1 🪙\nПрощальный разговор с Борисом".format(persistent.user_name))
                        $ talk_5boris = True
                        show pm see at right with moveinright
                        show ps uwu at left with moveinleft
                        show pb with moveinbottom
                        voice s0385
                        s "Здарова Борис"
                        m "Мы скоро будем выбираться от сюда"
                        voice b0099
                        b "Ого{w}, меня возьмете?"
                        voice s0386
                        s "Вообще ты нам не чего не давал"
                        voice s0387
                        s "Так что мы подумаем"
                        voice b0100
                        b "Та ну"
                        voice b0101
                        b "Я же тут навсегда останусь"
                        m "Позже скажем"
                        voice b0102
                        b "Ладно"
                        voice b0103
                        b "Если меня здесь оставите я вас буду проклинать"
                        voice s0388
                        s "Почему у тебя не появляеться новое оружие"
                        voice s0389
                        s "Логичноже пополнять товар"
                        voice b0104
                        b "Да{w}, но больше нету материалов из которых можно сделать оружие"
                        voice s0390
                        s "Ладно"
                        voice b0105
                        b "У меня есть вопрос по поводу третей руки Макса"
                        m "А?"
                        m "Ты про эту"
                        voice b0106
                        b "Да{w} что это за хуйня"
                        m "Ну так это{w}, я зелёный{w}, а значит мутант"
                        voice s0391
                        s "И ведь не поспоришь"
                        voice b0107
                        b "Так а реально от куда?"
                        m "Я сам не ебу"
                        m "Она просто появилась когда я сюда попал"
                        m "Могу сказать что дрочить удобно"
                        voice s0392
                        s "Потверждаю"
                        voice b0108
                        b "Так у тебя нету третей руки"
                        voice s0393
                        s "А обязательно моя?"
                        voice b0109
                        b "Пиздец"
                        voice b0110
                        b "Идите нахуй пидарасы"
                        m ")))"
                        hide pm with moveoutright
                        hide ps with moveoutleft
                        hide px with moveoutbottom
                    random:
                        b "У меня самые выгодные цены!"
                        voice b0111
                        b "Два хуя!{w} И все у меня во рту"
                        voice b0112
                        b "Только я продаю нелегальное оружие!"
                        b "Меня ебали"
                        voice b0113
                        b "Хочешь подозрительные зелья?"
                        voice b0115
                        b "Меня ебут каждый день в очко"
                        voice b0114
                        b "Наркотики тоже продаю!"
                        b "Бухло есть!"
                        b "Я сосу члены"

                    jump shop23
                "Уйти":
                    voice b0116
                    b "Увидимся ещё"
                    hide pb
                    jump shop_bar
        "Тянка" if game_time >= 12 and barmen:
            if win_1les and not talk_1tank:
                $ OneDiscordMessage("# Глава 1 🪙\nСаша и Макс в первые говорят с Тянкой".format(persistent.user_name))
                $ talk_1tank = True
                show ps smile at left
                show pm at right
                with dissolve
                m "Ты готов поговорить со своим детищем"
                m "Ты его создал{w}, а оно сдохло"
                voice s0394
                s "Я вахуи как"
                voice s0395
                s "Но да"
                voice s0396
                s "У меня есть вопросы к ней"
                "Вы подошли к тянке"
                $ persistent.remember_t = True
                show tank
                with dissolve
                voice t0020
                t "Папа{w} и папа"
                voice t0021
                t "У меня два отца"
                m "Да{w}, мы тарахались"
                voice s0397
                s "Не важно"
                voice s0398
                s "Как ты здесь оказалась?"
                voice t0022
                t "Не знаю"
                voice t0023
                t "Я помню только как кого-то позвала к себе домой"
                voice t0024
                t "А он пошёл играть в майнкрафт с друзьями"
                voice t0025
                t "От такого я пошла и повесилась"
                voice s0399
                s "Насколько я помню это была лучшая концовка в моей игре"
                m "Да, я всегда на неё проходил"
                m "Концовка сигмы"
                voice s0400
                s "Там надо было переспать с тянкой и потом пойти играть в майн"
                voice t0026
                t "Вы о чём?"
                voice t0027
                t "Не с кем я не спала"
                voice t0028
                t "Пидарасы"
                voice s0401
                s "Да"
                voice s0402
                s "И после этого ты попала в этот мир? Видела бога юй или иисуса?"
                voice t0029
                t "Нет, я была в пустоте"
                voice t0030
                t "Целый год"
                voice t0031
                t "Я ждала{w} и в какой-то момент попала сюда"
                voice t0032
                t "Здесь я встретила Бориса"
                voice t0033
                t "Я иногда у него убираю{w} и он разрешает мне здесь жить"
                m "Понятно, он тебя использует"
                voice s0403
                s "100\%"
                voice t0034
                t "Неа, я его наёбываю"
                voice t0035
                t "Я уже давно пиздю у него Деньги"
                voice t0036
                t "Он думает что это зелебоба{w}, но это я"
                menu raskasat:
                    "Рассказать Борису?"
                    "Я сигма, сдать её":
                        $ OneDiscordMessage("# Глава 1 👇\nРассказать Борису про Тянку?\n> `Я сигма, сдать её`".format(persistent.user_name))
                        m "Знаешь{w}, я сигма"
                        m "Борис иди сюда"
                        voice s0404
                        s "Блять я же ещё не всё спросил"
                        $ renpy.notify("Это действие будет иметь последствия")
                        m "Та иди нахуй"
                        scene black
                        with fade
                        "К вам подошёл Борис"
                        "Макс рассказал всё как было"
                        voice b0117
                        b "Ах ты тварь!"
                        "Борис забрал Тянку и ушёл в свою комнату с ней"
                        voice t0037
                        t "АПУТИ!"
                        voice b0118
                        b "Не путю"
                        scene bg shop_bar
                        with fade
                        show ps smile at left
                        show pm at right
                        with dissolve
                        voice s0405
                        s "Пиздец, походу мы теперь её не увидим"
                        m "Зато мы сигмы"
                        m "Го ограбим Бориса?"
                        menu ograbit:
                            "Ограбить Бориса?"
                            "Го":
                                $ OneDiscordMessage("# Глава 1 👇\nОграбить Бориса?\n> `Го`".format(persistent.user_name))
                                voice s0406
                                s "Го{w=1.6}, пока он занят ограбим как можно больше"
                                m "Лучший"
                                hide pm
                                hide ps
                                with dissolve
                                "Вы подошли к кассе"
                                m "Берём 500 грывень"
                                voice s0407
                                s "Мало го 600 хотя бы"
                                voice s0408
                                s "Видимо кроме нас с тобой не кто не чего не покупает"
                                m "Да уж{w}, не очень у него тут бизнес"
                                "Вы украли 600 грывень"
                                $ player_inv.money += 600
                                "Вам больше нечего делать{w}, вы ушли"
                                jump shop_bar
                            "Ты еблан?":
                                $ OneDiscordMessage("# Глава 1 👇\nОграбить Бориса?\n> `Ты еблан?`".format(persistent.user_name))
                                voice s0409
                                s "Ты еблан?"
                                m "Да"
                                voice s0410
                                s "Ты конкурента устранил и теперь хочешь грабить его вместо неё"
                                voice s0411
                                s "Нет, мы не будем таким заниматься"
                                m "Ладно{w}, я просто предложил"
                                hide pm
                                hide ps
                                with dissolve
                                jump shop_bar
                    "Поддержать":
                        $ OneDiscordMessage("# Глава 1 👇\nРассказать Борису про Тянку?\n> `Поддержать`".format(persistent.user_name))
                        $ action_1tank = True
                        voice s0412
                        s "Харош"
                        m "Мы получается тоже можем пиздить деньги?"
                        voice s0413
                        s "Да, надо его грабить нахуй"
                        $ renpy.notify("Это действие будет иметь последствия")
                        voice t0038
                        t "Вы можете приходить ночью"
                        voice t0039
                        t "Когда он спит, он закрывает дверь на замок"
                        voice t0040
                        t "Я могу вам открывать{w}, но не всегда"
                        voice t0041
                        t "Так что приходите не сильно часто"
                        m "Ок"
                        voice s0414
                        s "Будем примерно раз в 4 дня приходить"
                        voice t0042
                        t "Жду вас"
                        voice s0415
                        s "У меня есть к тебе вопрос"
                        voice s0416
                        s "Какой магией ты обладаешь?"
                        voice t0043
                        t "Не знаю{w}, я слышала что тут есть магия и всякое такое"
                        voice t0044
                        t "Но мне это не сильно интересно"
                        voice t0045
                        t "Тем более в колледже слишком дорогое обучение"
                        m "Мы можем договориться что бы Санёк бесплатно тебя обучал"
                        voice t0046
                        t "Я же говорю не сильно хочу этим заниматься"
                        voice t0047
                        t "Тем более если кто-то узнает что у меня есть боевые способности"
                        voice t0048
                        t "Меня отправят в Бахмут"
                        m "Мне похуй"
                        m "Ты идёшь в колледж"
                        voice t0049
                        t "Динахуй{w}, не хочу"
                        voice s0417
                        s "Та давай"
                        voice s0418
                        s "Один раз сходишь"
                        voice s0419
                        s "Просто посмотришь что у тебя за магия"
                        voice t0050
                        t "Ну ладно"
                        voice t0051
                        t "Если один раз"
                        voice t0052
                        t "То можно"
                        voice t0053
                        t "Только позже, ладно?"
                        voice s0420
                        s "Хорошо, ждём"
                        voice t0054
                        t "Я пойду убирать{w}, а то он меня выселит"
                        hide tank
                        with dissolve
                        voice s0421
                        s "Что же, сегодня ночью зайдём"
                        m "Канечна{w}, да"
                        m "Будем грабить его"
                        "Вам больше нечего делать{w}, вы ушли"
                        hide pm
                        hide ps
                        with dissolve
                        jump shop_bar
            if not talk_3tank and win_4dan:
                $ OneDiscordMessage("# Глава 1 👇\nПоследний разговор с Тянкой перед штурмом".format(persistent.user_name))
                $ talk_3tank = True
                show pm oshko at right with moveinright
                show ps smile at left with moveinleft
                show tank with moveinbottom
                voice t0055
                t "Саша, зачем ты тогда ушёл и не вернулся"
                m "Ты за хлебом ходил?"
                voice s0422
                s "Нет"
                voice s0423
                s "Вообще-м мы так подумали"
                voice s0424
                s "Ты не реальна{w=2} как и всё остальное"
                m "Ого и как ты это понял?"
                voice t0056
                t "Как я могу быть не реальной"
                voice t0057
                t "Вот я перед тобой"
                voice s0425
                s "Да{w=1.6}, но это только для тех кто знал про тебя до смерти"
                m "Ты думаешь это так?"
                voice s0426
                s "Я в этом уверен"
                voice s0427
                s "Максима я не видел при жизни{w=2.6}, а значит и здесь его для меня нету"
                voice s0428
                s "Они существуют и в реальности ещё живые"
                voice s0429
                s "А мы умерли"
                voice t0058
                t "Ладно"
                voice t0059
                t "Но почему я чуствую себя живой тогда?"
                voice s0430
                s "Потому что я создал тебя живой"
                voice s0431
                s "Со своей историей и т.д."
                m "Это хорошая теория"
                m "Но тогда как мы можем верить в то что ты Санёк, Борис настоящие"
                voice s0432
                s "Не знаю"
                voice s0433
                s "В любом случае это информация нам даёт только то что мы не все сможем выбраться"
                voice t0060
                t "Ты хочешь сказать я не смогу вернуться домой?"
                voice s0433b
                s "Не то что бы так"
                voice s0434
                s "Это и есть твой дом"
                m "Как я понял ты появилась здесь из чьих-то воспоминаний"
                voice t0061
                t "Грустно"
                voice t0062
                t "Но я вам не верю!"
                voice t0063
                t "Так что я смогу выбраться от сюда и буду сражаться до конца"
                voice s0435
                s "Ну пробуй"
                voice s0436
                s "Не думаю что у тебя получиться"
                voice t0064
                t "Вот и буду пробывать!"
                hide tank with moveoutbottom
                m "Может ты зря с ней так?"
                voice s0437
                s "Забей"
                hide pm with moveoutright
                hide ps with moveoutleft
            "Ещё рано"
            jump shop_bar
        "Тарас" if game_time == 12 and barmen:
            if not talk_1taras:
                $ talk_1taras = True
                show pm talk at left
                show ps uwu at right
                show pt
                with dissolve
                $ persistent.remember_z = True
                voice z0002
                z "О"
                voice z0003
                z "Привет"
                voice z0004
                z "Я знаю всё"
                voice z0005
                z "Если вам нужна помощь обращайтесь!"
                voice z0006
                z "Я подскажу что вам надо сделать сейчас"
                voice z0007
                z "Меня заперли в этом здании строители"
                voice z0008
                z "Дверь слишком мала"
                voice s0438
                s "Ты не можешь нагнутся?"
                voice z0009
                z "Я не могу нагнутся{w}, разрабы дауны"
                m "По ф{w}a{w}к{w}т{w}у"
                voice z0010
                z "Сейчас я вам подскажу что можно сделать!"
                voice s0439
                s "Рассказывай"
            if party_list.count == 0:
                voice z0053
                z "Ебать [name] лох, один в отряде остался"
            
            if not first_pola:
                show pt
                with dissolve
                voice z0011
                z "Вы должны пойти в 24 часа в поле и встретить там Санька"
                hide pt
                with dissolve
                jump shop_bar
            if not first_libriary:
                show pt
                with dissolve
                voice z0012
                z "Вы должны пойти в библиотеку и встретить там Санька"
                hide pt
                with dissolve
                jump shop_bar
            if not win_1les:
                show pt
                with dissolve
                voice z0013
                z "Идите в лес в первый бой"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1tank:
                show pt
                with dissolve
                voice z0014
                z "Поговорите с Тянкой"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1sanek:
                show pt
                with dissolve
                voice z0015
                z "Пойдите в библиотеку к Саньку"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1maxim:
                show pt
                with dissolve
                voice z0016
                z "Макс{w}, ты можешь пойти домой к Максиму"
                hide pt
                with dissolve
                jump shop_bar
            if not win_2les:
                show pt
                with dissolve
                voice z0017
                z "Пройдите чащю леса что бы открыть новые действия"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2sanek:
                show pt
                with dissolve
                voice z0018
                z "Идите в библиотеку и поговорите с Саньком"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2maxim:
                show pt
                with dissolve
                voice z0019
                z "Поговори с Любимым на мосту"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1boris:
                show pt
                with dissolve
                voice z0020
                z "Поговори с Борисом в магазине"
                hide pt
                with dissolve
                jump shop_bar
            if not win_3les:
                show pt
                with dissolve
                voice z0021
                z "Продалжай сражаться"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3sanek:
                show pt
                with dissolve
                voice z0022
                z "Поговори с Саньком в поле"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2tank and action_1tank:
                show pt
                with dissolve
                voice z0023
                z "Прийди ночью в магазин Бориса"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1denis:
                show pt
                with dissolve
                voice z0024
                z "Продолжай пиздить Дениса пока он спит"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3tank and action_1tank:
                show pt
                with dissolve
                voice z0025
                z "Поговори с тянкой в колледже"
                hide pt
                with dissolve
                jump shop_bar
            if not win_4les:
                show pt
                with dissolve
                voice z0026
                z "Одолей зелебобу"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1kirill:
                show pt
                with dissolve
                voice z0027
                z "Поговори с Кириллом в колледже"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2kirill:
                show pt
                with dissolve
                voice z0028
                z "Поговори с Кириллом в колледже в комнате"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2boris:
                show pt
                with dissolve
                voice z0029
                z "Поговори с Борисом"
                hide pt
                with dissolve
                jump shop_bar
            if not win_1dan:
                show pt
                with dissolve
                voice z0030
                z "Зачисти подвал Арнаутова"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_4sanek:
                show pt
                with dissolve
                voice z0031
                z "Поговори с Саньком в колледже"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_1sasha:
                show pt
                with dissolve
                voice z0032
                z "Иди в свою комнату{w} там будет собрание"
                hide pt
                with dissolve
                jump shop_bar
            if not win_2dan:
                show pt
                with dissolve
                voice z0033
                z "Продолжай сражаться!"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_5sanek:
                show pt
                with dissolve
                voice z0034
                z "Поговори с Саньком"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3boris:
                show pt
                with dissolve
                voice z0035
                z "Поговори с Борисом"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3kirill:
                show pt
                with dissolve
                voice z0036
                z "Иди ночью в комнату{w} там общий сбор"
                hide pt
                with dissolve
                jump shop_bar
            if not win_3dan:
                show pt
                with dissolve
                voice z0037
                z "Продолжай сражаться!"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_4boris:
                show pt
                with dissolve
                voice z0038
                z "Поговори с Борисом"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3maxim:
                show pt
                with dissolve
                voice z0039
                z "Отправляйся к Любимому"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2sasha:
                show pt
                with dissolve
                voice z0040
                z "Встеться с Тянкой"
                hide pt
                with dissolve
                jump shop_bar
            if not win_4dan:
                show pt
                with dissolve
                voice z0041
                z "Что ты тут делаешь"
                voice z0042
                z "Третия штурмова бригада открыла новые подземелье!"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_2taras:
                $ talk_2taras = True
                show pt
                with dissolve
                voice z0043
                z "Поздравляю вас с зачисткой всех подвалов!"
                voice z0044
                z "Я вижу будующие.."
                voice z0045
                z "У вас всё получиться!"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_4maxim:
                show pt
                with dissolve
                voice z0046
                z "Иди к Любимому"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3tank:
                show pt
                with dissolve
                voice z0047
                z "Поговори с Тянкой"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_6sanek:
                show pt
                with dissolve
                voice z0048
                z "Ты должен прийти к Саньком"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_5boris:
                show pt
                with dissolve
                voice z0049
                z "Поговори с Борисом"
                hide pt
                with dissolve
                jump shop_bar
            if not talk_3sasha:
                show pt
                with dissolve
                voice z0050
                z "Общий сбор!"
                hide pt
                with dissolve
                jump shop_bar
            if not win_denis:
                show pt
                with dissolve
                voice z0051
                z "Иди блять пизди Дениса!"
                hide pt
                with dissolve
                jump shop_bar
            show pt
            with dissolve
            voice z0052
            z "Иди нахуй заебал, пидарас доделай игру. Сука блять уже месяц делаешь эту хуйню всё равно не кто не увидит так как это блять не возможно не как, только во время разработки этой хуйни пиздец макс даун спамер ебаный"
            hide pt
            with dissolve
            jump shop_bar
        "Уйти":
            show screen map
            play music "music/Path to Lake Land.ogg"
            scene black
            ''
    show screen map
    play music "music/Path to Lake Land.ogg"
    play music "music/Path to Lake Land.ogg"
    scene black
    ''
