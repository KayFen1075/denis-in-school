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
define r = Character('', color="#292929", image="b", callback=name_callback, cb_name="b") # gotov

# persistent
default persistent.difficulty = 1

## Статистика
default persistent.new_games = 1
default persistent.reset_games = 0

## Знакомство с персонажими 
default persistent.remember_m = True
default persistent.remember_s = True
default persistent.remember_d = False
default persistent.remember_k = False
default persistent.remember_u = False
default persistent.remember_x = False
default persistent.remember_t = False
default persistent.remember_z = False
default persistent.remember_l = False
default persistent.remember_b = False

default persistent.first_game = True
default persistent.selected_u = None
default persistent.endings = []
default persistent.one_webhook_messages = []
default persistent.main_menu = "gui/main_menu.png"
default persistent.first_run = True
default persistent.angels_pizdet = False
default persistent.user_name = "Не указанно"
default persistent.main_menu_music = "music/disco.mp3"
default persistent.secret_code = True
default persistent.end_game = False

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
    import time;
    from discord_webhook import DiscordWebhook 
    # info
    count_endings = 6
    end_message = f"Вы прошли {len(persistent.endings)} концовку из {count_endings}!"

    # запись действий
    first_game = True
    bb = 1
    kHelp = False
    FigthPoints = 0
    LoliAnswers = 0
    love_points = 0
    wait_most = 0

    max_level = 12
    fights_left_les = 3
    fights_left_dan = 3
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
    ui_viev_bag = False
    ui_viev_equipment = False
    first_libriary = False
    maxim = False
    autohil = False
    # in game
    game_time = 12
    cost_multiplate = 1
    otpizdeli_denisa = 0
    obs_sworlds = 0
    friend = 0
    first_code = False

    type_battle = "none"
    talk_1taras = False

    win_1les = False
    first_win1les = False
    first_by_item = False
    talk_1tank = False
    action_1tank = False
    talk_1sanek = False
    talk_1maxim = False

    win_2les = False
    first_win2les = False
    talk_2sanek = False
    talk_2maxim = False # +maksim
    talk_1boris = False

    win_3les = False
    first_win3les = False
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
    first_win1dan = False
    first_dan = False
    first_win1dan = False
    talk_4sanek = False
    talk_1sasha = False

    win_2dan = False
    first_win2dan = False
    talk_5sanek = False
    talk_3boris = False
    talk_3kirill = False

    win_3dan = False
    first_win3dan = False
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
    
    one_events = []
    
    # functions
    def ending(name):
        if name not in persistent.endings:
            if name == "Умереть от Дениса":
                ach_die_with_denis.grant()
            if name == "Умереть от великое божество":
                ach_ui.grant()
            persistent.endings.append(name)
            renpy.notify(f'Открыта новая концовка {name}')
            DiscordMessage("**{0}** открыл новую концовку `{1}`!\nПройдено концовок: {2} из {3}".format(persistent.user_name, name, len(persistent.endings), count_endings))
    def OneDiscordMessage(m):
        if m not in persistent.one_webhook_messages:
            persistent.one_webhook_messages.append(m)
            DiscordMessage(m)
    def OneEventCheck(e):
            if e not in one_events:
                one_events.append(e)
                return True
            return False
    def DiscordMessage(m):
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1179025849857626152/0xNjeYYuHaeT8DF1xiv_CnO3lRf_YKeiPlGuUmeGBOw_ffZLEVJEzby2DJeCdT6QTMWE", content=m, username=persistent.user_name)
        response = webhook.execute()
    def addTime():
        global game_time, fights_left_les, fights_left_dan
        fights_left_les = min(fights_left_les+1,3)
        fights_left_dan = min(fights_left_dan+1,3)
        game_time = (game_time % 24) + 6 
        print(game_time)
    
    def random_choise(shanc):
        i = random.randint(1, shanc)
        return i == 1
    # Скрипты

# Эффекты

init python:
    close_eye = ImageDissolve("eye", 2.0, 20, reverse=True)
    open_eye = ImageDissolve("eye", 2.0, 20, reverse=False)
    
