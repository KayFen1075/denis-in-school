# characters
define m = Character('Макс', color="#3cef5d", image="m", callback=name_callback, cb_name="m")
define s = Character('Саша', color="#543cef", image="s", callback=name_callback, cb_name="s")
define d = Character('Денис', color="#e41010", image="d", callback=name_callback, cb_name="d")
define k = Character('Кирилл', color="#ec32df", image="k", callback=name_callback, cb_name="k")
define u = Character('Бог Юй', color="#e410c4", image="u", callback=name_callback, cb_name="u")
define x = Character('Санёк', color="#df9921", image="x", callback=name_callback, cb_name="x")
define t = Character('Тянка', color="#f68ccd", image="t", callback=name_callback, cb_name="t")
define z = Character('Тарас', color="#eee44b", image="z", callback=name_callback, cb_name="z")
define l = Character('Любимый', color="#c31414", image="l", callback=name_callback, cb_name="l")
define b = Character('Борис', color="#a921df", image="b", callback=name_callback, cb_name="b")


# persistent
default persistent.endings = []
default persistent.main_menu = "gui/main_menu.png"
default persistent.hight_level = 1
default persistent.first_run = True
default persistent.angels_pizdet = False
default persistent.user_name = "Не указанно"
default persistent.main_menu_music = "music/disco.mp3"
default persistent.secret_code = True

# Имена для входа
default persistent.denis = "?"
default persistent.sasha = "?"
default persistent.lox = "?"
default persistent.maks = "?"

image bronze_sworld:
    xsize 50 ysize 50
    "images/inv/bronze_sworld.png"
    # size 50px
# config

init python:
    from discord_webhook import DiscordWebhook
    # info
    count_endings = 6
    end_message = f"Вы прошли {len(persistent.endings)} концовку из {count_endings}!"

    # запись действий
    bb = 1
    kHelp = False
    FigthPoints = 0
    LoliAnswers = 0
    love_points = 0
    wait_most = 0

    max_level = 12
    see_attack_speed = 1
    attack_speed = 0.7
    kill_speed = 1

    mogila_borisa = False
    ch_1_dialog_ms = False
    student = False
    matras = False
    first_barmen = False
    barmen = False
    first_pola = False
    first_libriary = False
    maxim = False
    # in game
    game_time = 12
    cost_multiplate = 1
    otpizdeli_denisa = 0
    friend = 0
    first_code = False

    type_battle = "none"
    talk_1taras = False

    win_1les = False
    talk_1tank = False
    action_1tank = False
    talk_1sanek = False
    talk_1maxim = False

    win_2les = False
    talk_2sanek = False
    talk_2maxim = False # +maksim
    talk_1boris = False

    win_3les = False
    talk_2tank = False
    talk_3sanek = False
    talk_2tank = False
    talk_1denis = False # -friend
    talk_3tank = False  # +tank

    win_4les = False # +lox
    first_win4les = False
    talk_1kirill = False
    talk_2kirill = False
    talk_2boris = False

    win_1dan = False # +friend
    first_dan = False
    first_win1dan = False
    talk_4sanek = False
    talk_1sasha = False

    win_2dan = False
    talk_5sanek = False
    talk_3boris = False
    talk_3kirill = False

    win_3dan = False
    talk_4boris = False
    talk_3maxim = False
    talk_2sasha = False
    
    win_4dan = False #
    first_win4dan = False
    talk_2taras = False
    talk_4maxim = False
    talk_3tank = False
    talk_6sanek = False
    talk_5boris = False
    talk_3sasha = False
    talk_5maxim = False

    win_denis = False
    action_ostavit_borisa = False
    
    # functions
    def ending(name):
        if name not in persistent.endings:
            global DiscordWebhook
            persistent.endings.append(name)
            renpy.notify(f'Открыта новая концовка {name}')
            DiscordMessage("**{0}** открыл новую концовку `{1}`!\nПройдено концовок: {2} из {3}".format(persistent.user_name, name, len(persistent.endings), count_endings))
    def DiscordMessage(m):
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1179025849857626152/0xNjeYYuHaeT8DF1xiv_CnO3lRf_YKeiPlGuUmeGBOw_ffZLEVJEzby2DJeCdT6QTMWE", content=m)
        response = webhook.execute()
    def addTime():
        global game_time
        game_time = (game_time % 24) + 6 
        print(game_time)
    
    def random_choise(shanc):
        i = random.randint(1, shanc)
        return i == 1

    # scripts

