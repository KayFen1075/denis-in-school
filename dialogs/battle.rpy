default monsters = [
    {
        "name": "Орк",
        "xp": 100,
        "armor": 5,
        "attacks": [
            {
                "name": "Атака ножём!",
                "damageMin": 34,
                "damageMax": 50,
            },
            {
                "name": "Атака кулаками!",
                "damageMin": 10,
                "damageMax": 30,
            },
        ],
    },
]
default magic = {
    "maks": {
        "name": "Уникальная магия Макса",
        "description": "Хиляет выбраного персонажа",
        "damage": 0,
        "health": 50,
        "dialogs": [
            "Выпей мою сперму",
            "Я хуй знает будет это работать или нет",
            "Ты первый кто пробует",
        ],
    },
}

default weapons = {
    "fists": {
        "name": "Удар кулаками",
        "description": "Хуярите из-зо всех сил",
        "cost": 0,
        "damageMin": 20,
        "damageMax": 45,
        "dialogs": [
            "Я конечно не ванпачмен{w}, но я тебя выебу",
            "Stop mob vote!",
        ],
    },
    "knight": {
        "name": "Удар ножёж",
        "description": "27 ударов",
        "cost": 100,
        "damageMin": 100,
        "damageMax": 130,
        "dialogs": [
            "Да, я действовал на верника",
            "Щя зарежу нахуй",
        ],
    },
    "bow": {
        "name": "Выстрел из лука",
        "description": "Точное попадание!",
        "cost": 350,
        "damageMin": 170,
        "damageMax": 200,
        "dialogs": [
            "Пиу пау{w}, я стреляю по хохлам",
            "Иди нахуй",
        ],
    },
}

label start_battle():
    $ player_inv.money += 10
    $ print(player_inv.money)
    show screen crafting(player_inv)
    ''
    ''
    ''
    hide screen world_time
    call battle
    $ restorehp()
    $ restoremp()
    "Вы пришли, как вдруг на вас напал"
    show screen world_time
    show screen map
    play music "music/Path to Lake Land.ogg"
    ''
    return
