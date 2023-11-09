define m = Character('Макс', color="#3cef5d")
define s = Character('Саша', color="#543cef")
define d = Character('Денис', color="#e41010")
define k = Character('Кирилл', color="#9610e4")
define b = Character('Бог Юй', color="#e410c4")

default persistent.endings = []
default persistent.main_menu = "gui/main_menu.png"

init python:
    # info
    count_endings = 2
    end_message = f"Вы прошли {len(persistent.endings)} концовку из {count_endings}!"

    # in game
    kHelp = False
    FigthPoints = 0 
    
    # functions
    def ending(name):
        if name not in persistent.endings:
            renpy.notify(f'Новая концовка {name}')
            persistent.endings.append(name)

    def fontPixel():
        gui.text_font = "fonts/YourFontFile.ttf"
        
    # scripts

'''
Пример концовки

scene denis
with fade
pause 1.5
$ endig("Умереть от Дениса")
"Вы слишком слабенькие что бы убежать от Дениса.."
"[end_message]"
'''

