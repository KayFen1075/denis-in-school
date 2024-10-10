default persistent.SS_endings = []

python:
    def SS_ending(name):
        if name not in persistent.SS_endings:
            if name == "Секретная концовка":
                SS_secret_ending.grant()
            persistent.SS_endings.append(name)
            renpy.notify(f'Открыта новая концовка {name}')
            DiscordMessage("**{0}** открыл новую концовку в **Sex Simulator** `{1}`!".format(persistent.user_name, name, len(persistent.endings), count_endings))
    

label SEX_SIMULATOR_start:
    with fade
    scene black
    "Вы достали пыльный телефон"
    "На нём была одна игра"
    "{size=+20}Sex Simulator"
    menu start_game_sex_opt:
        "Запустить":
            pass
    play music "audio/sex simulator/Street_Sound.wav"
    scene whitle with fade
    pause 2
    scene bg street with dissolve
    show tankpng with dissolve
    t "Привет :3"
    s "0_o"
    s "Здарова"
    play sound "audio/sex simulator/Girl_Cmex.wav"
    t "Не хочешь сходить куда нибудь?))"
    s "Могу нахуй сходить"
    t "Не-не-не"
    play sound "audio/sex simulator/Girl_Cmex.wav"
    t "Я имею ввиду вместе)"
    s "Aaaaa"
    s "Ну давай"
    s "Только а ты кто вообще?"
    t "Мы пока не знакомы"
    t "Вот и хочу познакомиться с тобой :333"
    menu cafe_kino:
        "Ну ок"
        "Го в кафе сходим":
            jump SEX_SIMULATOR_cafe
        "Го в кино сходим":
            jump SEX_SIMULATOR_kino

label SEX_SIMULATOR_cafe:
    play sound "audio/sex simulator/Girl_Cmex.wav"
    t "Давай)"
    scene black with fade
    "Вы идёте в кафе"
    pause 5
    "Не ну а чё, идти долго надо..."
    pause 5
    play music "audio/sex simulator/Cafe_Background.wav"
    scene bg cafe with dissolve
    "Вы пришли."
    show tankpng with dissolve
    t "Что заказывать будем?"
    menu SEX_SIMULATOR_act_cafe:
        "Ммммм..."
        "Давай стейк":
            t "Я не против :3"
            "Вам принесли вашы стейки."
            t "Выглядит вкусно"
            s "Ага"
            pass
        "Давай что ты хочешь":
            t "Надо подумать..."
            t "Как насчёт мороженого?"
            s "Давай"
            "Вам принесли мороженое."
            t "Выглядит вкусно"
            s "Ага"
            pass
            #block of code to run
    menu SEX_SIMULATOR_act_cafe_telefon:
        "*У тебя зазвонил телефон*"
        "Сбросить":
            "Вы сбросили звонок."
            
        "Ответить":
            "Вы ответили на звонок."
            s "У аппарата"
            m "Алё"
            m "Погнали в майн играть"
            s "Я занят сейчас"
            m "Мне похуй"
            menu SEX_SIMULATOR_act_cafe_minecraft:
                "Отказаться":
                    s "Я сейчвс на свидании, сам иди играй"
                    m ":(((("
                    "*Макс сбросил трубку*"
                "Согласиться":
                    s "Ладно го"
                    m "Ок жду в дс"
                    "*Макс сбросил трубку*"
                    s "Слушай..."
                    s "Тут такое дело..."
                    s "Пошла нахуй, я пошёл играть в майнкрафт с кентами"
                    t "0_0"
                    "Ты бросил тянку одну, и ушёл домой"
                    # Хорошая концовка
    s "Слушай, а чем ты в жизни занимаешься?"
    t "Нуууу..."
    t "Я пока что учусь в школе еще"
    play sound "audio/sex simulator/Girl_Cmex.wav"
    t "А так в свободное время люблю гулять с друзьями)))"
    menu SEX_SIMULATOR_act_cafe_aty:
        t "А ты?"
        "Тоже учусь еще":
            t "Понятно..."
            "Вам принесли счёт."
            pass
            # End ty lox
        "Я невьебенно крутой":
            t "Ха-ха-ха-ха"
            t "А ты смешной)"
            s "Это не шутка была"
            "Ты понравился тянке."
            pause 2.0
            "Вам принесли счёт."
            menu SEX_SIMULATOR_act_cafe_price:
                s "Ахуеть"
                "Возмутиться":
                    pass
                "Отдать деньги":
                    s "Вот"
                    scene black with fade
                    "Вы отдали деньги, и вы вышли на улицу."
                    scene bg street with fade
                    play music "audio/sex simulator/Street_Sound.wav"
                    t "Хорошо посидели)"
                    s "Ага"
                    t "Давай еще как нибудь встретимся"
                    s "Я не против"
                    "Тянка дала вам свой номер телефона."
                    t "И еще..."
                    menu SEX_SIMULATOR_act_street:
                        "Тянка потянулась поцеловаться."
                        "Поцеловать":
                            pass
                        "Пошла нахуй":
                            "Ты долбаёб?"
                            pass
                    pause 2
                    "Вы поцеловались."
                    t "Ну ладно, до встречи)"
                    s "Да, давай)"
                    # (Не)Плохая концовка
                    #block of code to run
    s "0-0"
    s "Вы наверное ошиблись, тут чёто слишком дохуя"
    "Официант" "200 грн это нормальная цена"
    s "Ладно, вот"
    scene black with fade
    "Ты отдал деньги, и вы вышли на улицу."
    scene bg street with fade
    play music "audio/sex simulator/Street_Sound.wav"
    t "Ну, не плохо посидели"
    s "Ага"
    play sound "audio/sex simulator/Girl_think.wav"
    t "Может еще как нибудь встретимся?"
    s "Я не против"
    "Тянка дала вам свой номер телефона."
    t "Ну давай, до встречи"
    s "Да давай"
    s "Пока"
    "Вы разошлись."
    pass
        