label horror_effect():
    show layer master:
        align (.5, .5)
        parallel:
            easein 6 zoom 1.08
            easein 6 zoom 1.03
            repeat
        parallel:
            1.
            block:
                block:
                    linear .02 xoffset 2
                    linear .02 xoffset -2
                    repeat 6
                .5
            repeat
        parallel:
            linear .02 matrixcolor BrightnessMatrix(-0.1)
            linear .02 matrixcolor BrightnessMatrix(-0.12)
            linear .02 matrixcolor BrightnessMatrix(-0.11)
            linear .02 matrixcolor BrightnessMatrix(-0.14)
            linear .02 matrixcolor BrightnessMatrix(-0.13)
            linear .02 matrixcolor BrightnessMatrix(-0.16)
            linear .02 matrixcolor BrightnessMatrix(-0.13)
            linear .02 matrixcolor BrightnessMatrix(-0.14)
            linear .02 matrixcolor BrightnessMatrix(-0.11)
            linear .02 matrixcolor BrightnessMatrix(-0.12)
            repeat
    return

label end_horror_effect():
    show layer master:
        matrixcolor BrightnessMatrix(0)
        parallel:
            easein 8 zoom 1.0
        parallel:
            linear 8 matrixcolor BrightnessMatrix(0.0)
    return

label restoreos():
    $ fights_left_les = 3
    $ fights_left_dan = 3
    return

label unstoreos():
    $ fights_left_les = 0
    $ fights_left_dan = 0
    return

label splashscreen:
    if not renpy.exists('characters/maks.char') or not renpy.exists('characters/sasha.char') and renpy.windows:
        scene bg shcool
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
        m "И за эти 3 раза пропал{w=1.5}{nw}"
        if not renpy.exists('characters/sasha.char') and not renpy.exists('characters/maks.char'):
            m "Пропал{w=0.6}и мы{w=0.5}{nw}"
            scene whitle with fade
            $ renpy.movie_cutscene('videos/0423.mpg') 
            $ renpy.quit()
        if not renpy.exists('characters/maks.char'):
            m "Пропал{w=0.6} я{w=0.5}{nw}"
            scene whitle with fade
            $ renpy.movie_cutscene('videos/0423.mpg') 
            $ renpy.quit()
        if not renpy.exists('characters/sasha.char'):
            m "Пропал{w=0.6} ты{w=0.5}{nw}"
            scene whitle with fade
            $ renpy.movie_cutscene('videos/0423.mpg') 
            $ renpy.quit()
    $ renpy.movie_cutscene('videos/black.mpg')
    define config.main_menu_music = persistent.main_menu_music
    if persistent.first_run == True:
        $ from discord_webhook import DiscordWebhook
        $ OneDiscordMessage("Кто-то в первые запусти игру")
        play music battle3
        scene bg angels
        with fade
        voice m0001
        m "Добро пожаловать в ебейшую визуальную новелу"
        voice m0002
        m "Сейчас будет один вопрос{w=1.4}, ВАЖНО ОТВЕТИТЬ ЧЕСТНО!"
        $ persistent.endings = []
        $ persistent.user_name = renpy.input("Как тебя зовут в реальности? (Это важно!!!)", length=32).title()
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
            voice d0001
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
            voice x0001
            x "ААА ЖЕНЩИНА"
            l "ААА ЖЕНЩИНА"
            voice d0002
            d "ААА ЖЕНЩИНА"
            u "а что тут такого?"
        voice m0026
        m "Привет [persistent.user_name]!{w=1.6} твоё имя будет использовано для статистики. {w=2.6}Её можно будет посмотреть в дискорде."
        voice m0026b
        m "Выбери сложность игры"
        menu difficulty_menu:
            "[persistent.user_name] какую-же сложность ты выберишь?"
            "Сложно\n{sc}БДСМ с Денисом{/sc}":
                call hard_config
            "Средняя\n{rotat=60}Обычная классика{/rotat}":
                call norm_config
            "Лёгкая\n{b}LGBT++++++++{/b}":
                call easy_config
        voice s0015
        s "Приятной дрочке!"
        $ persistent.first_run = False
        $ webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1179025849857626152/0xNjeYYuHaeT8DF1xiv_CnO3lRf_YKeiPlGuUmeGBOw_ffZLEVJEzby2DJeCdT6QTMWE", content="Это же **{0}**!".format(persistent.user_name))
        $ response = webhook.execute()
    scene black
    with fade

label prefSpeed(on=False):
    if on:
        $ see_attack_speed = 0.3
        $ attack_speed = 0.2
        return
    else:
        $ see_attack_speed = 1
        $ attack_speed = 0.7
        return
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
