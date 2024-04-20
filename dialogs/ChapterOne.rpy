label deadw:
    scene main_menu_ch_1
    with fade
    pause(3)
 
    $ narrator = Character(what_style="pixel_say_dialogue", narrator=True) # soon

    $ m = Character('Макс', color="#3cef5d", voice_tag="m", who_style="style_pm_label", what_style="style_pm_dialogue", window_style="style_pm_back", image="m", callback=name_callback, cb_name="m") # soon
    $ s = Character('Саша', color="#543cef", voice_tag="s", who_style="style_ps_label", what_style="style_ps_dialogue", window_style="style_ps_back", image="s", callback=name_callback, cb_name="s") # soon
    $ d = Character('Денис', color="#e41010", voice_tag="d", image="d", who_style="style_pd_label", what_style="style_pd_dialogue", window_style="style_pd_back", callback=name_callback, cb_name="d") # 50/50
    $ k = Character('Кирилл', color="#ec32df", voice_tag="k", who_style="style_pk_label", what_style="style_pk_dialogue", window_style="style_pk_back", image="k", callback=name_callback, cb_name="k") # 50/50
    $ u = Character('Бог Юй', color="#e410c4", voice_tag="u", image="u", who_style="style_pu_label", what_style="style_pu_dialogue", window_style="style_pu_back", callback=name_callback, cb_name="u") # xz
    $ x = Character('Санёк', color="#df9921", voice_tag="x", image="x", who_style="style_px_label", what_style="style_px_dialogue", window_style="style_px_back", callback=name_callback, cb_name="x") # xz
    $ t = Character('Тянка', color="#f68ccd", voice_tag="t", image="t", who_style="style_pt_label", what_style="style_pt_dialogue", window_style="style_pt_back", callback=name_callback, cb_name="t") # xz
    $ z = Character('Тарас', color="#eee44b", voice_tag="z", image="z", who_style="style_pz_label", what_style="style_pz_dialogue", window_style="style_pz_back", callback=name_callback, cb_name="z") # gotov
    $ l = Character('Любимый', color="#c31414", voice_tag="l", image="l", who_style="style_pl_label", what_style="style_pl_dialogue", window_style="style_pl_back", callback=name_callback, cb_name="l") # soon
    $ b = Character('Борис', color="#a921df", voice_tag="b", image="b", who_style="style_pb_label", what_style="style_pb_dialogue", window_style="style_pb_back", callback=name_callback, cb_name="b") # gotov

    $ persistent.main_menu = "gui/main_menu_ch_1.png"
    $ persistent.main_menu_music = "music/BitWaves.wav"
    $ config.main_menu_music = "music/BitWaves.wav"
    $ renpy.notify("Загляни в главное меню")
    scene black
    play music "music/Do Not Run.mp3"
    with Fade(1, 10, 0.2, color="#ffff")
    scene bg sky
    "? ? ?" "Где я"
    "? ? ?" "Что произошло"
    "? ? ?" "Помню что на меня кто-то напал в спину.."
    "? ? ?" "Как будто со мной кто-то был"
    "? ? ?" "Почему я ни чего не чувствую"
    $ persistent.remember_u = True
    voice u0001
    u "{bt=3}Иди за мной{/bt}"
    "? ? ?" "Кто ты"
    $ denis_word_start_time = time.time()
    "{move}Д н е{/move}" "{i}{move}Начали двигаться{/move}{/i}"
    if time.time()-denis_word_start_time >= 35:
        play music iseeyou
        "{sc}Никогда{/sc}"
        "{sc}Не упоминай {size=+20}это{size=+50} имя{w=0.4}{nw}{/sc}"
        pause(1.4)
        "{sc}Ключ к тайне всегда был рядом{w=0.5}, как и он {w=0.1}ЗБВД{w=0.3}{nw}{/sc}"
        $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} зачем ты собрал его имя?".format(persistent.user_name))
        play music "music/Do Not Run.mp3"
        $ denis_word_start_time = time.time()*10000000 
    $ print(time.time()-denis_word_start_time)
    "? ? ?" "Что происходит"
    show u
    with dissolve
    with vpunch
    voice u0002
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    voice u0003
    u "{bt=3}Сейчас будет идти суд над вами всеми{/bt}"
    show u zov
    with vpunch
    voice u0004
    u "{bt=3}Так мы сможем понять куда вы попадёте{/bt}"
    show u dab
    with vpunch
    voice u0005
    u "{bt=3}Ад или рай{/bt}"
    "Наступило молчание"
    "Все ждали приговора"
    "Как вдруг"
    $ persistent.end_game = False
    if not persistent.end_game:
        jump adray
    menu kanon:
        "Пойти по канону или в соло"
        "Канон":
            menu adray:
                "Кому дать слово?"
                "[persistent.denis]":
                    if not persistent.end_game:
                        if persistent.selected_u != 1 and persistent.selected_u:
                            $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} загрузился, зачем?".format(persistent.user_name))
                            "Вы дали слово.."
                            hide u
                            with dissolve
                            "Вы дали слово [persistent.user_name]"
                            stop music
                            "Я знаю что ты сделал{w}, ты загрузился{w=0.4}{nw}"
                            play music iseeyou
                            pause(2)
                            "Больше так не делай{w=1}{nw}"
                            "Я слежу за тобой{nw}"
                            play music "music/Do Not Run.mp3"
                            show u dab
                            jump kanon
                    $ persistent.selected_u = 1
                    $ config.rollback_enabled = False
                    "Вы дали слово Денису"
                    $ config.rollback_enabled = True
                    "Возможно это было худшее решение{w} за всю игру"
                    d "Пошла нах.."
                    "Макс закрыл рот аутисту"
                    show u muha
                    with vpunch
                    voice u0006
                    u "{bt=3}Что же{w}, через тебя будет проходить суд{/bt}"
                    voice u0007
                    u "{bt=3}В зависимости от твоих ответов будет зависеть судьба вас всех{/bt}"
                    show u nag
                    with vpunch
                    voice u0008
                    u "{bt=3}И так{/bt}"
                    voice u0009
                    u "{bt=3}Лоли или милфы?{/bt}"
                    d "Лоли 9 лет"
                    hide u
                    show lolidance
                    pause(3)
                    u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0011
                    u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                    d "Секс-партнёр"
                    u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0012
                    u "{bt=20}Любишь меня?{/bt}"
                    d "Трахаю"
                    u "{bt=50}☠ ☠ ☠{/bt}"
                    voice u0014
                    u "{bt=3}Я посмотрела твоё дело..{/bt}"
                    voice u0015
                    u "{bt=3}То что ты делал при жизни это ужасно{w} так что{/bt}"
                    voice u0017
                    u "{bt=50}Я считаю{w} что{w} вы все{w} должны{w} попасть{w}...{/bt}"
                    with vpunch
                    u "{bt=3}{/bt}"
                    $ persistent.denis = "Денису"
                    voice u0018
                    u "В АД"
                    jump ad
                "[persistent.sasha]":
                    if not persistent.end_game:
                        if persistent.selected_u != 2 and persistent.selected_u:
                            $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} загрузился, зачем?".format(persistent.user_name))
                            "Вы дали слово.."
                            hide u
                            with dissolve
                            "Вы дали слово [persistent.user_name]"
                            stop music
                            "Я знаю что ты сделал{w}, ты загрузился{w=0.4}{nw}"
                            play music iseeyou
                            pause(2)
                            "Больше так не делай{w=1}{nw}"
                            "Я слежу за тобой{nw}"
                            play music "music/Do Not Run.mp3"
                            show u dab
                            jump kanon
                    $ persistent.selected_u = 2
                    $ config.rollback_enabled = False
                    "Вы дали слово Саше"
                    $ config.rollback_enabled = True
                    voice s0115
                    s "Ну давайте я отвечу"
                    show u muha
                    with vpunch
                    voice u0006
                    u "{bt=3}Что же{w}, через тебя будет проходить суд{/bt}"
                    voice u0007
                    u "{bt=3}В зависимости от твоих ответов будет зависеть судьба вас всех{/bt}"
                    show u nag
                    with vpunch
                    voice u0008
                    u "{bt=3}И так{/bt}"
                    voice u0009
                    u "{bt=3}Лоли или милфы?{/bt}"
                    voice s0116
                    s "Милфы естественно"
                    hide u
                    show lolidance
                    pause(2)
                    u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0011
                    u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                    voice s0117
                    s "Бля шо за вопросы"
                    voice s0118
                    s "Я тебя первый раз в жизни вижу"
                    m "Отвечай нормально еблан"
                    voice s0119
                    s "Ладно, пусть другом буду"
                    u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0012
                    u "{bt=20}Любишь меня?{/bt}"
                    voice s0120
                    s "28"
                    pause(1.0)
                    m "..."
                    m "Нам пизда"
                    u "{bt=50}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0014
                    u "{bt=3}Я посмотрела твоё дело..{/bt}"
                    voice u0020
                    u "{bt=3}Боже мой{/bt}"
                    voice u0016
                    u "{bt=3}Зачем ты выебал кошку Кирилла?{/bt}"
                    voice u0019
                    u "{bt=3}Ну ладно{w} это не педофилия{/bt}"
                    # voice uвставка
                    u "{bt=50}Я считаю{w} что{w} вы все{w} можете{w} попасть{w} в{w} рай{/bt}"
                    m "Ебать"
                    $ persistent.sasha = "Саше"
                    m "Как нахуй"
                    jump ray
                "[persistent.lox]":
                    if not persistent.end_game:
                        if persistent.selected_u != 3 and persistent.selected_u:
                            $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} загрузился, зачем?".format(persistent.user_name))
                            "Вы дали слово.."
                            hide u
                            with dissolve
                            "Вы дали слово [persistent.user_name]"
                            stop music
                            "Я знаю что ты сделал{w}, ты загрузился{w=0.4}{nw}"
                            play music iseeyou
                            pause(2)
                            "Больше так не делай{w=1}{nw}"
                            "Я слежу за тобой{nw}"
                            play music "music/Do Not Run.mp3"
                            show u dab
                            jump kanon
                    $ persistent.selected_u = 3
                    $ config.rollback_enabled = False
                    "Вы дали слово Кириллу"
                    $ config.rollback_enabled = True
                    voice k0028
                    k "Ладно, давайте я отвечу"
                    m "Не разрешаю"
                    voice k0029
                    k "Та иди нахуй"
                    show u muha
                    # voice uвставка
                    u "{bt=3}Ай ай ай{w}, какой плохой мальчик{/bt}"
                    # voice uвставка
                    u "{bt=3}На суде неприемлемо браниться{/bt}"
                    show u nag
                    with vpunch
                    voice u0006
                    u "{bt=3}Что же{w}, через тебя будет проходить суд{/bt}"
                    voice u0007
                    u "{bt=3}В зависимости от твоих ответов будет зависеть судьба вас всех{/bt}"
                    show u zov
                    with vpunch
                    voice u0008
                    u "{bt=3}И так{/bt}"
                    voice u0009
                    u "{bt=3}Лоли или милфы?{/bt}"
                    voice k0030
                    k "Милфы"
                    hide u
                    show lolidance
                    pause(3)
                    voice u0014
                    u "{bt=3}Я посмотрела твоё дело..{/bt}"
                    # voice uвставка
                    u "{bt=3}Зачем ты обрыгал всё что двигалось и не двигалось?{/bt}"
                    # voice uвставка
                    u "{bt=3}Ну ладно{/bt}"
                    u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0011
                    u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                    voice k0031
                    k "Я твой отчим и твой любовник"
                    u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0012
                    u "{bt=20}Любишь меня?{/bt}"
                    voice k0032
                    k "ОБОЖАЮ, когда попаду в рай то выебу тебя"
                    u "{bt=50}☠ ☠ ☠{/bt}"
                    voice u0017
                    # voice uвставка
                    u "{bt=50}Я считаю{w} что{w} вы все{w} должны{w} попасть{w}...{/bt}"
                    with vpunch
                    $ persistent.lox = "Кириллу"
                    voice u0018
                    u "В АД"
                    jump ad
                "[persistent.maks]":
                    if not persistent.end_game:
                        if persistent.selected_u != 4 and persistent.selected_u:
                            $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} загрузился, зачем?".format(persistent.user_name))
                            "Вы дали слово.."
                            hide u
                            with dissolve
                            "Вы дали слово [persistent.user_name]"
                            stop music
                            "Я знаю что ты сделал{w}, ты загрузился{w=0.4}{nw}"
                            play music iseeyou
                            pause(2)
                            "Больше так не делай{w=1}{nw}"
                            "Я слежу за тобой{nw}"
                            play music "music/Do Not Run.mp3"
                            show u dab
                            jump kanon

                    $ persistent.selected_u = 4
                    $ config.rollback_enabled = False
                    "Вы дали слово Максу"
                    $ config.rollback_enabled = True
                    m "Я знаю всё про неё, так что на вопросы отвечу правильно!"
                    show u muha
                    with vpunch
                    voice u0005
                    u "{bt=3}Что же{w}, через тебя будет проходить суд{/bt}"
                    voice u0006
                    u "{bt=3}В зависимости от твоих ответов будет зависеть судьба вас всех{/bt}"
                    show u nag
                    with vpunch
                    voice u0008
                    u "{bt=3}И так{/bt}"
                    voice u0009
                    u "{bt=3}Лоли или милфы?{/bt}"
                    m "Канечно{w} милфы"
                    hide u
                    show lolidance
                    pause(3)
                    u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0011
                    u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                    m "Для тебя я буду старшим братиком"
                    u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0012
                    u "{bt=20}Любишь меня?{/bt}"
                    m "Иди нахуй"
                    u "{bt=50}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                    voice u0014
                    u "{bt=3}Я посмотрела твоё дело..{/bt}"
                    u "{bt=3}Ты был фурри фем бойчиком{/bt}"
                    u "{bt=3}Так что{/bt}"
                    u "{bt=50}Я считаю{w} что{w} вы все{w} можете{w} попасть{w} в{w} рай{/bt}"
                    $ persistent.maks = "Максу"
                    jump ray
        "В соло" if persistent.end_game:
            if not persistent.end_game:
                if persistent.selected_u != 5 and persistent.selected_u:
                    $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} загрузился, зачем?".format(persistent.user_name))
                    "Вы дали слово.."
                    hide u
                    with dissolve
                    "Вы дали слово [persistent.user_name]"
                    stop music
                    "Я знаю что ты сделал{w}, ты загрузился{w=0.4}{nw}"
                    play music iseeyou
                    pause(2)
                    "Больше так не делай{w=1}{nw}"
                    "Я слежу за тобой{nw}"
                    play music "music/Do Not Run.mp3"
                    show u dab
                    jump kanon
            $ persistent.selected_u = 5
            $ config.rollback_enabled = False
            "Вы решили ответить сами"
            $ config.rollback_enabled = True
            show u muha
            voice u0006
            u "{bt=3}Что же{w}, через тебя будет проходить суд{/bt}"
            voice u0007
            u "{bt=3}В зависимости от твоих ответов будет зависеть судьба всех персонажей{/bt}"
            voice s0121
            s "С кем она говорит"
            voice k0033
            k "Хуй знает"
            show u zov
            with vpunch
            voice u0008
            u "{bt=3}И так{/bt}"
            voice u0009
            u "{bt=3}Лоли или милфы?{/bt}"
            menu loli:
                u "{bt=3}Лоли или милфы?{/bt}"
                "Лоли":
                    $ LoliAnswers -= 1
                    pass
                "Милфы":
                    $ LoliAnswers += 1
                    pass
            hide u
            show lolidance
            pause(3)
            u "{bt=3}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
            voice u0011
            u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
            menu kto:
                u "{bt=3}Кто ты для меня Братикк{w}, или друг?{/bt}"
                "Братик":
                    $ LoliAnswers += 2
                    pass
                "Сестра":
                    $ LoliAnswers += 1
                "Друг":
                    pass
                "Отчим":
                    $ LoliAnswers -= 1
            u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
            voice u0012
            u "{bt=20}Любишь меня?{/bt}"
            menu love:
                u "{bt=20}Любишь меня?{/bt}"
                "Нет":
                    pass
                "Да":
                    $ LoliAnswers += 1
                    pass
                "Хочу тебя трахнуть)))))))":
                    $ LoliAnswers -= 2
                    pass
                "Я по мальчикам":
                    u "{bt=10}Уважаю{/bt}"
                    pass
                "Хуй":
                    $ LoliAnswers -= 1
                    pass


            if LoliAnswers >= 3:                              
                u "{bt=10}❤️❤️↘️❤️❤️⬅️❤️❤️↗️❤️❤️❤️⬇️❤️❤️⬆️❤️❤️{/bt}"
                # voice uвставка
                u "{bt=50}Я считаю{w} что{w} вы все{w} должны{w} попасть{w} в рай{/bt}"
                voice s0122
                s "Что за хуйня только что была"
                m "Хз, но мы все летим в рай, поэтому кайф"
                jump ray
            else:
                u "{bt=50}☠ ☠ ☠{/bt}"
                # voice uвставка
                u "{bt=50}Я считаю{w} что{w} вы все{w} должны{w} попасть{w}...{/bt}"
                with vpunch
                u "В АД"
                voice s0123
                s "Ну вообще круто"
                m "Блять какого хуя, мы даже ни чего сказать не успели"
                jump ad
    return