label SEX_SIMULATOR_kino:
    t "Давай)"
    "???" "Вы идёте в кино"
    "???" "..."
    "???" "..."
    "???" "..."
    "???" "..."
    "???" "Не не а чё, идти долго надо..."
    "???" "..."
    "???" "..."
    "???" "Вы пришли."
    play music "audio/sex simulator/Cinema_Background.wav"
    scene bg cinema with dissolve
    t "На какой фильм пойдём?"
    menu SEX_SIMULATOR_act_cinema_film:
        "Мммм..."
        "Марвел":
            t "Я не против :3"
            "???" "Вы сели в ожидании начала фильма."
            "???" "..."
            "???" "..."
            s "Слушай хочешь анегдот расскажу?"
            t "О, давай))"
            s "Приходит значит парень в столовую, и начинает смотреть меню"
            s '"Прирожок - 50 руб"\n"Передёрнуть - 500 руб"'
            s "Смотрит на кассу, а там стоит красивая блондиночка"
            s "Он подходит к ней и даёт 500 рублей"
            s "Она смотрит на него, улыбается"
            s "И спрашивает: \n-Тебе как передёргивать?"
            s "А он ей отвечает:"
            s "Передёрнуть я могу и дома, мне пожалуйста 10 прирожков."
            t "..."
            t "Пиздец"
            "???" "Начинается фильм, и вы идете в зал."
            scene bg cinema film with dissolve
            play music "audio/sex simulator/Marvel_Background.wav"
            "???" "Крч представь что тут марвел идет."
            stop music
            "???" "..."
            "???" "..."
            play sound "audio/sex simulator/Error_sex.mp3"
            "???" "Фильм подошел к концу, вы выходите на улицу.{w=0.5}{nw}"
            scene black with hpunch
            m "Э БЛЯ"
            s "От сука игра вылетела"
            m "Ну пиздец"
            

        "Ужасы":
            s "Как насчёт хорора?"
            t "Ого, хоррор..."
            t "Ну давай попробуем)))"
            "???" "Вы сели в ожидании начала фильма."
            s "Может купим что-то поесть?"
            t "Давай)"
            "???" "Вы подходите к кассе."
            t "Мммм..."
            t "Может купим попкорн?"
            s "Го"
            "???" "Ты смотришь на цену."
            s "0_0"
            s "Та не, я чёто передумал"
            "???" "Тянка не услышала это, и уже была готова купить попкорн."
            menu SEX_SIMULATOR_act_cinema_casa:
                "Купить двоим":
                    "???" "Ты решаешь заплатить за двоих."
                    "???" "Тянке понравилось это."

                    "???" "Начинается фильм, и вы идете в зал."
                    scene bg cinema film with dissolve
                    play music "audio/sex simulator/Horror_Background.wav"
                    t "Страшновато..."
                    s "Ага"
                    "???" "Обстановка начинает накаляться."
                    s "Бля я в ахуе"
                    s "Чё так страшно то"
                    t "..."
                    t "..."
                    t "..."
                    play sound "audio/sex simulator/Girl_Scream.wav"
                    scene black with hpunch
                    t "A-A-A-A-A"
                    menu SEX_SIMULATOR_act_cinema_horror:
                        "Прижать к себе":
                            "???" "Ты прижал тянку к себе."
                            "???" "Ты нравишься тянке."
                            "???" "Фильм подошел к концу, и вы выходите на улицу."
                            scene bg street with dissolve
                            play music "audio/sex simulator/Street_Sound.wav"
                            t "А мне очень понравился фильм)))"
                            s "Согласен"
                            "???" "Ты уже хотел начать прощаться, но тянка остановила тебя."
                            t "Слушай..."
                            t "Может быть проведём еще немного времени вместе?"
                            "???" "Ты впал в ступор от услышанного."
                            menu SEX_SIMULATOR_street_tank:
                                "Согласиться":
                                    s "Ну это..."
                                    s "Я не против"
                                    t "Отлично)"
                                    t "Как насчёт пойти ко мне в гости?)"
                                    "???" "Ты ахуел от услышанного."
                                    s "Я согласен..."
                                    scene bg home tank with dissolve
                                    show tankpng with dissolve
                                    "???" "Вы пришли к тянке домой."
                                    s "А что мы тут делать будем?"
                                    t "Нууу..."
                                    t "Есть много вариантов..."
                                    "???" "Вы с тянкой сблизились."
                                    t "Как насчёт..."
                                    t "Тянка дотронулась до твоего писюна, и потянулась к нему."
                                    "???" "..."
                                    play sound "audio/sex simulator/Girl_Sex.wav"
                                    "???" "И у вас начался жёсткий сэкс."
                                    # Лучшая концовка
                                "Отказаться":
                                    pass
                                    #block of code to run
                                
                        "Хули ты орёшь?":
                            pass
                            #block of code to run
                        
                "Не покупать":
                    pass
                    #block of code to run
                
            pass
        