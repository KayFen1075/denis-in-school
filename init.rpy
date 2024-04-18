# characters
define m = Character('Макс', color="#3cef5d", voice_tag="m", image="m", callback=name_callback, cb_name="m") # soon
define s = Character('Саша', color="#543cef", voice_tag="s", image="s", callback=name_callback, cb_name="s") # soon
define d = Character('Денис', color="#e41010", image="d", callback=name_callback, cb_name="d") # 50/50
define k = Character('Кирилл', color="#ec32df", voice_tag="k", image="k", callback=name_callback, cb_name="k") # 50/50
define u = Character('Бог Юй', color="#e410c4", image="u", callback=name_callback, cb_name="u") # xz
define x = Character('Санёк', color="#df9921", image="x", callback=name_callback, cb_name="x") # xz
define t = Character('Тянка', color="#f68ccd", image="t", callback=name_callback, cb_name="t") # xz
define z = Character('Тарас', color="#eee44b", image="z", callback=name_callback, cb_name="z") # gotov
define l = Character('Любимый', color="#c31414", image="l", callback=name_callback, cb_name="l") # soon
define b = Character('Борис', color="#a921df", image="b", callback=name_callback, cb_name="b") # gotov

# persistent
default persistent.first_game = True
default persistent.selected_u = None
default persistent.endings = []
default persistent.one_webhook_messages = []
default persistent.new_games = 1
default persistent.reset_games = 0
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
    autohil = False
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
    final_battle = False
    action_ostavit_borisa = False
    
    # functions
    def ending(name):
        if name not in persistent.endings:
            global DiscordWebhook
            persistent.endings.append(name)
            renpy.notify(f'Открыта новая концовка {name}')
            DiscordMessage("**{0}** открыл новую концовку `{1}`!\nПройдено концовок: {2} из {3}".format(persistent.user_name, name, len(persistent.endings), count_endings))
    def OneDiscordMessage(m):
        if m not in persistent.one_webhook_messages:
            persistent.one_webhook_messages.append(m)
            DiscordMessage(m)

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
        voice m0001
        m "Добро пожаловать в ебейшую визуальную новелу"
        voice m0002
        m "Сейчас будет один вопрос{w}, ВАЖНО ОТВЕТИТЬ ЧЕСТНО!"
        $ persistent.endings = []
        $ persistent.user_name = renpy.input("Как тебя зовут в реальности? (Это важно!!!)", length=32)
        if persistent.user_name.casefold() == "денис" or persistent.user_name.casefold() == "даун" or persistent.user_name.casefold() == "аутист" or persistent.user_name.casefold() == "уебан":
            voice m0003
            m "Оу"
            voice m0004
            m "Денис?"
            voice s0001
            s "Если сможешь пройти игру 3 раза с определёнными условиями то получишь прикольчик"
            voice m0005
            m "Так что удачи)"
        elif persistent.user_name.casefold() == "макс":
            voice m0006
            m "Какие люди"
            voice m0007
            m "Тайлер дёрнул"
            voice s0002
            s "Ты посмотри на этого далбоёба"
            voice m0008
            m "Та вообще пидр"
            voice k0026
            k "Я бы его трахнул"
        elif persistent.user_name.casefold() == "борис":
            voice m0009
            m "Борис{w} какое имя"
            voice s0003
            s "Уебанское"
            voice b0001
            b "Ахуели?"
            voice s0004
            s "Ух ебать"
            voice s0005
            s "Он в начальном экране говорит"
            voice m0010
            m "Я вахуи"
        elif persistent.user_name.casefold() == "кирилл" or persistent.user_name.casefold() == "лох":
            voice m0011
            m "Ты дождался своего бета теста)"
            voice s0006
            s "Кирилл предуприждаю"
            voice s0007
            s "Тебя будут так и так в игре"
            voice m0012
            m "Так что проходи только с резиновым членом в жопе"
        elif persistent.user_name.casefold() == "саша":
            voice s0008
            s "А кто же это"
            voice m0013
            m "Alexmantos"
            voice s0009
            s "Это блогодаря ему здесь 2 колабы"
        elif persistent.user_name.casefold() == "рома":
            voice m0014
            m "Могу сказать что тебя не будет в первой главе"
            voice m0015
            m "А вот во второй.."
            voice s0010
            s "Всё в переди!"
        elif persistent.user_name.casefold() == "тарас":
            voice m0016
            m "Можно менять название"
            voice s0011
            s "Титан в школе"
        elif persistent.user_name.casefold() == "максим" or persistent.user_name.casefold() == "любимый":
            voice m0017
            m "Любимый!"
            voice m0018
            m "Цколько лет цколько цим"
            voice s0012
            s "Ты про кого?"
        elif persistent.user_name.casefold() == "юй":
            voice m0019b
            m "А ты что тут забыла?"
            d "Я бы её трахнул сейчас"
        elif persistent.user_name.casefold() == "тянка":
            voice t0001
            t "Я же говорила что я реальна!"
            voice t0002
            t "Вот я выбралась и скачала эту игру"
        elif persistent.user_name.casefold() == "влад":
            voice m0019
            m "Вот и неведимка зашёл в игру"
            voice s0013
            s "Я здесь не кого не вижу"
        elif persistent.user_name.casefold() == "вадим":
            voice m0020
            m "Вадим?"
            voice m0021
            m "Тебя в первой главе нету"
            voice m0022
            m "Но можешь появиться во второй)"
        elif persistent.user_name.casefold() == "илья":
            voice m0023
            m "Тебе игра понравиться"
            voice m0024
            m "Здесь можно поиграть в мортал комбат"
        elif persistent.user_name.casefold() == "аня" or persistent.user_name.casefold() == "катя":
            voice m0025 # ЗАПИСАТЬ
            m "ААА ЖЕНЩИНА"
            voice k0027
            k "ААА ЖЕНЩИНА"
            voice s0014 # ЗАПИСАТЬ
            s "ААА ЖЕНЩИНА"
            voice b0002
            b "ААА ЖЕНЩИНА"
            voice z0001
            z "ААА ЖЕНЩИНА"
            x "ААА ЖЕНЩИНА"
            l "ААА ЖЕНЩИНА"
            d "ААА ЖЕНЩИНА"
            u "а что тут такого?"
        voice m0026
        m "Привет [persistent.user_name]!{w} твоё имя будет использовано для статистики. {w}Её можно будет посмотреть в дискорде."
        voice s0015 # ЗАПИСАТЬ
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
