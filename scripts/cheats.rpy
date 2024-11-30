label cheats:
    $ print(player_inv.inv)
    menu CHEAT_MENU:
        "Все читы"
        "Локации":
            menu DEV_CHEATS:
                "Читы разроботчика"
                "Сплеш скрин":
                    jump splashscreen
                "SEX_SIMULATOR":
                    jump SEX_SIMULATOR_start
                "Пролог":
                    pass
                "Глава 1":
                    jump deadw
                "Перед РПГ":
                    $ narrator = Character(what_style="pixel_say_dialogue", narrator=True) # soon
                    $ nvl = Character(what_style="pixel_say_dialogue")
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
                    jump ray_dev
        "Борис":
            menu CHEATS_BORIS:
                "+1000":
                    $ renpy.notify("+1000")
                    $ player_inv.money += 1000
                    jump cheats
                "+5000":
                    $ renpy.notify("+5000")
                    $ player_inv.money += 5000
                    jump cheats
                "+10000":
                    $ renpy.notify("+10000")
                    $ player_inv.money += 10000
                    jump cheats
                "+10000000":
                    $ renpy.notify("+10000000")
                    $ player_inv.money += 10000000
                    jump cheats
                "+Предметы":
                    call load_items
                    $ player_inv.takes([arrmory_kora,arrmory_pants,arrmory_lists,arrmory_hot_pants,arrmory_nike_pro,arrmory_dead_slime,arrmory_banana,arrmory_list,arrmory_gold,arrmory_capert,arrmory_god,arrmory_black,arrmory_ice,arrmory_druid,arrmory_magic,arrmory_woin,arrmory_adic,arrmory_dildo,arrmory_feja])
                    $ player_inv.takes([palka_sworld,rogatka_sworld,lesh_sworld,samoletik_sworld,kulak_sworld,zerkalo_sworld,gold_sworld,bow_sworld,sheild_sworld,ice_sworld,klin_sworld,poduszka_sworld,vibrator_sworld,knut_sworld,obs_sworld,biblia_sworld,doom_sworld,czerep_sworld,ices_sworld,resinoviy_chlen])
                    $ player_inv.takes([assc_sex,assc_list,assc_zeleboba,assc_gold,assc_lune,assc_bb,assc_roshen,assc_sans,assc_cum,assc_mes,assc_photo_album,assc_hell,assc_prisma,assc_xxx,assc_cums])
                    jump shop23
                "+Магия":
                    $ player_inv.take_skills([nike_pro_skill,dead_slime_skill,banana_skill,list_skill,gold_skill,capert_skill,god_skill,black_skill,ice_skill,druid_skill,magic_skill,woin_skill,adic_skill,dildo_skill,feja_skill,resinoviy_chlen_skill,kulak_sworld_skill,zerkalo_sworld_skill,gold_sworld_skill,bow_sworld_skill,sheild_sworld_skill,ice_sworld_skill,klin_sworld_skill,poduszka_sworld_skill,vibrator_sworld_skill,knut_sworld_skill,obs_sworld_skill,biblia_sworld_skill,doom_sworld_skill,czerep_sworld_skill])
                "ПОЛНЫЙ ОТРЯД":
                    $ party_list = [sasha, lox, tanka, boris, maksim]
                    jump cheats
                "+Levels":
                    $ cheat_levels()
                    jump cheats
                        
                "leave":
                    jump shop23
        "Бои":
            menu BATTLE:
                "Вызвать бой":
                    pass
                "Бой с зелебобой":
                    pass
        "Закрыть":
            pass

init python:
    def cheat_levels():
        for i in party_list:
            i.lvl = 16
        return