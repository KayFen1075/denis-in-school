default name = "Player"
default currentplayer = "[name]"
default eventrunning = False
default _game_menu_screen = "preferences"

label load_setup:
    if not name:
        $ name = "Player"
    $ a.name = name
    $ magicheal.addSkill(a) # add new skills
    $ defenseup.addSkill(c)
    $ magicswap.addSkill(y)
    call load_monsters from _call_load_monsters_1
    call load_items from _call_load_items_1
    $ party_list = [m,s,k] # initial party list, including main character
    $ fixedset = "set 1"
    $ wild_monsters = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11]
    $ restorehp()
    $ restoremp()
    return
