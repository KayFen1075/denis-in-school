image lolidance:
    "u dab"
    pause(0.15)
    "u muha"
    pause(0.15)
    "u nag"
    pause(0.15)
    "u"
    pause (0.15)
    "u zov"
    pause (0.15)
    "u hide"
    repeat

label deadw:
    scene main_menu_ch_1
    with fade
    pause(3)
    $ persistent.main_menu = "gui/main_menu_ch_1.png"
    $ config.main_menu_music = "music/BitWaves.wav"
    $ renpy.notify("Заглягни в главное меню")
    scene black
    play music "music/Do Not Run.mp3"
    with Fade(1, 10, 0.2, color="#ffff")
    scene bg sky
    "? ? ?" "Где я"
    "? ? ?" "Что прозошло"
    "? ? ?" "Помню что на меня кто-то напал в спину.."
    "? ? ?" "Как будто со мной кто-то был"
    "? ? ?" "Почему я ни чего не чуствую"
    b "{bt=3}Иди за мной{/bt}"
    "? ? ?" "Кто ты"
    "? ? ?" "{i}{move}начали двигатся{/move}{/i}"
    "? ? ?" "Что происходит"
    show u
    with dissolve
    with vpunch
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    u "{bt=3}Сейчас будет идти суд над вами всеми{/bt}"
    show u zov
    with vpunch
    u "{bt=3}Так мы сможем понять куда вы попадёте{/bt}"
    show u dab
    with vpunch
    u "{bt=3}Ад или рай{/bt}"
    "Наступило молчание"
    "Все ждали приговора"
    "Как вдруг"
    menu kanon:
        "Пойти по канону или в соло"
        "Канон":
            menu adray:
                "Кому дать слово?"
                "?":
                    "Вы дали слово Денису"
                    "Возможно это было худшее решение{w} за всю игру"
                    d "{sc}Иди нахуй{/sc}"
                    "Перед нами появился педофил"
                    "Мы так и не могли двигатся"
                    d "Я твою мать"
                    u "{bt=3}Такое{w}, не приемлемо в небесах{/bt}"
                "?":
                    "Вы дали слово Кириллу"
                "?":
                    "Вы дали слово Саше"
                ".":
                    "Вы дали слово Максу"
                    m "Я знаю всё про неё, так что на вопросы отвечу правильно!"
                    show u muha
                    with vpunch
                    u "{bt=3}Чтоже{w}, через тебя будет проходить суд{/bt}"
                    u "{bt=3}В зависимости от твоих ответов будет зависить судьба вас всех{/bt}"
                    show u nag
                    with vpunch
                    u "{bt=3}И так{/bt}"
                    u "{bt=3}Лоли или милфы?{/bt}"
                    m "Канечно{w} милфы"
                    hide u
                    show lolidance
                    pause(3)
                    u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                    m "Для тебя я буду старшим братиком"
                    u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    u "{bt=20}Любишь меня?{/bt}"
                    m "Иди нахуй"
                    u "{bt=50}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    u "{bt=50}Я считаю{w} что{w} вы все{w} можете{w} попасть{w} в{w} рай{/bt}"
                    jump ray
        "В соло":
            return
    return
    
label ad:

    u "{bt=3}Вы все отправляетесь в ад{/bt}"
    u "{bt=3}Мучения и страдания будут преследовать всю всюду{/bt}"
    scene black
    with fade
    "Всё потемнело"
    "Мы начали падать"
    "Куда-то глубоко в низ"
    "Был слышен только ветер"
    "И стоны Дениса"
    pause(2)
    k "Я чуствую себя!"
    s "Перестань дрочить даун"
    k "Динах"
    m "Денис ты еблан?{w} Нахуй ты бога нахуй послал"
    m "Ёбнутый даун"
    pause(1.5)
    "Не знаю сколько мы падали"
    return

image islands:
    "bg island2"
    pause(12)
    "bg island3"
    pause(12)
    "bg island4"
    repeat

