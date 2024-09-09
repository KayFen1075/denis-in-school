define -2 all_achievements = Achievement(
    name=_("Платина"),
    id="platinum_achievement",
    description=_("Поздравляем! Вы разблокировали все достижения!"),
    unlocked_image=Transform("gui/window_icon.png"),
    hide_description=_("Получите все остальные достижения"),
)

define ach_bad_start = Achievement(
    name=_("Ужасное начало"),
    id="bad_start",
    description=_("Пойти в школу"),
    unlocked_image="gui/achievements/ach_bad_start.png",
    locked_image="locked_achievement",
    hidden=False,
)

define ach_die_with_denis = Achievement(
    name=_("Слабая смерть"),
    id="ach_die_with_denis",
    description=_("Умереть от Дениса"),
    unlocked_image="gui/achievements/ach_die_with_denis.png",
    locked_image=Transform("gui/achievements/ach_die_with_denis.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
    hide_description=True,
)

define ach_win_boss = Achievement(
    name=_("Босс файт"),
    id="ach_win_boss",
    description=_("Одолеть босса в доме Кирилла"),
    unlocked_image="gui/achievements/ach_win_boss.png",
    locked_image="locked_achievement",
    hidden=False,
)

define ach_mocha_b = Achievement(
    name=_("Золотой дождь"),
    id="ach_mocha_b",
    description=_("Обоссать Бориса"),
    unlocked_image="gui/achievements/ach_mocha_b.png",
    locked_image="locked_achievement",
    hide_description=True,
    hidden=False,
)

define ach_end_prolog = Achievement(
    name=_("Конец начала"),
    id="end_prolog",
    description=_("Заверши пролог и выживи"),
    unlocked_image="gui/achievements/ach_end_prolog.png",
    locked_image="locked_achievement",
    hidden=False,
)

define ach_denis_word = Achievement(
    name=_("Пазл"),
    id="ach_denis_word",
    description=_("Зачем ты это сделал, теперь он знает где ты"),
    unlocked_image="gui/achievements/ach_denis_word.png",
    locked_image="locked_achievement",
    hide_description=True,
    hidden=False,
)

define ach_ad = Achievement(
    name=_("Адское пекло"),
    id="ach_ad",
    description=_("Попасть в АД"),
    unlocked_image="gui/achievements/ach_ad.png",
    locked_image="locked_achievement",
    hidden=False,
)

define ach_ray = Achievement(
    name=_("Райские пейзажи"),
    id="ach_ray",
    description=_("Попасть в РАЙ"),
    unlocked_image="gui/achievements/ach_ray.png",
    locked_image="locked_achievement",
    hidden=False,
)

define ach_angel_killer = Achievement(
    name=_("Ангело убийца"),
    id="ach_angel_killer",
    description=_("Избить ангела до смерти"),
    unlocked_image="gui/achievements/ach_angel_killer.png",
    locked_image=Transform("gui/achievements/ach_angel_killer.png", matrixcolor=TintMatrix("#000000")),
    hidden=True,
)

define ach_ui = Achievement(
    name=_("Искупление"),
    id="ach_ui",
    description=_("Отправитсья в ад с рая"),
    unlocked_image="gui/achievements/ach_ui.png",
    locked_image=Transform("gui/achievements/ach_ui.png", matrixcolor=TintMatrix("#000000")),
    hide_description=True,
    hidden=False,
)

define ach_player_maks = Achievement(
    name=_("Ренкорация хиллера!"),
    id="ach_player_maks",
    description=_("В главных ролях - самый сексуальный мужик в мир"),
    unlocked_image="gui/achievements/ach_player_maks.png",
    locked_image=Transform("gui/achievements/ach_player_maks.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_player_lox = Achievement(
    name=_("Ренкорация шлюхи!"),
    id="ach_player_lox",
    description=_("В главных ролях - горячая чикса"),
    unlocked_image="gui/achievements/ach_player_lox.png",
    locked_image=Transform("gui/achievements/ach_player_lox.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_player_sasha = Achievement(
    name=_("Ренкорация наёмника!"),
    id="ach_player_sasha",
    description=_("В главных ролях - конченный идиот"),
    unlocked_image="gui/achievements/ach_player_sasha.png",
    locked_image=Transform("gui/achievements/ach_player_sasha.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

# define ach_players_all = Achievement(
#     name=_("Ренкорация далбоёбов!"),
#     id="ach_players_all",
#     description=_("В фильме Денис в школе"),
#     unlocked_image="gui/achievements/ach_players_all.png",
#     stat_max=3,
#     locked_image=Transform("gui/achievements/ach_players_all.png", matrixcolor=TintMatrix("#000000")),
#     hidden=False,
# )

define ach_sex_ms = Achievement(
    name=_("Горячая ночь"),
    id="ach_sex_ms",
    description=_("Переспать с Сашей в тесной кроватке"),
    unlocked_image="gui/achievements/ach_sex_ms.png",
    locked_image=Transform("gui/achievements/ach_sex_ms.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_buy_magic = Achievement(
    name=_("И это платно?"),
    id="ach_buy_magic",
    description=_("Купить заклинание"),
    unlocked_image="gui/achievements/ach_buy_magic.png",
    locked_image=Transform("gui/achievements/ach_buy_magic.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_buy_all_magic = Achievement(
    name=_("Стать магом в 30 лет"),
    id="ach_buy_all_magic",
    description=_("Купить все заклинания"),
    unlocked_image="gui/achievements/ach_buy_all_magic.png",
    locked_image=Transform("gui/achievements/ach_buy_all_magic.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_max_level = Achievement(
    name=_("Превзойти себя"),
    id="ach_max_level",
    description=_("Достигни максимального уровня"),
    unlocked_image="gui/achievements/ach_max_level.png",
    locked_image=Transform("gui/achievements/ach_max_level.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_cash_1000 = Achievement(
    name=_("Первые деньги"),
    id="ach_cash_1000",
    description=_("Заработать 1к грывень"),
    unlocked_image="gui/achievements/ach_cash_1000.png",
    locked_image=Transform("gui/achievements/ach_cash_1000.png", matrixcolor=TintMatrix("#000000")),
    stat_max=1000,
    hidden=False,
)

define ach_cash_10000 = Achievement(
    name=_("Хороший торговец"),
    id="ach_cash_10000",
    description=_("Заработать 10к грывень"),
    unlocked_image="gui/achievements/ach_cash_10000.png",
    locked_image=Transform("gui/achievements/ach_cash_10000.png", matrixcolor=TintMatrix("#000000")),
    stat_max=10,
    hidden=False,
)

define ach_cash_inf = Achievement(
    name=_("Хороший читер"),
    id="ach_cash_inf",
    description=_("Заработать 100к грывень"),
    unlocked_image="gui/achievements/ach_cash_inf.png",
    stat_max=100,
    locked_image=Transform("gui/achievements/ach_cash_inf.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_all_events = Achievement(
    name=_("Я видел всё"),
    id="ach_all_events",
    description=_("Увидеть все события"),
    unlocked_image="gui/achievements/ach_all_events.png",
    locked_image=Transform("gui/achievements/ach_all_events.png", matrixcolor=TintMatrix("#000000")),
    stat_max=10,
    hide_description=True,
    hidden=False,
)

define ach_zeleboba = Achievement(
    name=_("Get out of my swamp!"),
    id="ach_zeleboba",
    description=_("Одолеть зелебобу"),
    unlocked_image="gui/achievements/ach_zeleboba.png",
    locked_image=Transform("gui/achievements/ach_zeleboba.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

# define ach_otrad_xuina = Achievement(
#     name=_("Большой.. выбор"),
#     id="ach_otrad_xuina",
#     description=_("Собрать всех бахмутовцев!"),
#     unlocked_image="gui/achievements/ach_otrad_xuina.png",
#     stat_max=6,
#     locked_image=Transform("gui/achievements/ach_otrad_xuina.png", matrixcolor=TintMatrix("#000000")),
#     hidden=False,
# )

define ach_code = Achievement(
    name=_("Какой-то код"),
    id="ach_code",
    description=_("Спрятан в дискорде"),
    unlocked_image="gui/achievements/ach_code.png",
    locked_image=Transform("gui/achievements/ach_code.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_dead_denis = Achievement(
    name=_("Убить дениса"),
    id="ach_dead_denis",
    description=_("Поздравляю! Вы убили Дениса в загробном мире"),
    unlocked_image="gui/achievements/ach_dead_denis.png",
    locked_image=Transform("gui/achievements/ach_dead_denis.png", matrixcolor=TintMatrix("#000000")),
    hidden=True,
)

define ach_back_to_hell = Achievement(
    name=_("Обратно в пекло"),
    id="ach_back_to_hell",
    description=_("Собрать 12 обсидиановых мечей и построить портал в ад"),
    unlocked_image="gui/achievements/ach_back_to_hell.png",
    locked_image=Transform("gui/achievements/ach_back_to_hell.png", matrixcolor=TintMatrix("#000000")),
    stat_max=12,
    hidden=False,
)

define ach_end_ch1 = Achievement(
    name=_("Конец приключения"),
    id="ach_end_ch1",
    description=_("Завершить первую главу"),
    unlocked_image="gui/achievements/ach_end_ch1.png",
    locked_image=Transform("gui/achievements/ach_end_ch1.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)



# define ach_del_d = Achievement(
#     name=_("Щястливый конец"),
#     id="ach_del_d",
#     description=_("Вернуться домой"),
#     unlocked_image="gui/achievements/ach_del_d.png",
#     locked_image=Transform("gui/achievements/ach_del_d.png", matrixcolor=TintMatrix("#000000")),
#     hidden=True,
# )


define ach_play_again = Achievement(
    name=_("Второй шанц"), 
    id="ach_play_again",
    description=_("Начать сначала"),
    unlocked_image="gui/achievements/ach_play_again.png",
    locked_image=Transform("gui/achievements/ach_play_again.png", matrixcolor=TintMatrix("#000000")),
    hidden=False,
)

define ach_dead_file = Achievement(
    name=_("Потерянная история"), 
    id="ach_dead_file",
    description=_("Потерять Макса или Сашу"),
    unlocked_image="locked_achievement",
    locked_image="locked_achievement",
    hide_description=True,
    hidden=False,
)

define ach_insane = Achievement(
    name=_("НЕВОЗМОЖНО"), 
    id="ach_insane",
    description=_("Пройти игру от начала до конца на сложности НЕВОЗМОЖНО"),
    unlocked_image="gui/achievements/ach_insane.png",
    locked_image="locked_achievement",
    hidden=False,
)