label splashscreen:
    $ renpy.movie_cutscene('videos/black.mpg')
    define config.main_menu_music = persistent.main_menu_music
    if persistent.first_run == True:
        $ from discord_webhook import DiscordWebhook
        play music battle3
        scene bg angels
        with fade
        m "Добро пожаловать в ебейшую визуальную новелу"
        m "Сейчас будет один вопрос{w}, ВАЖНО ОТВЕТИТЬ ЧЕСТНО!"
        $ persistent.endings = []
        $ persistent.user_name = renpy.input("Как тебя зовут в реальности? (Это важно!!!)", length=32)
        if persistent.user_name.casefold() == "денис" or persistent.user_name.casefold() == "даун" or persistent.user_name.casefold() == "аутист" or persistent.user_name.casefold() == "уебан":
            m "Оу"
            m "Денис?"
            s "Если сможешь пройти игру 3 раза с определёнными условиями то получишь прикольчик"
            m "Так что удачи)"
        elif persistent.user_name.casefold() == "макс":
            m "Какие люди"
            s "Ты посмотри на этого далбоёба"
            m "Та вообще пидр"
            k "Я бы его трахнул"
        elif persistent.user_name.casefold() == "борис":
            m "Борис{w} какое имя"
            s "Уебанское"
            b "Ахуели?"
            s "Ух ебать"
            s "Он в начальном экране говорит"
            m "Я вахуи"
        elif persistent.user_name.casefold() == "кирилл" or persistent.user_name.casefold() == "лох":
            m "Ты дождался своего бета теста)"
            s "Кирилл предуприждаю"
            s "Тебя будут так и так в игре"
            m "Так что проходи только с резиновым членом в жопе"
        elif persistent.user_name.casefold() == "саша":
            s "А кто же это"
            m "Alexmantos"
            s "Это блогодаря ему здесь 2 колабы"
        elif persistent.user_name.casefold() == "рома":
            m "Могу сказать что тебя не будет в первой главе"
            m "А вот во второй.."
            s "Всё в переди!"
        elif persistent.user_name.casefold() == "тарас":
            m "Можно менять название"
            s "Титан в школе"
        elif persistent.user_name.casefold() == "максим" or persistent.user_name.casefold() == "любимый":
            m "Любимый!"
            m "Цколько лет цколько цим"
            s "Ты про кого?"
        elif persistent.user_name.casefold() == "юй":
            m "А ты что тут забыла?"
            d "Я бы её трахнул сейчас"
        elif persistent.user_name.casefold() == "тянка":
            t "Я же говорила что я реальна!"
            t "Вот я выбралась и скачала эту игру"
        elif persistent.user_name.casefold() == "влад":
            m "Вот и неведимка зашёл в игру"
            s "Я здесь не кого не вижу"
        elif persistent.user_name.casefold() == "вадим":
            m "Вадим?"
            m "Тебя в первой главе нету"
            m "Но можешь появиться во второй)"
        elif persistent.user_name.casefold() == "илья":
            m "Тебе игра понравиться"
            m "Здесь можно поиграть в мортал комбат"
        elif persistent.user_name.casefold() == "аня" or persistent.user_name.casefold() == "катя":
            m "ААА ЖЕНЩИНА"
            k "ААА ЖЕНЩИНА"
            s "ААА ЖЕНЩИНА"
            b "ААА ЖЕНЩИНА"
            z "ААА ЖЕНЩИНА"
            x "ААА ЖЕНЩИНА"
            l "ААА ЖЕНЩИНА"
            d "ААА ЖЕНЩИНА"
            u "а что тут такого?"
        m "Привет [persistent.user_name]!{w} твоё имя будет использовано для статистики. {w}Её можно будет посмотреть в дискорде."
        s "Приятной дрочке!"
        $ persistent.first_run = False
        $ webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1179025849857626152/0xNjeYYuHaeT8DF1xiv_CnO3lRf_YKeiPlGuUmeGBOw_ffZLEVJEzby2DJeCdT6QTMWE", content="**{0}** в первые запустил игру!".format(persistent.user_name))
        $ response = webhook.execute()
    scene black
    with fade

label prefSpeed(on=False):
    if on:
        $ print('speed')
        $ see_attack_speed = 0.3
        $ attack_speed = 0.2
    else:
        $ print('slow')
        $ see_attack_speed = 1
        $ attack_speed = 0.7
    return
#'''
#Пример концовки
#
#scene denis
#with fade
#pause 1.5
#$ ending("Умереть от Дениса")
#"Вы слишком слабенькие что бы убежать от Дениса.."
#"[end_message]"
#'''