label ad:
    $ OneDiscordMessage("# Начало Главы 1 😈\n{0} Отправляеться в АД".format(persistent.user_name))
    voice u0021
    u "{bt=3}Вы все отправляетесь в ад{/bt}"
    voice u0022
    u "{bt=3}Мучения и страдания будут преследовать всю всюду{/bt}"
    scene black
    with fade
    "Всё потемнело"
    play music "music/Cliffs.mp3"
    "Мы начали падать"
    "Куда-то глубоко в низ"
    "Был слышен только ветер"
    "И стоны Дениса"
    pause(2)
    voice k0034
    k "Я чувствую себя!"
    voice s0124
    s "Перестань дрочить даун"
    voice k0035
    k "Динах"
    m "Денис ты еблан?{w} Нахуй ты бога нахуй послал"
    d "Захотел"
    m "Ёбнутый даун"
    pause(1.5)
    "Не знаю сколько мы падали"
    d "Знаете{w} я бы её трахнул{w} и вас тоже"
    k "❤️❤️❤️"
    voice k0036
    k "Трахни труп"
    d "Иди ко мне"
    m "Я так понимаю все мы сдохли"
    voice s0125
    s "Думаю{w=1.6} возможно{w=1} я перебрал с мефедроном"
    voice k0037
    k "Хочешь покажу пенис?"
    "{i}Кирилл показал член{w=.4}, но не кто не увидел из-за темноты{w}(из-за размера){w=0.2}{nw}{/i}"
    m "Я могу представить как мы втроём сдохни"
    m "Но, {w}кто убил Дениса?"
    voice s0126
    s "Я думаю достаточно людей, которые хотели бы это сделать"
    "Вы услышали знакомую музыку"
    play music "music/Digital Roots.mp3"
    "Вокруг всё потемнело"
    voice k0038
    k "Я ебал мухомор"
    scene bg ad
    with fade
    "Перед вами было месиво из пикселей"
    "Словно понос Дениса"
    show pk auel
    with dissolve
    voice k0039
    k "Я не понимаю"
    voice k0040
    k "Почему мы все идём в ад{w}, из-за одного еблана"
    show pk auel at left
    with move
    show pd smile at right
    with dissolve
    d "Мне всё нравиться"
    d "Где все?"
    d "Почему здесь только мы"
    voice k0041
    k "Хороший вопрос"
    voice k0042
    k "Мы падали вместе"
    voice k0043
    k "Но в итоге ты оказался тяжелее"
    d "Получается и ты тоже"
    voice k0044
    k "Может Макс слишком много вопросов задавал"
    voice k0045
    k "И его отправили куда-то в другое место"
    d "Хз"
    d "Мне всё нравиться здесь{w}, иди ко мне мой сладенький"
    voice k0046
    k "Та блять иди нахуй"
    hide pk
    with moveoutleft
    "Кирилл начал убегать"
    d "Куда же ты"
    d "У нас есть целая вечность)"
    hide pd
    with moveoutleft
    "Денис побежал за ним"
    scene bg lesad
    with fade
    play music "music/Vitality.mp3"
    "Вы добежали до адского леса"
    "Кровавые листья свисали с древ"
    show u
    with hpunch
    voice u0023
    u "{bt=3}Стойте{/bt}"
    voice u0024
    u "{bt=3}Я же вам не рассказала про это место{/bt}"
    show pk dshentelmen at right
    with moveinright
    show pd at left
    with moveinright
    d "Тебя тоже трахнуть"
    voice u0025
    u "{bt=3}Не выйдет{/bt}"
    voice u0026
    u "{bt=3}В аду у меня защита от таких, как вы{/bt}"
    voice k0047
    k "Так что ты хотела нам рассказать"
    hide u
    show lolidance
    voice u0027
    u "{bt=3}Вообще м это ад{/bt}"
    d "Ахуеть{w}, а мы и не знали"
    voice u0028
    u "{bt=3}У него есть особенность{/bt}"
    voice u0029
    u "{bt=3}Раз в год происходит чистка грешников{/bt}"
    voice u0030
    u "{bt=3}Ангелы убийцы спускаются с небес\n и убивают по больше грешников{/bt}"
    voice k0048
    k "Круто"
    voice u0031
    u "{bt=3}И ещё{w} сегодня тот день{/bt}"
    voice u0032
    u "{bt=3}Так что да{/bt}"
    voice u0033
    u "{bt=3}Удачи{/bt}"
    hide lolidance
    with moveouttop
    voice k0049
    k "Э что"
    voice k0050
    k "Куда"
    d "Ну так что"
    d "Если нам пиздец"
    d "То давай"
    voice k0051
    k "Иди нахуй"
    hide pk
    with moveoutright
    d "Ну куда же ты"
    hide pd
    with moveoutright
    "Денис опять побежал за ним"
    scene bg city2ad
    with fade
    play music "music/pixel_sprinter_loop.mp3"
    "Вы прибежали в адский город"
    k "Ебать красиво"
    d "Ладно{w}, я потом тебя трахну"
    k "Может нам надо где-то спрятаться?"
    d "Можем{w} вломиться в чей-то дом{w} украсть детей{w} и занести их в мой подвал"
    k "Мне нравиться только первая часть"
    k "Идём в тот красивый район"
    scene black
    with fade
    "Вы отправились в тот район"
    d "Посмотри на верх"
    d "Ангелы в аду"
    k "Так и есть это они"
    k "Надо блять быстрее искать укрытие"
    scene bg cityad
    with fade
    "Вы пришли в адский район"
    d "Сколько же тут дитишек"
    k "Идём в этот незаметный домик"
    "Вы отправились"
    scene bg doorad
    with fade
    show pk sigma at left
    with moveinleft
    k "Здесь закрыто"
    k "Здесь вообще есть законы?"
    show pd see at right
    with moveinright
    d "Даже если и есть мне это не помешает воровать детей"
    k "Пиздец"
    d "У меня уже есть опыт по взлому дверей"
    show pd scream2 at center
    with move
    d "Так что это не проблема"
    "Денис начал взламывать дверь"
    pause(0.5)
    k "Ну что?"
    d "Не мешай"
    pause(0.5)
    k "Скажи просто что ты лох"
    d "Та блять"
    d "Тут замки другие"
    d "Адские"
    show pd see at right
    with move
    k "Знаешь{w} у меня появилась идея"
    k "Попробуй спереться об дверь"
    d "Ты ахуел?"
    d "В прочем это может сработать"
    show pd scream2 at center
    with move
    "Денис спёрся об дверь"
    pause(0.5)
    d "Не чего не происходит"
    k "Та подожди ты"
    d "Ладно"
    pause(0.5)
    "Дверь начала трескаться"
    "Под весом Дениса дверь не выдержала и разрушилась на атомы"
    k "О вот"
    d "Блять"
    scene black
    with fade
    play music "music/videoplayback.mp3"
    "Денис не выдержал и упал в пустоту"
    "Кирилл пошёл за ним следом"
    k "Пиздец здесь темно"
    "Кирилл начал икать, где включается свет"
    "В попытках найти свет он дотронулся до Денис"
    d "Хочешь прямо здесь?)"
    k "Иди нахуй{w}, ищи свет"
    d "Ладно я пойду дальше"
    "Вы продолжили искать свет"
    play sound "steklo.mp3"
    "Кирилл услышали звук разбитого стекла"
    k "Блять ты что наделал"
    "В ответ тишина"
    "Кирилл нашёл включатель света"
    scene bg roomad
    with fade
    show pk
    with moveinleft
    k "Пиздец"
    $ OneDiscordMessage("# Начало Главы 1 💀\nКирилл потерял Дениса")
    k "Этот еблан врезался в окно и упал с 15 этажа"
    k "За ним я точно прыгать не буду"
    pause(1.0)
    k "Интересно{w} чей это дом"
    play sound stuki
    "Кирилл услышал стуки в окно"
    k "Походу этот далбоёб зацепился"
    k "Пойду сброшу его"
    hide pk
    with dissolve
    "Кирилл подошёл к окну{w} и увидел ангела с копьём"
    k "Блять пиздец"
    "Кирилл отпрыгнул от окна"
    show pk stoika
    with moveinbottom
    k "Меня нашли что делать теперь"
    show pk stoika at left
    with move
    show u muha
    with moveintop
    voice u0034
    u "{bt=3}Ты что забыл у меня дома{/bt}"
    voice u0035
    u "{bt=3}Это священное место{/bt}"
    k "Но это же ад"
    hide u
    show lolidance
    voice u0036
    u "{bt=3}Так тихо{/bt}"
    k "И почему ты вообще живёшь в аду"
    voice u0037
    u "{bt=3}Я уже говорила что у меня неуязвимость в аду{/bt}"
    voice u0038
    u "{bt=3}Мне безопаснее здесь чем в раю{/bt}"
    voice u0039
    u "{bt=3}И ещё{w} за то что ты забрался в мой дом\n без разрешения{/bt}"
    voice u0040
    u "{bt=3}Я отправлю тебя в другой мир{/bt}"
    k "Там будут кошко девочки?"
    voice u0041
    u "{bt=3}Возможно{/bt}"
    k "Тогда я не против?"
    pause(1.0)
    voice u0042
    u "{bt=3}Мне пришло уведомление, что кто-то\n пробрался в мою райскую церковь{/bt}"
    voice u0043
    u "{bt=3}Я отойду не на долго{/bt}"
    hide lolidance
    with moveouttop
    pause(1.0)
    k "Я так понимаю ангелы не будут заходить в хоромы богини"
    k "Интересно что это за аниме мир"
    "Прошло 10 минут"
    show lolidance
    with moveintop
    voice u0044
    u "{bt=3}Вообще-м у тебя будет напарник{/bt}"
    voice u0045
    u "{bt=3}Он поможет тебе одолеть короля демонов{/bt}"
    voice u0046
    u "{bt=3}Выбери кого-то{/bt}"
    $ name = "Кирилл"
    $ img_player = "lox"
    $ a.name = name
    $ a.skills = [souldrain2]
    $ a.hpmax = 27
    menu maks_sasha:
        "Выбрать напарника"
        "Макс":
            $ OneDiscordMessage("# Начало Главы 1 👇\nВыбрать напарника:\n> `Макс`")
            $ friend = "maks"
            $ party_list = [maks]
            voice u0047
            u "{bt=3}Отлично!{/bt}"
            voice u0048
            u "{bt=3}Твоё приключение будет вместе с Максом{/bt}"
        "Саша":
            $ OneDiscordMessage("# Начало Главы 1 👇\nВыбрать напарника:\n> `Саша`")
            $ friend = "sasha"
            $ party_list = [sasha]
            voice u0047
            u "{bt=3}Отлично!{/bt}"
            voice u0049
            u "{bt=3}Твоё приключение будет вместе с Сашей{/bt}"
    call load_monsters from _call_load_monsters
    call load_items from _call_load_items
    $ restorehp()
    $ restoremp()
    voice u0050
    u "{bt=3}Но он появиться позже{/bt}"
    voice u0051
    u "{bt=3}А пока проведу для тебя обучение{/bt}"
    play music "music/epic loop.mp3"
    scene maprev
    with fade
    voice u0052
    u "{bt=3}Перед тобой карта города{/bt}"
    $ persistent.main_menu = "gui/main_menu_ch_1_2.png"
    $ persistent.main_menu_music = "music/battle_in_aries_peak.mp3"
    $ config.main_menu_music = "music/battle_in_aries_peak.mp3"
    $ renpy.notify("Загляни в главное меню)")
    voice u0053
    u "{bt=3}Здесь есть места которые ты можешь посетить{/bt}"
    voice u0054
    u "{bt=3}Белые места — относительно безопасные места{/bt}"
    voice u0055
    u "{bt=3}Красные — места где на тебя могут напасть{/bt}"
    voice u0056
    u "{bt=3}Не советую туда ходить{/bt}"
    show screen world_time
    voice u0057
    u "{bt=3}Сверху слева в правом нижнем углу показано время{/bt}"
    $ addTime()
    voice u0058
    u "{bt=3}Следи за ним и не ходи ночью{/bt}"
    $ addTime()
    voice u0059
    u "{bt=3}Я ограничила некоторые локации в разное время{/bt}"
    $ addTime()
    voice u0060
    u "{bt=3}Что же, дальше ты сам{/bt}"
    $ addTime()
    voice u0061
    u "{bt=3}Одолей короля демонов и спаси этот мир!{/bt}"
    scene bg dm_vhod
    with fade
    show pk dshentelmen
    with dissolve
    k "Где я оказался"
    show pk dshentelmen
    with move
    $ persistent.remember_l = True
    show pl at left
    with moveinleft
    l "Ты у меня дома"
    k "Максим?"
    scene black
    with fade
    k "Я познакомился с Борисом"
    k "Ещё со многими жителями этого города"
    k "Как оказалось Денис тоже здесь"
    k "Но он как был аутистом, так и остался ним"
    k "Так что его не кто недолюбливает"
    k "Мы все регулярно его пиздим"
    if friend == "maks":
        k "В какой-то момент появился Макс"
        k "Он рассказал, что Сашу украл зелебоба и его надо спасти"
    else:
        k "В какой-то момент появился Саша"
        k "Он рассказал, что Макса украл зелебоба и его надо спасти"
    k "Мы с радостью начали наше путешествие"
    k "Это наше начало нового приключения"
    pause(1.0)
    "ПРЕДУПРИЖДЕНИЕ" "Сюжет будет идти дальше как по другой ветке{w} Саша и Макс будут во всех диалогах, они спасают Кирилла, но ты спасаешь одного из них.{w} Короче в боях"
    "ПРЕДУПРИЖДЕНИЕ" "Короче в боях и некоторых диалогах будет Кирилл, а в других сюжетных будут Саша и Макс"
    $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} прошёл начало первой главы".format(persistent.user_name))
    show screen map
    ''
    '//'


