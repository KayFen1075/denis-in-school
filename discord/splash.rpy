label after_load:
    $ print('after_load')
    if discordrun:
        python:
            try:
                import io
                import os
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                import io
                open("game/state.txt", 'w+')
                io.open("game/state.txt", 'w+', encoding = "utf-8").write("err3")
                state = "err3"
return

label before_main_menu:
    $ print('before_main_menu')
    if discordrun:
        python:
            import io
            state = "mm"
            io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
return

label quit:
    $ print('before_main_menu')
    if discordrun:
        python:
            import os
            os.popen('taskkill /f /im python.exe')
    return