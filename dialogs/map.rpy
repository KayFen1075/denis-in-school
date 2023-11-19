screen world_time:
    modal False
    zorder 100

    fixed:
        $ time_images = {
        6: "gui/time_6.png",
        12: "gui/time_12.png",
        18: "gui/time_18.png",
        24: "gui/time_24.png"
        }

        if game_time in time_images:
            add time_images[game_time]

screen map:
    modal True
    zorder 100

    fixed:
        xsize 1920 ysize 1080
        $ time_images = {
            6: "images/map/map_morging.png",
            12: "images/map/map.png",
            18: "images/map/map_evening.png",
            24: "images/map/map_night.png"
        }
        if game_time in time_images:
            add time_images[game_time]

        button:
            xpos 1554 ypos 905
            xsize 163 ysize 156
            idle_background "gui/arrmory.png"
            hover_foreground "gui/arrmory.png"
            action Show("EquipmentScreen")
        button:
            xpos 1740 ypos 905
            xsize 168 ysize 153
            idle_background "gui/backpack.png"
            hover_foreground "gui/backpack.png"
            action Show("inventory_screen", None, player_inv)
        button:
            xpos 0 ypos 0
            xsize 561 ysize 333
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/les_hover.png"
            action Hide("map"), Jump("les")
        button:
            xpos 520 ypos 0
            xsize 854 ysize 503
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/pola_hover.png"
            action Hide("map"), Jump("pola")
        button:
            xpos 305 ypos 623
            xsize 110 ysize 118
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/ds_hover.png"
            action Hide("map"), Jump("ds")
        button:
            xpos 650 ypos 526
            xsize 68 ysize 88
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/dm_hover.png"
            action Hide("map"), Jump("dm")
        button:
            xpos 949 ypos 625
            xsize 123 ysize 99
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/most_hover.png"
            action Hide("map"), Jump("most")
        button:
            xpos 1321 ypos 513
            xsize 108 ysize 112
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/shop_hover.png"
            action Hide("map"), Jump("shop")
        button:
            xpos 1839 ypos 13
            xsize 74 ysize 66
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/daun_hover.png"
            action Hide("map"), Jump("daun")
        button:
            xpos 170 ypos 943
            xsize 225 ysize 36
            idle_background "images/map/not_hover.png"
            hover_foreground "images/map/not_hover.png"
            action Hide("map"), Jump("dansh")