image islands:
    "bg island2"
    pause(12)
    "bg island3"
    pause(12)
    "bg island4"
    repeat


label ray:
    $ OneDiscordMessage("# Начало Главы 1 😇\n{0} Отправляеться в РАЙ".format(persistent.user_name))
    play music "music/Cliffs.mp3"
    scene black
    with fade
    "Ноги оторвались с небес"
    "Мы начали подниматься куда-то верх"
    "Я начал чуствовать.."
    voice s0127
    s "Куда мы летим"
    m "Ебалн{w} в рай"
    d "Знаете{w} я бы её трахнул{w} и вас тоже"
    k "❤️❤️❤️"
    k "Трахни труп"
    d "Иди ко мне"
    m "Я так понимаю все мы сдохли"
    voice s0125
    s "Думаю{w=1.6} возможно{w=1} я перебрал с мефедроном"
    k "Хочешь покажу пенис?"
    "{i}Кирилл показал член{w=.4}, но не кто не увидел из-за темноты{w}(из-за размера){w=0.2}{nw}{/i}"
    m "Я могу переставить как мы втроём сдохни"
    m "Но, {w}кто убил Дениса?"
    voice s0126
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
    voice s0130
    s "Хз"
    voice s0131
    s "Где все?"
    m "Хороший вопрос"
    m "Мы вместе поднимались сюда"
    voice s0132
    s "У меня есть теория{w=2.1} что Дениса оно не подняло"
    m "Он типо насквозь через ад ещё пролетит?"
    voice s0133
    s "Да"
    voice s0134
    s "Он уже в пустоте в майнкрафте умирает"
    m "Урааа Роблокс"
    m "Где Кирилл тогда?"
    voice s0135
    s "Мне кажется или он опять его спиздил"
    voice s0136
    s "Когда мы падали он сказал{w=1.7} \"Трахни труп\" "
    voice s0137
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
    # voice uзапись
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    voice u0062
    u "{bt=3}Первое, что вы должны знать{/bt}"
    voice u0063
    u "{bt=3}В раю запрещена вся похабщина{/bt}"
    hide u
    show lolidance
    voice u0064
    u "{bt=3}Тоби ж вам запрещено трахаться{w} и нарушать законы Украины{/bt}"
    voice u0065
    u "{bt=3}Если вы их нарушите{w} будет{w} штраф{w} в размере{w} в ад{/bt}"
    voice u0066
    u "{bt=3}Так что можете наслаждаться спокойной жизнью!{/bt}"
    hide lolidance
    with dissolve
    m "Эм..{w} лучше уж в ад"
    voice s0138
    s "Да{w=1.8} по трахаемся на последок?"
    m "Го"
    scene black
    with fade
    "~ax-ax-ax"
    m "Что же{w}, теперь можем идти"
    scene islands
    with fade
    play music "music/BitWaves.wav"
    "Мы зашли во врата"
    "Перед нами были прекрасные виды"
    "Перед вами простирался райский пейзаж: мягкие облака, яркое солнце, и вдалеке виднелись красочные острова"
    "Ангелы играли music/BitWaves.wav музыку"
    show ps at right
    show pm talk at left
    with dissolve
    voice s0139
    s "Нам надо придумать что делать"
    m "Можем найти Кирилла{w}, не думаю что Денис мог его утащить в ад за собой"
    voice s0140
    s "Я вижу на том острове церковь"
    voice s0141
    s "Идём туда"
    menu ostatsa_v_ray:
        "Пойти?"
        "Пойти искать Кирилла":
            $ OneDiscordMessage("# Начало Главы 1 👇\nПойти искать Кирилла?\n> `Пойти`".format(persistent.user_name))
            pass
        "Остаться в раю":
            $ OneDiscordMessage("# Начало Главы 1 👇\nПойти искать Кирилла?\n> `Остаться в раю`".format(persistent.user_name))
            scene ending ray
            with fade
            pause 1.5
            $ ending("Остаться в раю")
            "Вы посчитали что вам не нужны приключения"
            "Вы остались в раю, что бы слушать music/BitWaves.wav музыку"
            "[end_message]"
            menu kirliskat:
                "Продолжить искать Кирилла?"
                "Да":
                    pass
                "Нет":
                    return
    m "Да"
    m "Если что мы всегда можем получить штраф"
    voice s0142
    s "Кстати{w=2.5}, я хотел тебя кое о чём спросить.."
    m "Что?"
    menu vashniy_vibor:
        "Спросить про утро или промолчать?"
        "Спросить":
            $ OneDiscordMessage("# Начало Главы 1 👇\nСпросить про утро или промолчать?\n> `Спросить`".format(persistent.user_name))
            voice s0143
            s "Что происходило сегодня утром?"
            voice s0144
            s "Почему ты опоздал на 5 урок?"
            m "Ты тоже вообще-то опоздал"
            voice s0145
            s "Я дрочил, у меня есть причина"
            m "Ну{w}, я просто{w}, как обычно, проспал"
            m "Не чего большего"
            s "{i}Он явно что-то не договаривает{/i}"
            m "Почему ты этим заинтересовался?"
            m "Ты обычно про это не спрашивал"
            voice s0147
            s "Сегодня стало интересно"
            voice s0148
            s "Вот и спросил"
            voice s0149
            s "Сам видишь какой сегодня странный день"
            m "Ладно идём дальше"
            $ ch_1_dialog_ms = True
        "Промолчать":
            $ OneDiscordMessage("# Начало Главы 1 👇\nСпросить про утро или промолчать?\n> `Промолчать`".format(persistent.user_name))
            voice s0150
            s "Не чего"
            voice s0151
            s "Уже забыл что, хотел спросить"
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
    voice s0152
    s "Хз"
    voice s0153
    s "Мб можно потрахатся и покаяться в церкви"
    m "Когда-то проверим"
    m "Я вот сейчас задумался"
    m "Почему я зелёный{w}, а не голубой как ты"
    voice s0154
    s "Почему мы тогда пиксельные и всё вокруг тоже"
    m "Это я так понимаю, мы не узнаем до конца игры"
    voice s0155
    s "Да"
    pause(1)
    m "Пизда"
    voice s0156
    s "Ты видел хуй Кирилла?{w} Когда он его показывал"
    m "Нет, темно было как в очке негра"
    m "Мы даже не узнали какого он цвета{w}, вдруг он тоже голубой"
    m "Но я видел его член до этого"
    voice s0156
    s "Все видели"
    voice s0157
    s "Найти человека, который не видел"
    voice s0158
    s "Не считая Кирила"
    m "Денис{w} не видел свой член"
    s "ظنّين دائماً أن هناك شيء ليس على ما ي"
    voice s0160
    s "Ладно заходим"
    hide pm
    hide ps
    with dissolve
    "Вы подошли к двери"
    "Саша попробовал открыть дверь"
    "Дверь была заперта"
    voice s0161
    s "бл, и что делать"
    show ps smile at left
    show pm da at right
    with dissolve
    m "Не знаю"
    m "Похоже бог покинул нас"
    voice s0162
    s "Пидарас"
    voice s0163
    s "Тогда залезем по другому"
    menu cerkov:
        "Как попасть в церковь"
        "Выбить окно":
            $ OneDiscordMessage("# Начало Главы 1 👇\nКак попасть в церковь?\n> `Выбить окно`".format(persistent.user_name))
            "Макс разбежался и выбил окно"
        "Чёрный вход":
            $ OneDiscordMessage("# Начало Главы 1 👇\nКак попасть в церковь?\n> `Чёрный вход`".format(persistent.user_name))
            "Вы обошли церковь и зашли через чёрный вход"
        "Забраться через крышу":
            $ OneDiscordMessage("# Начало Главы 1 👇\nКак попасть в церковь?\n> `Забраться через крышу`".format(persistent.user_name))
            "Вы поднялись на крышу"
            "На крыше не было прохода"
            m "Пиздец"
            "Вы спустились в низ"
            menu cerkov2:
                "Как попасть в церковь"
                "Выбрать окно":
                    $ OneDiscordMessage("# Начало Главы 1 👇\nКак попасть в церковь?\n> `Выбить окно`".format(persistent.user_name))
                    "Макс разбежался и выбил окно"
                "Чёрный вход":
                    $ OneDiscordMessage("# Начало Главы 1 👇\nКак попасть в церковь?\n> `Чёрный вход`".format(persistent.user_name))
                    "Вы обошли церковь и зашли через чёрный вход"
    scene black
    with fade
    "Вы наконец-то пробрались в церковь"
    "Божественная музыка.mp3 становилась всё громче и громче"
    # play music ...
    scene bg cerkovin
    with fade
    "В нутри была обычная церковь"
    show ps smile at left
    show pm da at right
    with dissolve
    m "И нахуйя мы сюда пробрались"
    voice s0163b
    s "Хуй знает"
    voice s0164
    s "Больше не было мест куда можно было пойти"
    voice s0165
    s "Разве что избить ангела"
    $ renpy.notify("Вам доступно новое действие")
    m "Ладно{w}, давай осмотримся здесь"
    show u
    with Dissolve(3)
    # voice uзапись
    u "{bt=3}Я{w} великое{w} божество{/bt}"
    voice u0067
    u "{bt=3}Что вы здесь забыли?{/bt}"
    m "Почему церковь не закрыта?"
    voice u0068
    u "{bt=3}Эм..{w} так как я недавно стала{w} великим{w} божеством{/bt}"
    voice u0069
    u "{bt=3}То и религию ещё не создала{/bt}"
    voice u0070
    u "{bt=3}Так что смысла в церкви нет{/bt}"
    voice s0166
    s "Как ты стала великим{w} божеством"
    voice u0071
    u "{bt=3}Неважно{/bt}"
    voice u0072
    u "{bt=3}Меня выбрали люди{/bt}"
    voice u0073
    u "{bt=3}Мне нужна ваша помощь{/bt}"
    voice u0074
    u "{bt=3}Поможете мне?{/bt}"
    menu boghelp:
        "Помочь великому божеству?"
        "Нам всё равно не чем заняться":
            $ OneDiscordMessage("# Начало Главы 1 👇\nПомочь великому божеству?\n> `Нам всё равно не чем заняться`".format(persistent.user_name))
            pass
        "Мы не хотим тебе помогать":
            $ OneDiscordMessage("# Начало Главы 1 👇\nПомочь великому божеству?\n> `Мы не хотим тебе помогать`".format(persistent.user_name))
            u "{bt=3}а..{/bt}"
            u "{bt=3}Значит я ошиблась когда, отправила вас в рай{/bt}"
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
    voice s0167
    s "Чем тебе надо помочь?"
    m "Мы готовы оставлять закладки мефедрона"
    u "{bt=3}Могла бы я выбрать других..{/bt}"
    u "{bt=3}И так{/bt}"
    hide u
    show lolidance
    u "{bt=3}В моём мире появился король демонов{/bt}"
    u "{bt=3}Ваша задача отправиться{w} и отпиздить его нахуй{/bt}"
    u "{bt=3}Да{w}, он меня заебал{/bt}"
    u "{bt=3}Так что я разрешаю вам делать всё что хотите{/bt}"
    u "{bt=3}Но уебите эту гниду{/bt}"
    u "{bt=3}Ваше приключение{w} будет изменить название..{/bt}"
    u "{bt=3}Эпическая сага о бескрайних приключениях Макса и Саши{w}\nв многомерном мире{w}, где они перерождаются снова и снова{w}\nоткрывая новые грани своих судебных циклов и сталкиваясь \nс бесчисленными вызовами{w}, погружаясь в уникальные реальности{w}, полные\n магии{w}, тайн и волнующих событий{w}, под названием\n 'Макс и Саша{w}: Реинкарнация в бескрайних\n измерениях и вечных временах{w}, где каждое воплощение — новое приключение{w}, а каждая\n судьба — загадка{w}, разгадываемая лишь через исследование\n бескрайних возможностей вечности'.{/bt}"
    voice s0168
    s "nigger"
    m "Ебать название"
    u "{bt=3}Кто{w} из вас{w} будет главным героем{/bt}"
    menu gg:
        "Выбрать главного героя(Только в боях, уник магия, фразы)"
        "Саша - Главный герой":
            $ OneDiscordMessage("# Начало Главы 1 ⚔️\nСаша - Главный герой`".format(persistent.user_name))
            $ name = "Саша"
            $ img_player = "sasha"
            $ a.name = name
            $ a.skills = [doubleattack]
            $ friend = "maks"
            $ a.hpmax = 30
            $ party_list = [maks]
        "Макс - Главный герой":
            $ OneDiscordMessage("# Начало Главы 1 🛡️\nМакс - Главный герой`".format(persistent.user_name))
            $ name = "Макс"
            $ img_player = "maks"
            $ a.name = name
            $ friend = "sasha"
            $ a.skills = [circleofhealing]
            $ a.hpmax = 25
            $ party_list = [sasha]
    call load_monsters from _call_load_monsters_2
    call load_items from _call_load_items_2
    $ restorehp()
    $ restoremp()
    u "{bt=3}Отличный выбор!{/bt}"
    u "{bt=3}[name], отныне ты должен со своим другом отпиздить короля демонов{/bt}"
    u "{bt=3}Управлять всем будешь ты{/bt}"
    u "{bt=3}Давай я покажу тебе как всё работает{/bt}"
    scene maprev
    with fade
    u "{bt=3}Перед тобой карта города{/bt}"
    $ persistent.main_menu = "gui/main_menu_ch_1_2.png"
    $ persistent.main_menu_music = "music/battle_in_aries_peak.mp3"
    $ config.main_menu_music = "music/battle_in_aries_peak.mp3"
    $ renpy.notify("Загляни в главное меню)")
    u "{bt=3}Здесь есть места которые ты можешь посетить{/bt}"
    u "{bt=3}Белые места — относительно безопасные места{/bt}"
    u "{bt=3}Красные — места где на тебя могут напасть{/bt}"
    u "{bt=3}Не советую туда ходить{/bt}"
    show screen world_time
    u "{bt=3}Сверху слева в правом нижнем углу показано время{/bt}"
    $ addTime()
    u "{bt=3}Следи за ним и не ходи ночью{/bt}"
    $ addTime()
    u "{bt=3}Я ограничила некоторые локации в разное время{/bt}"
    $ addTime()
    u "{bt=3}Что же, дальше ты сам{/bt}"
    $ addTime()
    u "{bt=3}Одолей короля демонов и спаси этот мир!{/bt}"
    $ OneDiscordMessage("# Начало Главы 1 🏅\n{0} прошёл начало первой главы".format(persistent.user_name))
    show screen map
    ''
    ''
    return