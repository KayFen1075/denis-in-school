# characters
define m = Character('Макс', color="#3cef5d", image="m", callback=name_callback, cb_name="m")
define s = Character('Саша', color="#543cef", image="s", callback=name_callback, cb_name="s")
define d = Character('Денис', color="#e41010", image="d", callback=name_callback, cb_name="d")
define k = Character('Кирилл', color="#9610e4", image="k", callback=name_callback, cb_name="k")
define u = Character('Бог Юй', color="#e410c4", image="u", callback=name_callback, cb_name="u")
define x = Character('Санёк', color="#df9921", image="x", callback=name_callback, cb_name="x")
define b = Character('Борис', color="#a921df", image="b", callback=name_callback, cb_name="b")

define bb = Character('Бог Юй', color="#e410c4", kind=nvl)

# persistent
default persistent.endings = []
default persistent.main_menu = "gui/main_menu.png"
default persistent.hight_level = 1

# config
define config.main_menu_music = "music/disco.mp3"

init python:
    # info
    count_endings = 4
    end_message = f"Вы прошли {len(persistent.endings)} концовку из {count_endings}!"

    # запись действий
    kHelp = False
    FigthPoints = 0
    mogila_borisa = False
    ch_1_dialog_ms = False
    student = False
    matras = False
    first_barmen = False
    barmen = False
    first_pola = False
    maxim = False

    # in game
    game_time = 12
    maxHP = 100
    xp = 0
    needXp = 50
    cash = 0
    level = 1
    ggName = None
    player1 = {
        "name": None,
        "sprites": {
            "fight": "images/pixel/pm talk.png",
            "talk": "images/pixel/pm talk.png",
        },
        "stats": {
            "magic": [],
            "weapons": [],
        },
        "backpack": [],
    }
    player2 = {
        "name": None,
        "sprites": {
            "fight": "images/pixel/pm talk.png",
            "talk": "images/pixel/pm talk.png",
        },
        "stats": {
            "magic": [],
            "weapons": [],
        },
        "backpack": [],
    }

    # functions
    def ending(name):
        if name not in persistent.endings:
            renpy.notify(f'Вы открыта новая концовка {name}')
            persistent.endings.append(name)
    def addTime():
        global game_time
        game_time = (game_time % 24) + 6 
        print(game_time)
    def nameGG():
        global player1
        return player1.name

    def fontPixel():
        gui.text_font = "fonts/YourFontFile.ttf"
        
    # scripts

'''
Пример концовки

scene denis
with fade
pause 1.5
$ ending("Умереть от Дениса")
"Вы слишком слабенькие что бы убежать от Дениса.."
"[end_message]"
'''

