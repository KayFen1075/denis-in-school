label ds:
    play music "music/nature sketch.wav"
    if not student:
        $ OneDiscordMessage("# Глава 1 🏫\n{0} в первый раз пришёл в колледж".format(persistent.user_name))
        scene black
        "Вы начали подходить к колледжу"
        "Возле входа была надпись"
        scene bg koledsh
        with fade    
        "Текст: {i}Колледж имени Санька Холодия{/i}"
        show pm talk at left
        show ps smile at right
        with dissolve
        voice s0185
        s "Нас некуда не впускают"
        voice s0186
        s "Наверное нам надо пойти сюда"
        voice m0169
        m "Тебе не кажется это имя знакомое?"
        voice s0187
        s "Я помню только Санька Ткаченка"
        voice s0188
        s "Не знаю кто это"
        voice m0170
        m "Ладно, я уже подумал что это он"
        voice m0171
        m "Тогда идём внутрь"
        scene bg koledsh_step
        with fade
        "Вы зашли внутрь"
        show pm talk at left
        show ps at right
        with dissolve
        voice m0172
        m "Странные эти аниме миры"
        voice m0173
        m "Вроде и средневековье{w=1.2}, а здания из современности"
        voice s0189
        s "Строители гигачаты просто"
        "Пока мы это обсуждали"
        "Перед нами появился"
        show px see
        with Dissolve(2)
        $ persistent.remember_x = True
        voice x0292
        "? ? ?" "Вы кто такие"
        voice x0001
        "? ? ?" "Я здесь вас вижу впервые"
        "Мы не могли разглядеть его лицо"
        $ OneDiscordMessage("# Глава 1 🏫\n{0} познакомился с Саньком".format(persistent.user_name))
        show px
        voice x0002
        x "Подождите"
        voice x0003
        x "Я вас узнаю"
        voice x0004
        x "Вы тоже сюда попали?"
        voice s0190
        s "Да{w=1.5}, ты тоже умер?"
        voice x0005
        x "Я знаю"
        voice x0006
        x "Я просто в один момент появился здесь"
        voice x0007
        x "а вы как умерли?"
        voice m0174
        m "Нас Денис выебал{w=1.2}, с нами ещё был Кирилл"
        voice m0175
        m "Но мы не знаем где он"
        voice m0176
        m "Мы перед вратами в рай его слышали"
        voice m0177
        m "Но на месте его не было"
        voice x0008
        x "Странно"
        voice x0009
        x "Ну ладно"
        voice s0191
        s "Как ты перед нами появился?"
        voice s0192
        s "За секунду"
        voice x0010
        x "А"
        voice x0011
        x "Вы же ещё не знаете"
        voice x0012
        x "В этом мире есть магия"
        voice x0013
        x "Если прокачивать свою ману{w},\n то вы сможете использовать магию"
        voice x0014
        x "Пока я не думаю что вы можете использовать хотя бы слабое заклинание"
        voice m0178
        m "Ну да логично"
        voice m0179
        m "Нам божество об этом не рассказало"
        voice x0015
        x "Какое божество?"
        voice s0193
        s "Когда мы сюда попали"
        voice s0194
        s "Нам Бог Юй объяснила как смотреть карту и время"
        voice m0180
        m "Гайд для аутистов короче"
        voice x0016
        x "Не знаю что за карта и время"
        voice x0017
        x "У меня для этого есть солнечные часы"
        voice x0018
        x "Заклинание такое"
        voice x0019
        x "Показывает часы"
        voice m0181
        m "Ты сможешь нас обучить магии?"
        voice x0020
        x "Да конечно"
        voice x0021
        x "Но сначала"
        voice x0022
        x "Как и в любом исекае"
        voice x0023
        x "Надо узнать ваш уровень магии"
        voice x0024
        x "Мб вы как в любом исекае будите имбой"
        voice s0195
        s "Хорошо давай"
        voice s0196
        s "Проверяй"
        voice x0025
        x "Идёмте за мной"
        show bg koledsh_class
        with fade
        show px
        voice x0026
        x "Это наша библиотека"
        voice x0027
        x "Здесь ученики изучают магию и как её использовать"
        voice x0028
        x "Иногда я буду с вами заниматься здесь"
        voice x0029
        x "Подойдите к этому шару"
        voice x0030
        x "Он покажет вашу мощь{w} и заклинания которые вы изучили"
        voice m0182
        m "Давай я первый"
        "Магический шар" "..."
        "Магический шар" "у вас{w} {b}1 уровень{/b}"
        voice s0197
        s "лох"
        if name == "Макс":
            "Магический шар" "Я вижу{w} у вас есть заклинание"
            "Магический шар" "Уникальное заклинание Макса"
            voice x0031
            x "Ого в первые такое вижу"
            voice x0032
            x "За все эти года я не разу не видел уникальных заклинаний"
            "Магический шар" "Оно может лечить выбранного персонажа"
            "Магический шар" "Его мощь будет расти по мере повышения уровня"
        else:
            "Магический шар" "Я вижу{w} у вас нет заклинаний"
            voice x0033
            x "Слабенько"
        voice s0198
        s "Давай теперь я"
        voice s0199
        s "Я уверен у меня круче"
        "Саша подошёл к магическому шару"
        "Магический шар" "..."
        "Магический шар" "у вас{w} {b}1 уровень{/b}"
        if name == "Саша":
            "Магический шар" "Я вижу{w} у вас есть заклинание"
            "Магический шар" "Уникальное заклинание Саши"
            voice x0034
            x "Ого в первые такое вижу"
            voice x0035
            x "За все эти года я не разу не видел уникальных заклинаний"
            "Магический шар" "Оно может делать двойную атаку"
            "Магический шар" "Его мощь будет зависеть от твоего урона"
        else:
            "Магический шар" "Я вижу{w} у вас нет заклинаний"
            voice m0183
            m "Лох ебаный"
            voice x0036
            x "Слабенько"
        voice x0037
        x "Я конечно в первые вижу уникальные заклинания"
        voice x0038
        x "Ещё и с улучшением по мере уровня.."
        voice x0039
        x "Что ж у вас по первому уровню"
        voice x0040
        x "Я помогу вам изучить новые заклинания"
        voice x0041
        x "И увеличить запас маны"
        voice s0200
        s "Как мы это будем делать?"
        voice m0184
        m "Да и как поднять уровень"
        voice x0042
        x "Это очень трудно{w}, вам надо будет сражаться с монстрами"
        voice x0043
        x "За их убийство вы будите получать xp"
        voice x0044
        x "После вы повысите уровень"
        voice m0185
        m "Ману как повысить"
        voice x0045
        x "Для этого вам надо будет тренироваться со мной"
        voice x0046
        x "Я сам буду говорить когда и как мы будем тренироваться"
        voice x0047
        x "Можем провести первый урок ночью"
        voice x0048
        x "Перед этим познакомьтесь со всеми"
        voice s0201
        s "Хорошо"
        voice m0186
        m "Где мы будем жить?"
        voice x0049
        x "мм"
        voice x0050
        x "У нас есть одна свободная комната{w}, за мной"
        scene bg koledsh_step
        with fade
        scene bg koledsh_room
        with fade
        voice x0051
        x "Это будет ваша комната"
        voice x0052
        x "Так как у нас больше нет комнат"
        voice x0053
        x "То вы будите спать вдвоём на это тесной кровати"
        voice m0187
        m "Я только за"
        voice x0054
        x "Могу принести матрас, кто-то будет спать на полу"
        menu matras:
            "Приносить матрас"
            "Да принеси":
                $ OneDiscordMessage("# Глава 1 👇\nПриносить матрас?\n> `Да принеси`".format(persistent.user_name))
                $ matras = True
                voice x0055
                x "Хорошо, сейчас"
                with fade
            "Нет, мы так будем спать":
                $ OneDiscordMessage("# Глава 1 👇\nПриносить матрас?\n> `Нет, мы так будем спать`".format(persistent.user_name))
                voice x0056
                x "Хорошо, ваше решение"
        voice x0057
        x "Что же, не буду вам мешать, увидимся ночью"
        "Санёк вышел из комнаты"
        pause(1)
        voice s0202
        s "Что же, теперь мы будем жить тут"
        voice m0188
        m "Да"
        voice m0189
        m "Прикольно тут"
        voice s0203
        s "Надо зайти в ларёк{w=1.9}, посмотреть что там"
        voice m0190
        m "Идём"
        $ student = True
        menu sadf:
            "Уйти":
                pass
    scene bg koledsh
    with fade
    "Текст: {i}Колледж имени Санька Холодия{/i}"
    scene bg koledsh_step
    with fade
    if random_choise(5):
        if win_1les and OneEventCheck("Санёк избевает Дениса"):
            $ OneDiscordMessage("# Глава 1 🏫\n{0} уведил как Санёк избевает Дениса".format(persistent.user_name))
            show pd scream2
            with dissolve
            call horror_effect
            voice d0090
            d "Сейчас я смогу украсть книги"
            voice d0091
            d "Читать я не умею"
            voice d0092
            d "Но они определенно сделают меня сильнее"
            show px at left
            with moveinleft
            voice x0058
            x "Ах ты тварь"
            voice x0059
            x "Подошёл к моему колледжу"
            scene black
            with fade
        if win_2les and OneEventCheck("Один учитель"):
            "Подойдя к Колледжу вы увидели Санька"
            "Вы решили подойти к нему и поговорить"
            show pm oshko at right
            show ps smile at left
            with dissolve
            voice m0191
            m "Здарова Санёк"
            s "Что делаешь?"
            show px
            with dissolve
            voice x0060
            x "Здарова, я тут убираюсь"
            voice x0061
            x "Всё таки я тут один работаю"
            voice m0192
            m "Подожди, я думал у тебя есть учителя или что-то типо того"
            voice x0062
            x "Неа, я открыл колледж сам"
            voice x0063
            x "Да и людей у нас в селе не много"
            voice m0193
            m "Мы сейчас закупили новое оружие"
            voice m0194
            m "Теперь мы в 2 раза сильнее"
            voice x0064
            x "Круто{w=1.8}, а я без экипировки"
            voice x0065
            x "Полагаюсь только на магию"
            s "Понятно{w=1.7} мы пошли тогда"
            hide pm
            hide ps
            hide px
            with dissolve
            jump kudaidti
        if win_2dan and OneEventCheck("Помощь в библиотеке"):
            "Подойдя к Колледжу вы увидели Санька"
            "Он что-то делал в библиотеке"
            show pm oshko at right
            show pk stoika at left
            with dissolve
            voice k0140
            k "Здарова Санёк"
            voice m0195
            m "Что делаешь?"
            show px
            with dissolve
            voice x0066
            x "Занимаюсь книгами"
            voice x0067
            x "Кирилл твои свитки довольно интересны"
            voice x0068 
            x "Не когда не мог подумать что свитки могут быть связаны с деньгами"
            voice k0141
            k "Евери ебаные"
            voice m0195b
            m "Я вот задумался{w=1.8} куда пропадают эти деньги после изучения магии"
            voice k0142
            k "Не знаю, не знаю"
            hide pm
            hide ps
            hide px
            with dissolve
            jump kudaidti
    if game_time > 18 and random_choise(3):
        $ OneDiscordMessage("# Глава 1 🏫\n{0} пришёл ночью в колледж".format(persistent.user_name))
        show px
        with dissolve
        voice x0226
        x "Нельзя опаздывать в наш колледж"
        voice x0227
        x "У нас строгие правила"
        voice x0228
        x "Но вам я прощаю"
        voice s0203b
        s "Хорошо больше не будем опаздывать"
        hide px
        with dissolve
    menu kudaidti:
        "Библиотека":
            scene bg koledsh_class
            with fade
            menu asdghd:
                "Борис" if win_3dan and talk_3boris and not talk_4boris:
                    if win_3dan and talk_3boris and not talk_4boris:
                        $ OneDiscordMessage("# Глава 1 🏫\nБорис пришёл в колледж".format(persistent.user_name))
                        call restoreos()
                        $ talk_4boris = True
                        show px with dissolve
                        show pk dshentelmen at right with moveinright
                        voice x0069
                        x "Кого ты привёл?"
                        show pb at left with moveinleft
                        voice k0143
                        k "Бориса"
                        voice k0144
                        k "Нужно узнать его уровень"
                        voice k0145
                        k "И на что он вообще способен"
                        voice x0070
                        x "Борис, что ты так захотел узнать{w}, когда уже тут несколько лет здесь?"
                        voice b0012
                        b "Просто стало интересно"
                        voice x0071
                        x "Ладно"
                        voice x0072
                        x "Положи свою руку на этот магический шар"
                        "Борис положил руку на россию"
                        "Магический шар" "Я вижу{w}...{w} у тебя 1 уровень"
                        "Магический шар" "Магии никакой нет"
                        "Магический шар" "Так же маны тоже.."
                        voice x0073
                        x "В первые такое вижу"
                        voice k0146
                        k "Ты Аста?"
                        voice b0013
                        b "Нет"
                        voice b0014
                        b "Ну бывает"
                        voice b0015
                        b "Я всё равно торговец"
                        voice b0016
                        b "Мне оно и ненужно"
                        voice k0147
                        k "Но ты сходишь с нами в бой"
                        voice b0017
                        b "Я не хочу в бахмут"
                        voice k0148
                        k "Мы и так в бахмуте"
                        voice k0149
                        k "Это наш город"
                        voice b0018
                        b "Ладно"
                        voice b0019
                        b "Схожу с вами"
                        voice x0074
                        x "Я заметил что вы превзошли учителя"
                        voice x0075
                        x "Ваш уровень уже давно выше моего"
                        voice x0076
                        x "Сила тоже"
                        voice x0077
                        x "Приходите все вместе ко мне в конце месяца"
                        voice x0078
                        x "Проведём выпускной"
                        voice k0150
                        k "Это получается мы закончим среднее образование?"
                        voice b0020
                        b "Да{w}, вы да{w}"
                        voice x0079
                        x "Увидимся"
                        hide px with moveoutbottom
                        voice b0021
                        b "Что же{w} пойду дальше продавать нелегальное оружие"
                        hide pb with moveoutleft
                        voice k0151
                        k "Пойду расскажу про всё это Саше и Максу"
                        hide pk with moveoutright
                        $ OneDiscordMessage("# Глава 1 🏫\nБорис вступил в отряд".format(persistent.user_name))
                        $ party_list.append(boris)
                "Кирилл" if win_4les or not talk_2kirill and talk_1kirill:
                    if not talk_1kirill and win_4les:
                        $ OneDiscordMessage("# Глава 1 🏫\nКирилл вернулся в колледж".format(persistent.user_name))
                        $ talk_1kirill = True
                        call restoreos()
                        show pk
                        with dissolve
                        voice k0152
                        k "Вот я и пришёл"
                        voice k0153
                        k "Надеюсь мне не зря ебали жопу"
                        voice k0154
                        k "И эти свитки что-то значат"
                        show pk sigma at left
                        with move
                        show px
                        with dissolve
                        voice x0080
                        x "О"
                        voice x0081
                        x "Ты вернулся"
                        voice x0082
                        x "Куда пропадал?"
                        voice k0155
                        k "Меня зелебоба ебал"
                        voice k0156
                        k "В очко{w=1} жёстко"
                        voice x0083
                        x "Понял"
                        voice k0157
                        k "Я у него украл какие-то свитки"
                        voice k0158
                        k "Посмотри что это"
                        voice x0084
                        x "Показывай"
                        "Ты показал их Саньку"
                        voice x0085
                        x "Мне надо отойти с ними"
                        voice x0086
                        x "Посмотреть что с ними можно сделать"
                        hide px
                        with moveoutright
                        "Санёк ушёл в свою комнату"
                        "Изучать свитки"
                        voice k0159
                        k "Интересно{w=1}, что они могут делать"
                        voice k0160
                        k "И почему они были у зелебобы"
                        $ addTime()
                        "Ты простоял так 6 часов"
                        show px
                        with dissolve
                        voice x0087
                        x "Я прочитал их"
                        voice x0088
                        x "Это древняя тёмная магия"
                        voice x0089
                        x "Она очень сильна, но и опасна"
                        voice k0161
                        k "Ого{w=.4}, что это нахуй{w=.4} и как использовать"
                        voice x0090
                        x "Эти книги запечатали древние укры евреи"
                        voice x0091
                        x "Что бы распечатать эту магию нужны грывни"
                        voice k0162
                        k "Ахуено"
                        voice k0163
                        k "Я голый, как будут деньги буду изучать"
                        voice x0092
                        x "Не знаю"
                        voice x0093
                        x "В последнее время Макс и Саша зарабатывают много денег в боях"
                        voice x0094
                        x "Можешь отправится к ним"
                        voice k0164
                        k "Хорошо{w=1}, найду их и поговорю с ними"
                        voice x0095
                        x "Ты можешь найти их в комнате"
                        voice x0096
                        x "Они часто там спят{w}.."
                        voice k0165
                        k "Ты хочешь сказать{w=.4} что ты{w=.4} ПРЕДЛАГАЕШЬ{w=1} ПЕРЕСПАТЬ С НИМИ!?!?!"
                        voice x0097
                        x "Ты ёбнутый?"
                        voice x0098
                        x "Поговорить с ними еблан"
                        voice k0166
                        k "а"
                        voice k0167
                        k "Ладно"
                        if name != "Кирилл":
                            k "Пойду с ними поговорю"
                            scene black
                            with fade
                            "Кирилл пришёл в комнату"
                            "Ты вступил в 3 окрему штурмову бригаду{w}, удачи{w} успехов{w} в бахмуте"
                            $ OneDiscordMessage("# Глава 1 🏫\nКирилл вступил в отряд".format(persistent.user_name))
                            $ party_list.append(lox)
                            $ lox.exp = (lox.lvl+1)**3 -100
                    if talk_1kirill and not talk_2kirill:
                        $ OneDiscordMessage("# Глава 1 🏫\nвы узнали что делают свитки зелебобы".format(persistent.user_name))
                        call restoreos()
                        $ talk_2kirill = True
                        if name != "Кирилл":
                            "[name]" "Здорова"
                            "[name]" "Нам нужно понять как использовать эти свитки"
                            voice k0169
                            k "Да{w}, я уже вроде понял немного"
                            voice k0170
                            k "Нужны деньги и за них можно будет покупать новую магию"
                            "[name]" "Звучит дорого, показывай"
                        else:
                            voice k0171
                            k "Что же это за свитки"
                            voice k0172
                            k "Посмотрю{w}, для их открытия нужны деньги"
                        show screen magic_shop_menu
                        "Нажмите что бы продолжить"
                    voice k0168
                    k "Время изучать магию!"
                    show screen magic_shop_menu
                    "Нажмите что бы продолжить"
                    jump asdghd
                "Тянка" if action_1tank and talk_2tank and not talk_3tank:
                    $ OneDiscordMessage("# Глава 1 🏫\nТянка пришла в колледж".format(persistent.user_name))
                    $ talk_3tank = True
                    call restoreos()
                    show tank
                    with dissolve
                    voice t0003
                    t "Я пришла сюда"
                    show ps smile at left
                    with dissolve
                    voice s0204
                    s "Сейчас сюда подойдёт Санёк"
                    voice s0205
                    s "Он посмотрит что у тебя за магия и уровень"
                    show px at right
                    with dissolve
                    voice x0218
                    x "Здаствуйте"
                    voice x0219
                    x "Это та Тян о которой вы говорили?"
                    voice s0206
                    s "Да"
                    voice x0220
                    x "Где Макс?"
                    voice s0207
                    s "Он пошёл к Максиму"
                    voice x0221
                    x "Ладно начнём"
                    voice t0004
                    t "Что надо делать?"
                    voice x0222
                    x "Вот магический шар"
                    voice x0223
                    x "Положи на него руку"
                    voice x0224
                    x "Он покажет когда ты в последний раз дрочила"
                    voice x0225
                    x "Точнее магию"
                    t ".."
                    "Тянка положила руку на украину"
                    "Магический шар" "Я вижу.."
                    "Магический шар" "У тебя {b}11 Уровень{/b}"
                    "Магический шар" "Твоя магия это Колючий щит"
                    "Магический шар" "Ты одеваешь его на всех врагов"
                    "Магический шар" "И они получают небольшой урон от шипов"
                    voice x0225b
                    x "Не видел я ещё такой магии"
                    voice t0005
                    t "Крута"
                    voice s0208
                    s "Предлагаю тебе сходить с нами на один бой"
                    voice s0209
                    s "Ты не против?"
                    voice t0006
                    t "Можно, за одно опробую магию"
                    voice t0007
                    t "Только ты купи мне снаряжение за то что мы награбили"
                    voice s0210
                    s "Хорошо"
                    $ OneDiscordMessage("# Глава 1 🏫\nТянка вступила в отряд".format(persistent.user_name))
                    $ party_list.append(tanka)
                    $ tanka.exp = (tanka.lvl+1)**3 -100
                "Санёк" if not first_libriary and first_pola or win_1les and not talk_1sanek or win_2les and not talk_2sanek or win_1dan and not talk_4sanek or win_2dan and not talk_5sanek or win_4dan and not talk_6sanek:
                    if not first_libriary and first_pola:
                        $ OneDiscordMessage("# Глава 1 🏫\nПервый урок с Саньком".format(persistent.user_name))
                        call restoreos()
                        voice x0099
                        x "О вы пришли"
                        show px
                        voice x0100
                        x "Что же, тут вы можете познавать новые знание"
                        voice x0101
                        x "Открывать новые возможности"
                        show px at right
                        with move
                        show ps at left
                        with dissolve
                        show pm oshko
                        with dissolve
                        voice m0196
                        m "Тут можно дрочить?"
                        voice s0211
                        s "Да{w=1.8}, я разрешаю"
                        voice x0102
                        x "Нет"
                        voice x0103
                        x "Я запрещаю"
                        voice x0104
                        x "Сюда вы можете приходить и учиться"
                        voice m0197
                        m "Нельзя это сделать сразу"
                        voice x0105
                        x "Нет{w}, но{w}, я могу вам помочь с моментальным изучением тёмной магии"
                        voice x0106
                        x "Конечно это занимает время"
                        voice s0212
                        s "Это бесплатно?"
                        voice x0107
                        x "Нет"
                        voice m0198
                        m "Сколько?"
                        voice x0108
                        x "Каждое проклятое заклинание будет стоить по своему"
                        voice x0109
                        x "Вы можете посмотреть позже у одного человека"
                        voice x0110
                        x "Пока его тут нет"
                        voice s0213
                        s "Кто это?"
                        voice x0111
                        x "Потом узнаете"
                        voice m0199
                        m "Ладно{w=1.2}, а как нам сейчас получить новые заклинания"
                        voice s0214
                        s "Да, а то у нас по одному уникальному заклинанию"
                        voice s0215
                        s "Которые тяжело совмещать"
                        voice x0112
                        x "Для этого иногда приходите ко мне{w}, я буду вас обучать основам"
                        voice x0113
                        x "Позже мы сможем приступить к более сложным заклинаниям"
                        voice m0200
                        m "Как и когда нам приходить?"
                        voice x0114
                        x "Приходите днём где-то 12:00"
                        voice x0115
                        x "Занятия будут идти до 18:00"
                        voice x0116
                        x "В другое время можем просто поговорить"
                        voice s0216
                        s "Хорошо"
                        voice x0117
                        x "Если вы всё поняли то можем провести первый урок сейчас"
                        voice m0201
                        m "Давай"
                        voice x0118
                        x "Начнём"
                        show magic at top
                        with dissolve
                        voice x0119
                        x "Есть разные типы магии{w}, одни подходят против других"
                        voice x0120
                        x "Или наоборот не подходят"
                        voice s0217
                        s "Круто, а нахуя оно нам"
                        voice m0202
                        m "Ты даун?"
                        voice m0203
                        m "Что бы использовать магии правильно"
                        voice x0121
                        x "Нет{w}, оно вам нахуй не надо"
                        voice x0122
                        x "В нашем мире это не работает"
                        voice x0123
                        x "Любая магия хуярит любую другую"
                        voice x0124
                        x "Единственная сложность в том что магия не восстанавливается естественным способом"
                        voice x0125
                        x "Вам надо пить подозрительные зелья, что бы её восстанавливать"
                        voice m0204
                        m "Нам Борис говорил что может исцелить нас бухлом"
                        voice m0205
                        m "Это правда"
                        voice x0126
                        x "В теории да"
                        voice s0218
                        s "Так зачем нам зелья{w=3}, если мы можем закупаться бухлом и пиздится так"
                        voice x0127
                        x "Не можете"
                        voice x0128
                        x "В нашем мире бухло испаряться если оно покинет место создания"
                        voice x0129
                        x "Так что дальше лавки Бориса у вас не выйдет уйти"
                        voice m0206
                        m "Ладно будем жить там{w=1} z"
                        voice s0219
                        s "Так, то да{w=2}, нам в прицепе нет особого смысла убивать короля демонов"
                        voice s0220
                        s "Он та нам нихуя не сделал"
                        voice x0130
                        x "Делайте что хотите"
                        menu ostatsa_v_boris:
                            "Остаться жить в лавке Бориса и бухать 24/7"
                            "Ебать что за вопрос, конечно, да":
                                $ OneDiscordMessage("# Глава 1 👇\nОстаться жить в лавке Бориса и бухать 24/7\n> `Ебать что за вопрос, конечно, да`".format(persistent.user_name))
                                scene bg shop_bar with fade
                                "Вы решили что вам не нужно спасать мир"
                                "Вы остались бухать до конца жизни"
                                pause 1.5
                                $ ending("Умереть от Бухла")
                                "В какой-то день вы отравились и сдохли"
                                "[end_message]"
                                return
                            "Нет, мы должны спасти мир":
                                $ OneDiscordMessage("# Глава 1 👇\nОстаться жить в лавке Бориса и бухать 24/7\n> `Нет, мы должны спасти мир`".format(persistent.user_name))
                                pass
                        voice m0207
                        m "Нет{w=1}, мы должны его отпиздить"
                        voice m0208
                        m "Просто что бы быть круче"
                        voice s0221
                        s "Ладно, давай так и сделаем"
                        voice x0131
                        x "Что же{w}, сейчас я буду обучать вас новой магие"
                        voice x0132
                        x "Кто останется?"
                        voice s0222
                        s "Что значит кто останется?"
                        voice x0133
                        x "Я не смогу обучить вас обоих, так что выбирайте кто из вас получит новое заклинание"
                        menu first_magic:
                            "Кто получит заклинание \"Леденой шар\""
                            "Давай я([name])":
                                $ OneDiscordMessage("# Глава 1 🏫\n[name] изучил свою первую магию \"Леденой шар\"".format(persistent.user_name))
                                "[name]" "Сюда боты"
                                "[name]" "Первое заклинание"
                                hide pm
                                with dissolve
                                show ps at left
                                with move
                                if name == "Саша":
                                    voice x0134
                                    x "Тебе нужно прочитать этот свиток"
                                    voice x0135
                                    x "Здесь всё просто"
                                    voice x0136
                                    x "Нужно написать то что на нём написано"
                                    voice s0223
                                    s "Тут есть проблема{w=3}, я не умею писать"
                                    voice s0224
                                    s "За всё время я не одного сообщения не написал"
                                    voice s0225
                                    s "У меня дислексия"
                                    voice x0137
                                    x "а, ну это заклинание так не выучить"
                                    voice x0138
                                    x "Расскажу как это работает, но это займёт намного больше времени"
                                    $ addTime()
                                $ a.addSkill(mindfreeze)
                            "Саша" if sasha in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nСаша изучил свою первую магию \"Леденой шар\"".format(persistent.user_name))
                                voice s0226
                                s "Сосать"
                                voice s0227
                                s "Первое заклинание мне"
                                hide pm
                                with dissolve
                                show ps at left
                                with move
                                voice x0213
                                x "Тебе нужно прочитать этот свиток"
                                voice x0214
                                x "Здесь всё просто"
                                voice x0215
                                x "Нужно написать то что на нём написано"
                                voice s0223
                                s "Тут есть проблема{w}, я не умею писать"
                                voice s0224
                                s "За всё время я не одного сообщения не написал"
                                voice s0225
                                s "У меня дислексия"
                                voice x0216
                                x "а, ну это заклинание так не выучить"
                                voice x0217
                                x "Расскажу как это работает, но это займёт намного больше времени"
                                $ addTime()
                                $ sasha.addSkill(mindfreeze)
                            "Макс" if maks in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nМакс изучил свою первую магию \"Леденой шар\"".format(persistent.user_name))
                                voice m0209
                                m "Сюда"
                                voice m0210
                                m "Пошёл нахуй"
                                voice s0231
                                s "Иди нахуй гандон ебаный"
                                hide ps
                                with dissolve
                                show pm oshko at left
                                with move
                                $ maks.addSkill(mindfreeze)
                        voice x0139
                        x "И так приступим"
                        scene black
                        with fade
                        "Санёк рассказывал как работает магия"
                        "Как делаются круги призыва и всякое такие"
                        "Вы просидели так 6 часов"
                        $ addTime()
                        "Наконец-то вы закончили"
                        scene bg koledsh_class
                        with fade
                        show px
                        with dissolve
                        voice x0140
                        x "Что же{w}, теперь ты умеешь использовать ледяную магию"
                        voice x0141
                        x "Идите в лес и опробуйте её в реальном бою!"
                        voice x0142
                        x "Если вас отпиздят идите в лавку Бориса"
                        voice x0143
                        x "У заклинаний есть ограничения{w}, один человек может носить всего 6 заклинаний"
                        voice x0144
                        x "Так что собирай с умом отряд"
                        voice x0145
                        x "Удачи вам в первом реальном бою"
                        $ first_libriary = True
                        jump asdghd
                    if win_1les and not talk_1sanek:
                        $ OneDiscordMessage("# Глава 1 🏫\n{0} вернулся после первого боя к Саньку".format(persistent.user_name))
                        $ talk_1sanek = True
                        call restoreos()
                        show px
                        with dissolve
                        voice x0146
                        x "О вы пришли"
                        voice x0147
                        x "Как прошёл ваш первый бой?"
                        show ps smile at left
                        show pm at right
                        with dissolve
                        voice m0211
                        m "Круто"
                        voice m0212
                        m "Мы их разьебали"
                        voice s0232
                        s "Мы получили нормально так опыта"
                        voice s0233
                        s "Думаю теперь можем сами сражаться без проблем"
                        voice x0148
                        x "Это хорошо{w}, не забывайте покупать снаряжение у Бориса"
                        if action_1tank:
                            voice s0234
                            s "Мы ещё с Тянкой пообщялись"
                            voice s0235
                            s "Она согласилась пойти к тебе учится"
                            voice x0149
                            x "Это хорошо{w}, ещё один ученик"
                            voice m0213
                            m "Да, но мы сказали что ты будешь это делать бесплатно"
                            voice x0150
                            x "Вы ахуели?"
                            voice x0151
                            x "Пидарасы ебаные я вам разрешил бесплатно заниматься"
                            voice x0152
                            x "А вы Тянок сюда приводите"
                            voice m0214
                            m "Та ладно{w=1}, это один раз"
                            voice x0153
                            x "Под каблуки"
                        voice x0154
                        x "Ладно"
                        voice x0155
                        x "Начнём второй урок"
                        voice x0156
                        x "Сейчас я вам расскажу как делать тройное сально"
                        voice x0157
                        x "На поле боя есть важная вещь как расстановка противников"
                        voice x0158
                        x "Не всегда у вас выйдет ударить задний ряд противника"
                        voice x0159
                        x "Вам надо будет убить тех кто за ними"
                        voice x0160
                        x "Некоторые заклинания могут атаковать только задние ряди"
                        voice x0161
                        x "И некоторые наоборот только переднее"
                        voice x0162
                        x "Сейчас я вас обучу заклинанию смены позиции"
                        voice x0163
                        x "С помощью его вы можете поменять местами врага с другим врагом"
                        voice x0163b
                        x "При этом не теряя время на ход"
                        menu magic2:
                            "Кто получит заклинание \"Смена позиции\""
                            "Давай я([name])":
                                $ OneDiscordMessage("# Глава 1 🏫\n[name] изучил магию \"Смена позиции\"".format(persistent.user_name))
                                hide pm
                                with dissolve
                                show ps at left
                                with move
                                $ a.addSkill(magicswap)
                            "Саша" if sasha in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nСаша изучил магию \"Смена позиции\"".format(persistent.user_name))
                                hide pm
                                with dissolve
                                show ps at left
                                with move
                                $ sasha.addSkill(magicswap)
                            "Макс" if maks in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nМакс изучил магию \"Смена позиции\"".format(persistent.user_name))
                                hide ps
                                with dissolve
                                show pm oshko at left
                                with move
                                $ maks.addSkill(magicswap)
                        voice x0164
                        x "Хорошо{w}, и так приступим"
                        scene black
                        with fade
                        "Вы изучали как наебать монстров, что бы они поменялись местами"
                        "Спустя 6 часов вы закончили"
                        scene bg koledsh_class
                        with fade
                        voice x0165
                        x "Теперь вы можете использовать эту магию, она тратит не сильно много маны"
                        voice x0166
                        x "Так что удачи вам в бою!"
                        jump asdghd
                    if win_2les and not talk_2sanek:
                        $ OneDiscordMessage("# Глава 1 🏫\nВы вернулись после зачистки чащи леса к Саньку".format(persistent.user_name))
                        $ talk_2sanek = True
                        call restoreos()
                        show px
                        with dissolve
                        voice x0167
                        x "Вы смогли зачистить чащю леса?"
                        voice x0168
                        x "Да вы растёте на глазах"
                        voice m0215
                        m "Та ебать"
                        voice s0236
                        s "Мы вахуи"
                        voice s0237
                        s "На нас нападают монстры из ZELEBOBA ADVENTURE"
                        voice m0216
                        m "Так ещё и шкафчик"
                        voice m0217
                        m "Который когда-то ёбнул Рому"
                        voice x0169
                        x "Здешние земли опасны.."
                        voice x0170
                        x "Но вы живы"
                        voice x0171
                        x "Так что можем продолжить наше обучение"
                        voice x0172
                        x "Сегодня мы изучим заклинание Исцеление"
                        voice x0173
                        x "С помощью его можно исцелить себя"
                        voice x0174
                        x "Уточню{w}, ТОЛЬКО СЕБЯ"
                        voice x0175
                        x "Кто из вас его получит?"
                        menu magic3:
                            "Кто получит заклинание \"Магическое исцеление\""
                            "Давай я([name])":
                                $ OneDiscordMessage("# Глава 1 🏫\n[name] изучил магию \"Магическое исцеление\"".format(persistent.user_name))
                                $ a.addSkill(magicheal)
                            "Саша" if sasha in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nСаша изучил магию \"Магическое исцеление\"".format(persistent.user_name))
                                hide pm
                                with dissolve
                                show ps at left
                                with move
                                $ sasha.addSkill(magicheal)
                            "Макс" if maks in party_list:
                                $ OneDiscordMessage("# Глава 1 🏫\nМакс изучил магию \"Магическое исцеление\"".format(persistent.user_name))
                                hide ps
                                with dissolve
                                show pm oshko at left
                                with move
                                $ maks.addSkill(magicheal)
                        scene black
                        with fade
                        "Как обычно вы занимались 6 часов"
                        "Вы получили заклинание Исцеление"
                        "По дрочи на него теперь"
                        scene bg koledsh_class
                        with fade
                        show px
                        with dissolve
                        voice x0176
                        x "Что же{w}, следующий урок нельзя проводить в здании"
                        voice x0177
                        x "Так что встретимся в поле утром"
                        voice x0178
                        x "До завтра!"
                        hide px
                        with dissolve
                        show pm sit at right
                        show ps sit at left
                        with dissolve
                        voice s0238
                        s "Пиздец я заебался"
                        voice m0218
                        m "Я уже не могу{w=1}, не хочу ходить на его уроки"
                        voice m0219
                        m "Слишком сложно"
                        voice s0239
                        s "Вроде другой мир"
                        voice s0240
                        s "А блять нихуя не поменялось{i}(со звуком смачного пердежа){/i}"
                        voice s0241
                        s "Всё так же сидим по 6 часов учимся"
                        voice m0220
                        m "Это пиздец"
                        voice m0221
                        m "Я так понимаю завтра будет Захист Видчизнаны?"
                        voice s0242
                        s "Видимо да"
                        voice s0243
                        s "Мы в жизни не разу туда не ходили"
                        voice s0244
                        s "Можем пойти глянуть как это вообще выглядит"
                        voice m0222
                        m "Давай"
                        scene bg koledsh_class
                        jump asdghd
                    if win_1dan and not talk_4sanek:
                        $ OneDiscordMessage("# Глава 1 🏫\nПосле спасения друга вы вернулись к Саньку".format(persistent.user_name))
                        $ talk_4sanek = True
                        call restoreos()
                        show px
                        with dissolve
                        voice x0179
                        x "Вы снова пришли"
                        voice x0180
                        x "С возращением в отряд"
                        voice s0245
                        s "Что сегодня будем изучать?"
                        voice m0223
                        m "Телепорт?{w=1.4} Создание негров?"
                        voice k0173
                        k "Это мои гримуары могут"
                        voice x0181
                        x "Сегодня мы изучим как работают уровни"
                        voice x0182
                        x "Сам уровень он влияет на жизни"
                        voice x0183
                        x "У монстров нет"
                        voice x0184
                        x "Чем больше у вас уровень тем больше монстры будут промахиваться"
                        voice x0185
                        x "И наоборот"
                        voice x0186
                        x "Чем больше уровень у монстра тем больше ты будешь промахиваться"
                        voice x0187
                        x "Когда-то вам попадутся враги в разы сильнее чем вы"
                        voice m0224
                        m "И что тогда нам делать?"
                        voice x0188
                        x "Это мы изучим в следующий раз"
                        hide px
                        with dissolve
                        jump asdghd
                    if win_2dan and not talk_5sanek:
                        $ OneDiscordMessage("# Глава 1 🏫\nПосле спасения друга вы вернулись к Саньку".format(persistent.user_name))
                        $ talk_5sanek = True
                        call restoreos()
                        show px
                        with dissolve
                        voice x0189
                        x "Как я и обещал"
                        voice x0190
                        x "Сегодня мы изучим магию пробития уровня"
                        voice x0191
                        x "Вы сможете пробивать врагов которые уровнем гораздо выше чем вы"
                        voice x0192
                        x "Для слабых будет достаточно использовать 1-2 раза"
                        voice x0193
                        x "Но для сильных больше"
                        show ps at right
                        with dissolve
                        voice s0246
                        s "Это работает на всех?"
                        voice x0194
                        x "Да{w}, но есть побочный эффект"
                        voice x0195
                        x "Если использовать на слабого врага то вы понизите свой шанс пробития"
                        show pm at left
                        with dissolve
                        voice m0225
                        m "Почему?"
                        voice x0196
                        x "Разраб даун"
                        voice x0197
                        x "Итак{w} приступим"
                        $ renpy.call("lb_by_magic", lovedefence, True)
                        voice x0198
                        x "Теперь вы сможете одолеть сильных врагов"
                        voice x0199
                        x "Удачи вам!"
                    if win_4dan and not talk_6sanek:
                        $ OneDiscordMessage("# Глава 1 🏫\nНаши школьники окончили колледж".format(persistent.user_name))
                        $ talk_6sanek = True
                        call restoreos()
                        show pm oshko at right with moveinright
                        show ps smile at left with moveinleft
                        show px with moveinbottom
                        voice x0200
                        x "Сегодня"
                        voice x0201
                        x "Вы заканчиваете наш колледж"
                        voice s0247
                        s "Перемога"
                        voice m0226
                        m "Ураа, роблокс"
                        voice s0248
                        s "У тебя же он не работает"
                        voice m0227
                        m "Иди нахуй"
                        voice x0202
                        x "Вы освоили всё чему я мог вас научить"
                        voice x0203
                        x "Вы зачистили все окрестности"
                        voice x0204
                        x "Больше монстры на нас нападать не будут"
                        voice x0205
                        x "Я благодарен вам за это"
                        voice m0228
                        m "Пасиба"
                        voice x0206
                        x "С этого момента вы свободы"
                        voice x0207
                        x "Можете отправиться в столицу и продолжить свой путь магов{w}, тем более у вас ещё много мест для новых елементов магии"
                        voice s0249
                        s "Нет"
                        voice m0229
                        m "Мы уже почти сделали всё что нам нужно"
                        voice s0250
                        s "Нам осталось одолеть настоящего короля деманов"
                        voice m0230
                        m "Мы нашли его место положение и скоро его убьём"
                        voice x0208
                        x "Ого"
                        voice x0209
                        x "Я в вас верю"
                        voice x0210
                        x "Ну а теперь"
                        voice x0211
                        x "Делайте что хотите"
                        voice x0212
                        x "Ту комнату можете себе оставить на постоянно"
                        voice s0251
                        s "Хорошо"
                        voice m0231
                        m "Идём поговорим ещё с кем-то"
                        hide pm with moveoutright
                        hide ps with moveoutleft
                        hide px with moveoutbottom
                        jump asdghd
                "Уйти":
                    jump kudaidti
        "Комната":
            scene bg koledsh_room
            with fade
            menu asdaghd:
                # ИЗМЕНИТЬ
                "Общий сбор" if not talk_3kirill and win_2dan and talk_3boris and game_time == 24:
                    $ OneDiscordMessage("# Глава 1 🏫\nОбщий сбор".format(persistent.user_name))
                    call restoreos()
                    $ talk_3kirill = True
                    show pk with dissolve
                    voice k0174
                    k "Просыпайтесь!"
                    show pm smile at right with moveinright
                    show ps smile at left with moveinleft
                    voice m0232
                    m "Что надо"
                    voice s0252
                    s "Зачем разбудил"
                    voice k0175
                    k "Вообще-м"
                    voice k0176
                    k "Скоро у вас будет выпускной"
                    voice k0177
                    k "Вы закончите колледж магии"
                    voice m0233
                    m "Ураа среднее образование"
                    voice s0253
                    s "А когда это будет?"
                    voice k0178
                    k "Очень скоро"
                    voice k0179
                    k "В конце месяца"
                    voice m0234
                    m "Вроде недавно сюда попали"
                    voice s0254
                    s "Время быстро летит"
                    voice s0255
                    s "Скоро мы вообще покинем это место"
                    voice m0235
                    m "Быстрей бы"
                    voice m0236
                    m "Так хочется отпиздить Дениса"
                    voice k0180
                    k "А кто не хочет"
                    voice k0181
                    k "Недавно я смог его сфоткать"
                    voice k0182
                    k "Хотите покажу?"
                    voice s0256
                    s "Нахуй оно нам надо"
                    voice m0237
                    m "Реально"
                    voice k0183
                    k "Но я вам покажу"
                    call lb_by_magic(swordofdeath) from _call_lb_by_magic
                    voice s0257
                    s "Это отвратительно!"
                    voice m0238
                    m "Этим можно убивать"
                    voice k0184
                    k "Та ну"
                    voice k0185
                    k "Ладно давайте отправляться в новое приключение!"
                    hide pm with moveoutright
                    hide ps with moveoutleft
                    hide pk with moveoutbottom
                "Саша" if win_1dan and not talk_1sasha or not talk_3sasha and win_4dan:
                    if win_1dan and not talk_1sasha:
                        $ talk_1sasha = True
                        call restoreos()
                        show ps
                        with dissolve
                        voice s0258
                        s "Что же"
                        voice s0259
                        s "Наконец-то мы все собрались"
                        voice s0260
                        s "Спустя месяц{w=1.8}, мы смогли найти тебя Кирилл"
                        show pk dshentelmen at right
                        with dissolve
                        voice k0186
                        k "Да{w=1}, зелебоба пидр"
                        show pm talk at left
                        with dissolve
                        voice m0239
                        m "Нам надо обсудить одного дауна"
                        voice k0187
                        k "Ты про меня?"
                        voice m0240
                        m "Нет{w=1}, у нас тут один главный даун"
                        voice s0261
                        s "Не буду говорить кто это{w=1}.{w=.5}. Денис"
                        voice m0241
                        m "Да"
                        voice k0188
                        k "А{w=.6} ну так он это{w=1} пидар"
                        voice s0262
                        s "Знаем"
                        voice m0242
                        m "Он как-то смог связать лолей и поработить их"
                        voice k0189
                        k "Он вроде этим занимался всю жизнь"
                        voice s0263
                        s "Ещё и при жизни"
                        voice m0243
                        m "Так-то да{w=1}, но{w=.5} в этот раз они его слушают и выполняют то что он им говорит"
                        voice s0264
                        s "Если у нас есть длинное название и наша задача это одолеть короля демонов"
                        voice k0190
                        k "У Бориса стать торговцем"
                        voice s0265
                        s "От куда знаешь?"
                        voice k0191
                        k "Он это каждому второму рассказывает"
                        voice m0244
                        m "Но какая цель у Денис?"
                        voice m0245
                        m "Сомневаюсь что лоли дала бы ему цель ебать лоли"
                        voice s0266
                        s "Идём тогда к королю демонов"
                        voice s0267
                        s "Одолеем его"
                        voice k0192
                        k "Возможно мы сможем выбраться от сюда"
                        voice m0246
                        m "Шанцы есть"
                        voice m0247
                        m "Отправляемся"
                        scene black
                        with fade
                        "Вы отправились в путь"
                        "По пути вам не попадались монстры"
                        $ OneDiscordMessage("# Глава 1 🏫\nВы пришли убивать короля демонов".format(persistent.user_name))
                        play music "audio/music/videoplayback.mp3"
                        scene bg demon
                        with fade
                        "Вы пришли"
                        show ps
                        with dissolve
                        voice s0268
                        s "Это и есть замок короля демонов?"
                        show pkq stoika at left
                        with dissolve
                        voice k0193
                        k "Да{w=1}, такой был на гримуарах нарисован"
                        voice k0194
                        k "\"Если что-то будет не работать вернуть по адресу: Минск, Минская область, Беларусь, ул. Король Деманов\""
                        show pm at right
                        with dissolve
                        voice m0248
                        m "У нас хоть один не работал?"
                        voice k0195
                        k "Нет{w=1}, но мы не смогли все разблокировать"
                        voice k0196
                        k "Так как король демонов еврей ебаный"
                        voice s0269
                        s "У нас в мире два еврея"
                        voice m0249
                        m "Ты?"
                        voice s0270
                        s "Нет блять"
                        voice m0250
                        m "Ладно{w=1.2}, заходим к нему"
                        scene black
                        with fade
                        "Вы зашли в здание"
                        scene bg demon_kor
                        with fade
                        "Внутри не кого не было"
                        "Вы начали ходить по комнатам в поисках его"
                        "Саша нашёл записку"
                        "{i}Я хочу освободить этот мир{w}, что бы все души могли вернуться в свою реальность{/i}"
                        voice s0271
                        s "Возможно он не плохой"
                        "Вы проложили искать"
                        show ps
                        with dissolve
                        "Саша ходил по коридорам"
                        "Но"
                        "В один момент его кто-то схватил за плече"
                        "Нечто знакомое"
                        with fade
                        "В гlазах Саши потемнело"
                        scene black
                        with fade
                        voice s0272
                        s "Опять видение?"
                        voice s0273
                        s "Я снова в прошлом?"
                        "?" "Нет"
                        "?" "Это будущие"
                        scene bg world_norm
                        with fade
                        show s
                        with dissolve
                        "?" "Это будущие{w}, но без Дениса"
                        voice s0274
                        s "Кто ты?"
                        "?" "Тебе нельзя знать об этом"
                        scene bg world_ad
                        with fade
                        show s
                        with dissolve
                        "?" "Это ужасное будущие если Денис останется в живых"
                        "?" "Весь мир превратился в подземные клетки"
                        "?" "В мире больше не осталось не кого кроме маленьких девочек и мальчиков"
                        voice s0275
                        s "Это ужасно"
                        "?" "Только ты"
                        "?" "Можешь убить его и спасти мир"
                        "?" "Выберитесь из этой клетки и найдите его!"
                        "?" "Останови его любой ценой!"
                        voice s0276
                        s "Если ты знаешь так много"
                        voice s0277
                        s "Что произошло утром?"
                        "?" "Тебе нельзя это знать"
                        voice s0278
                        s "Но почему"
                        "?" "Тихо{w}, он уже здесь"
                        "?" "Мне нужно идти"
                        scene bg demon_kor
                        with fade
                        show ps
                        with dissolve
                        voice s0279
                        s "Ебать что это было"
                        voice s0280
                        s "Если я не смогу остановить Дениса"
                        voice s0281
                        s "Мы все умрём{w}, а сам мир превратиться в ад"
                        voice s0282
                        s "Я не должен этого допустить"
                        voice s0283
                        s "Мы{w=1.8} все{w=1.5} сбежим из этого места"
                        "Ты услышал крик"
                        voice s0284
                        s "Кто это?"
                        voice k0197
                        k "Я кое-что нашёл"
                        "Ты направился в сторону крика"
                        scene bg demon_room
                        with fade
                        show pk auf
                        with dissolve
                        "Зайдя в комнату к Кирилл вы увидели расчленённый труп"
                        "Который оброс ветками и листьями"
                        show pm talk at left
                        with dissolve
                        voice m0251
                        m "Ебать"
                        show ps at right
                        with dissolve
                        voice s0285
                        s "Его уже кто-то убил до нас"
                        voice k0198
                        k "Кто мог это сделать"
                        voice s0286
                        s "Он хотел вернуть всех в реальный мир"
                        voice k0199
                        k "Eбать он пидр"
                        voice m0252
                        m "Так нет{w=1.2}, нам нужно от сюда выбраться"
                        voice k0200
                        k "Почему?"
                        voice s0287
                        s "Тут Денис{w=2}, этого достаточно?"
                        voice k0201
                        k "Тогда ладно"
                        voice m0253
                        m "Так, а реально{w=1.4}, кто его убил если это была наша задача?"
                        voice s0288
                        s "Хз{w=1} хуй знает"
                        voice m0254
                        m "Я заметил что вся нечисть пропала после нападение Дениса"
                        voice m0255
                        m "Конечно я надеюсь что это не так"
                        voice k0202
                        k "Ты хочешь сказать его убил Денис?"
                        voice s0289
                        s "Та ну нет"
                        voice s0290
                        s "Он был настолько слаб что мы избивали его каждый день"
                        voice m0256
                        m "Да{w=.4}, но когда он на нас напал он не был слаб"
                        voice k0203
                        k "Странно что он умер в кровати"
                        "Саша и Макс вспомнили что во сне все беззащитные и не могут не чего сделать"
                        voice m0257
                        m "Эта ебаная крыса его убила пока он спал"
                        voice s0291
                        s "Пидарас"
                        voice k0204
                        k "Гандон"
                        voice s0292
                        s "Хуесос"
                        voice m0258
                        m "Денис"
                        voice s0293
                        s "Мы должны зачистить подземелье"
                        voice s0294
                        s "Он точно будет там"
                        voice s0295
                        s "Мы сможем его убить"
                        voice s0296
                        s "И вернуться в наш мир"
                        voice m0259
                        m "Отправляемся!"
                        voice k0205
                        k "Мы должны выбраться от сюда!"
                        "Земля из-под ног начала пропадать{w}, всё начало темнеть"
                        scene bg angels
                        with fade
                        show u muha
                        with dissolve
                        voice u0100
                        u "{bt=3}Вы не можете покинуть этот мир{/bt}"
                        voice s0297
                        s "Почему"
                        voice u0101
                        u "{bt=3}Я создала его для таких душ как вы{/bt}"
                        voice u0102
                        u "{bt=3}Вы и так умерли{w=1} как вы представляете воскрешение?{/bt}"
                        voice u0103
                        u "{bt=3}В той реальности в которой вы были прошло много лет{/bt}"
                        voice u0104
                        u "{bt=3}Время здесь в разы медленнее чем там{/bt}"
                        voice s0298
                        s "У нас есть цель"
                        voice s0299
                        s "Убить Дениса дабы спасти мир"
                        voice u0105
                        u "{bt=3}Дениса?{/bt}"
                        voice s0300
                        s "Да"
                        voice u0106
                        u "{bt=3}Нет{w=1} героя этого мира нельзя убивать{/bt}"
                        voice s0301
                        s "Героя?"
                        voice s0302
                        s "Что"
                        voice u0107
                        u "{bt=3}Он своими руками одолел короля демонов{/bt}"
                        voice u0108
                        u "{bt=3}В отличие от вас ему хватило сил и смелости это сделать{/bt}"
                        voice u0109
                        u "{bt=3}Если вы попробуете его хоть тронуть{/bt}"
                        voice u0110
                        u "{b}Я вас убью{/b}"
                        scene bg demon_room
                        with fade
                        "Вы вернулись в комнату"
                        show ps
                        with dissolve
                        voice s0303
                        s "Кажется я узнал кто, убил короля демонов"
                        scene black
                        with fade
                        "Саша рассказал всё что было"
                        "Вы решили идти до конца"
                        "Освободить всех лолей из рабства Дениса"
                        "?" "Я верю в тебя"
                        "Вы отправились обратно в городок \"Бісмут\""
                        "Кто-то понял букву \"с\" на \"х\""
                        show screen map
                        play music "music/Path to Lake Land.ogg"
                        ''
                    if not talk_3sasha and win_4dan:
                        $ OneDiscordMessage("# Глава 1 🏫\nПлан по победе над Денисом".format(persistent.user_name))
                        $ talk_3sasha = True
                        show pm oshko at right with moveinright
                        show ps uwu at left with moveinleft
                        show pk with moveinbottom
                        voice m0260
                        m "Денис явно теряет всё что имел"
                        voice s0304
                        s "Теперь он прячеться у себя в подвале"
                        voice k0206
                        k "Ему страшно"
                        voice s0305
                        s "Мы должны придумать план по штурму подвала"
                        voice m0261
                        m "Можем просто залететь в него"
                        voice k0207
                        k "Предлагаю просто залететь"
                        voice m0262
                        m "Го"
                        voice s0306
                        s "Нет"
                        voice s0307
                        s "Нам нужен план"
                        "Вы просидели так 6 часов"
                        $ addTime()
                        voice k0208
                        k "Вы блять заебали"
                        voice k0209
                        k "Мы за 6 часов не придумали план"
                        voice s0308
                        s "Та пиздeц"
                        voice m0263
                        m "Давайте тогда по моему плану"
                        voice k0210
                        k "Или по моему"
                        voice m0264
                        m "Залетаем и ебём его"
                        voice s0309
                        s "Хорошо{w=1.5}, рас у нас нету идей то делаем так"
                        voice s0310
                        s "Вы не забыли про важную магию?"
                        voice s0311
                        s "Она нам пригодиться"
                        voice k0211
                        k "Конечно"
                        voice m0265
                        m "Мы ради неё и жили"
                        voice s0312
                        s "Тогда хорошо"
                        voice s0313
                        s "Ещё"
                        voice s0314
                        s "По поводу наших воспоминаний"
                        voice s0315
                        s "Я не вижу в них зла"
                        voice s0316
                        s "Думаю им можно доверять"
                        voice m0266
                        m "Ок"
                        voice k0212
                        k "Отправляемся пиздить Дениса"
                "Поспать":
                    scene black
                    with fade
                    
                    pause(1.5)
                    if random_choise(4) and not matras:
                        $ OneDiscordMessage("# Глава 1 🏫\nМакс и Саша потрахались в тесной кроватке".format(persistent.user_name))
                        "Вы спите"
                        "У Саши встал"
                        "Саша прижался к Максу"
                        play sound 'скрипКровати.mp3'
                        "Они начали трахаться"
                        $ ach_sex_ms.grant()
                    random:
                        "Вы поспали 6 часов.."
                        "Вы пролижали 6 часов.."
                        "Вы подрочили 6 часов.."
                        "Вы поспали шесть минут шестого.."
                        "Вы трахались 6 часов.."
                        "Вы ебались 6 часов.."
                        "Вы поспали 6 часов.."
                        "Вы не спали 6 часов.."
                    $ addTime()
                    $ wait_most += 1
                    scene bg koledsh_room
                    with fade
                    jump asdaghd
                "Уйти":
                    pass
        "Уйти":
            pass

    show screen map
    play music "music/Path to Lake Land.ogg"
    scene black
    ''
    return