label ray:
    play music "music/Cliffs.mp3"
    scene black
    with fade
    "Ноги оторвались с небес"
    "Мы начали подниматься куда-то верх"
    "Я начал чуствовать.."
    s "Куда мы летим"
    m "Ебалн{w} в рай"
    d "Знаете{w} я бы её трахнул{w} и вас тоже"
    k "❤️❤️❤️"
    k "Трахни труп"
    d "Иди ко мне"
    m "Я так понимаю все мы здохли"
    s "Думаю{w} возможно{w} я перебрал с мефедроном"
    k "Хочешь покажу пенис?"
    "{i}Кирилл показал член{w}, но не кто не увидел из-за темноты{/i}"
    m "Я могу преставить как мы втроём здохни"
    m "Но, {w}кто убил Дениса?"
    s "Я думаю достаточно людей, которые хотели бы это сделать"
    "Вы услышали звук открывающихся ворот"
    "Вокруг всё посветлело"
    k "Я ебал мухомор"
    play music ray
    scene bg rayreys
    with fade
    "Перед нами открылись ворота"
    "Из чистых облаков{w}, словно конча"
    show pm talk
    with fade
    m "Я не понимаю"
    m "Почему мы все идём в рай{w}, если Денису там не место"
    show pm talk at left
    with move
    show ps at right
    with dissolve
    s "Хз"
    s "Где все?"
    m "Хороший вопрос"
    m "Мы вместе поднимались сюда"
    s "У меня есть теория{w} что Дениса оно не подняло"
    m "Он типо насквозь через ад ещё пролетит?"
    s "Да"
    s "Он уже в пустоте в майнкрафте умерает"
    m "Урааа Роблокс"
    m "Где Кирилл тогда?"
    s "Мне кажется или он опять его спиздил"
    s "Когда мы падали он сказал{w} \"Трахни труп\" "
    s "Формально он труп"
    m "Хм{w}, ладно похуй"
    m "Идём в рай"
    m "Будем кайфовать"
    hide pm
    hide ps
    with dissolve
    "Вы начали подходить всё ближе и ближе к вратам"
    "Как вдруг"
    show u
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    u "{bt=3}Первое что вы должны знать{/bt}"
    u "{bt=3}В раю запрещена вся похабщина{/bt}"
    hide u
    show lolidance
    b "{bt=3}Тобиж вам запрещенно трахаться{w} и нарушать законы Украины{/bt}"
    b "{bt=3}Если вы их нарушите{w} будет{w} штраф{w} в размере{w} в ад{/bt}"
    b "{bt=3}Так что можете наслаждаться спокойной жизнью!{/bt}"
    hide lolidance
    with dissolve
    m "Эм..{w} лучше уж в ад"
    s "Да{w} потрахаемся на последок?"
    m "Го"
    scene black
    with fade
    "~ax-ax-ax"
    m "Что же{w}, теперь можем идти"
    scene islands
    with fade
    play music "music/BitWaves.wav"
    "Мы зашли в врата"
    "Перед нами были прекрасные виды"
    "Перед вами простирался райский пейзаж: мягкие облака, яркое солнце, и вдалеке виднелись красочные острова"
    "Ангелы играли music/BitWaves.wav музыку"
    show ps at right
    show pm talk at left
    with dissolve
    s "Нам надо придумать что делать"
    m "Можем найти Кирилла{w}, не думаю что Денис мог его утащить в ад за собой"
    s "Я вижу на том острове церковь"
    s "Идём туда"
    menu ostatsa_v_ray:
        "Пойти?"
        "Пойти искать Кирилла":
            pass
        "Остаться в раю":
            scene ending ray
            with fade
            pause 1.5
            $ ending("Остаться в раю")
            "Вы посчитали что вам не нужны приключения"
            "Вы остались в раю что бы слушать music/BitWaves.wav музыку"
            "[end_message]"
            menu kirliskat:
                "Продолжить искать Кирилла?"
                "Да":
                    pass
                "Нет":
                    return
    m "Да"
    m "Если что мы всегда можем получить штраф"
    s "Кстати{w}, я хотел тебя кое о чём спросить.."
    m "Что?"
    menu vashniy_vibor:
        "Спросить про утро или промолчать?"
        "Спросить":
            s "Что происходило сегодня утром?"
            s "Почему ты опоздал на 5 урок?"
            m "Ты тоже вообще-то опаздал"
            s "Я дрочил, уменя есть причина"
            m "Ну{w}, я просто{w} как обычно проспал"
            m "Не чего большего"
            s "{i}Он явно что-то не договаривает{/i}"
            m "Почему ты этим заинтересовался?"
            m "Ты обычно про это не спрашивал"
            s "Сегодня стало интересно"
            s "Вот и спросил"
            s "Сам видешь какой сегодня странный день"
            m "Ладно идём дальше"
            $ ch_1_dialog_ms = True
        "Промолчать":
            s "Не чего"
            s "Уже забыл что хотел спросить"
    $ renpy.notify('Макс это запомнит')
    scene black
    with fade
    "Так они пошли до церкви"
    "По пути обсирая Дениса"
    scene bg cercov
    with fade
    show ps smile at left
    show pm da at right
    with dissolve
    m "Что же мы пришли"
    m "Зачем им церковь на небесах?"
    s "Хз"
    s "Мб можно потрахатся и покаяться в церкве"
    m "Когда-то проверим"
    m "Я вот сейчас задумался"
    m "Почему я зелёный{w}, а не голубой как ты"
    s "Почему мы тогда писксельные и всё вокруг тоже"
    m "Это я так понимаю мы не узнаем до конца игры"
    s "Да"
    pause(1)
    m "Пизда"
    s "Ты видел хуй Кирилла?{w} Когда он его показывал"
    m "Нет, темно было как в очке негра"
    m "Мы даже не узнали какого он цвета{w}, вдруг он тоже голубой"
    m "Но я видел его член до этого"
    s "Все видели"
    s "Найти человека который не видел"
    s "Не считая меня"
    m "Денис{w} не видел свой член"
    s "ظنّين دائماً أن هناك شيء ليس على ما ي"
    s "Ладно заходим"
    hide pm
    hide ps
    with dissolve
    "Вы подошли к двери"
    "Саша попробывал открыть дверь"
    "Дверь была заперта"
    s "бл, и что делать"
    show ps smile at left
    show pm da at right
    with dissolve
    m "Не знаю"
    m "Похоже бог покинул нас"
    s "Пидарас"
    s "Тогда залезем по другому"
    menu cerkov:
        "Как попасть в церковь"
        "Выбирть окно":
            "Макс разбежался и выбил окно"
        "Чёрный вход":
            "Вы обошли церковь и зашли через чёрный вход"
        "Залесть через крышу":
            "Вы поднялись на крышу"
            "На крыше не было прохода"
            m "Пиздец"
            "Вы спустились в низ"
            menu cerkov2:
                "Как попасть в церковь"
                "Выбирть окно":
                    "Макс разбежался и выбил окно"
                "Чёрный вход":
                    "Вы обошли церковь и зашли через чёрный вход"
    scene black
    with fade
    "Вы наконец-то пробрались в церковь"
    "Божественая музыка.mp3 становилась всё громче и громче"
    # play music ...
    scene bg cerkovin
    with fade
    "В нутри была обычная церковь"
    show ps smile at left
    show pm da at right
    with dissolve
    m "И нахуйя мы сюда пробрались"
    s "Хуй знает"
    s "Больше не было мест куда можно было пойти"
    s "Разве что избить ангела"
    $ renpy.notify("Вам доступно новое действие")
    m "Ладно{w}, давай осмотримся здесь"
    show u
    with Dissolve(3)
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    u "{bt=3}Что вы здесь забыли?{/bt}"
    m "Почему церковь не закрыта?"
    u "{bt=3}Эм..{w} так как я недавно стала{w} великим{w} божеством{/bt}"
    u "{bt=3}То и религию ещё не создала{/bt}"
    u "{bt=3}Так что смысла в церкви нету{/bt}"
    s "Как ты стала великим{w} божеством"
    u "{bt=3}Не важно{/bt}"
    u "{bt=3}Меня выбрали люди{/bt}"
    u "{bt=3}Мне нужна ваша помощь{/bt}"
    u "{bt=3}Поможете мне?{/bt}"
    menu boghelp:
        "Помочь великому божеству?"
        "Нам всё равно не чем занятся":
            pass
        "Мы не хотим тебе помогать":
            u "{bt=3}а..{/bt}"
            u "{bt=3}Значит я ошиблась когда отправила вас в рай{/bt}"
            scene ending u
            with fade
            pause 1.5
            show lolidance
            $ ending("Умереть от великое божество")
            "Вы не захотели помогать великому божеству"
            "Возможно это было не лучшее решение"
            "[end_message]"
            return
    u "{bt=3}Отлично!{/bt}"
    s "Чем тебе надо помочь?"
    m "Мы готовы оставлять закладки мефедрона"
    u "{bt=3}Могла бы я выбрать других..{/bt}"
    u "{bt=3}И так{/bt}"
    hide u
    show lolidance
    u "{bt=3}В моём мире появился король деманов{/bt}"
    u "{bt=3}Ваша задача отправиться{w} и отпиздить его нахуй{/bt}"
    u "{bt=3}Да{w}, он меня заебал{/bt}"
    u "{bt=3}Так что я разрешаю вам делать всё что хотите{/bt}"
    u "{bt=3}Но уебите эту гниду{/bt}"
    u "{bt=3}Ваше приключение{w} будет именить название..{/bt}"
    bb "{bt=3}Эпическая сага о бескрайних приключениях Макса и Саши{w}\nв многомерном мире{w}, где они перерождаются снова и снова{w}\nоткрывая новые грани своих судебных циклов и сталкиваясь \nс бесчисленными вызовами{w}, погружаясь в уникальные реальности{w}, полные\n магии{w}, тайн и волнующих событий{w}, под названием\n 'Макс и Саша{w}: Реинкарнация в бескрайних\n измерениях и вечных временах{w}, где каждое воплощение — новое приключение{w}, а каждая\n судьба — загадка{w}, разгадываемая лишь через исследование\n бескрайних возможностей вечности'.{/bt}"
    s "nigger"
    m "Ебать название"
    u "Кто{w} из вас{w} будет главным героем"
    menu gg:
        "Выбрать главного героя(Только в боях, уник магия, фразы)"
        "Саша - Главный герой | Макс - Друг гг":
            $ ggName = "Саша"
            $ name = "Саша"
            $ img_player = "sasha"
            $ a.name = name
            $ a.skills = [doubleattack]
            call load_monsters
            call load_items
            $ party_list = [maks, sanek, lox]
            $ wild_monsters = [mon1,mon2]
            $ restorehp()
            $ restoremp()
            u "{bt=3}Отличный выбор!{/bt}"
            u "{bt=3}Саша, отныне ты должен со своим другом отпиздить короля демонов{/bt}"
            u "{bt=3}Управлять всем будеш ты{/bt}"
            u "{bt=3}Давай я покажу тебе как всё работает{/bt}"
            scene maprev
            with fade
            u "{bt=3}Перед тобой карта города{/bt}"
            $ persistent.main_menu = "gui/main_menu_ch_1_2.png"
            $ config.main_menu_music = "music/battle_in_aries_peak.mp3"
            $ renpy.notify("Загляни в гавное меню)")
            u "{bt=3}Здесь есть места которые ты можешь посетить{/bt}"
            u "{bt=3}Белые места - оносительно безопасные места{/bt}"
            u "{bt=3}Красные - места где на тебя могут напасть{/bt}"
            u "{bt=3}Не советую туда ходить{/bt}"
            show screen world_time
            u "{bt=3}С лева с верху показано время{/bt}"
            $ addTime()
            u "{bt=3}Следи за ним и не ходи ночью{/bt}"
            $ addTime()
            u "{bt=3}Я ограничила некоторые локации в разное время{/bt}"
            $ addTime()
            u "{bt=3}Что же, дальше ты сам{/bt}"
            $ addTime()
            u "{bt=3}Одолей короля демонов и спаси этот мир!{/bt}"
            show screen map
            ''  
        "Макс - Главный герой | Саша - Друг гг":
            $ ggName = "Макс"
            $ player1 = {
                "name": "Макс",
                "sprites": {
                    "fight": "images/pixel/pm talk.png",
                    "talk": "images/pixel/pm talk.png",
                },
                "stats": {
                    "magic": [
                        "maks"
                    ],
                    "weapons": [
                        "fists"
                    ],
                },
                "backpack": [],
            }
            $ player2 = {
                "name": "Саша",
                "sprites": {
                    "fight": "images/pixel/pm talk.png",
                    "talk": "images/pixel/pm talk.png",
                },
                "stats": {
                    "magic": [
                        "sasha"
                    ],
                    "weapons": [
                        "fists"
                    ],
                },
                "backpack": [],
            }
            
            #block of code to run
        
    ''
    return