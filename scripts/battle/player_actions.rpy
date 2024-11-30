label turn_actions:
    while not battleEnd:
        $ playersCnt()
        $ currentplayer = None
        $ message = "attack"
        call screen turn_select
        $ currentplayer = _return
        if currentplayer != "done":
            call player_skill from _call_player_skill
            $ endTurn()
            jump turn_actions
        else:
            $ currentplayer = None
            $ message = None
            return
    return

screen turn_select():
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            for p in battle_players:
                if not p.turn and p.hp > 0:
                    textbutton "[p.name]" xalign 0.5 action Return(p)
            textbutton "Захончить ход" xalign 0.5 action Return("done")

label player_skill:
    $ startTurn()
    call screen choose_skill
    $ b_skill = _return
    if isinstance(b_skill, Skill):
        $ target = b_skill.targ
        call target_select(b_skill.targs) from _call_target_select
    if b_skill == "item":
        $ message = "item"
        call screen inventory_inbattle(player_inv)
        hide screen inv_tooltip
        $ b_skill = _return
        $ target = getTarget(b_skill)
        call target_select from _call_target_select_1
    elif b_skill == "attack":
        call target_select from _call_target_select_2
        $ target = "attack"
    if b_skill == "defend":
        $ target = "defend"
    call skill_effects from _call_skill_effects
    return

screen choose_skill():
    key "mouseup_3" action Function(renpy.pop_call), Jump("turn_actions")
    add "images/battle/skillbox.png" pos 20, 150 zoom 1.5

    if currentplayer.skills['старт']:
        $ skll = currentplayer.skills['старт']
        imagebutton:
            xpos 112 ypos 216 action Return(skll), SensitiveIf(sensIf(skll))
            idle getImage(skll)
            hover im.MatrixColor(getImage(skll), im.matrix.brightness(0.2))
            insensitive im.MatrixColor(getImage(skll), im.matrix.saturation(0.1))
            tooltip "Сила: {0}\nМана: {1}".format(skll.pwr + (currentplayer.lvl * (skll.pwr/4)), skll.mp_cost)
    else:
            imagebutton:
                xpos 112 ypos 216
                idle "images/skills/blank.png"
                tooltip "Тут пусто"
    
    if getattr(currentplayer.equip.get('оружие'), 'skill', None):
        $ skll = currentplayer.equip.get('оружие').skill
        imagebutton:
            xpos 244 ypos 216 action Return(skll), SensitiveIf(sensIf(skll))
            idle getImage(skll)
            hover im.MatrixColor(getImage(skll), im.matrix.brightness(0.2))
            insensitive im.MatrixColor(getImage(skll), im.matrix.saturation(0.1))
            tooltip "Сила: {0}\nМана: {1}".format(skll.pwr + (currentplayer.lvl * (skll.pwr/4)), skll.mp_cost)
    else:
        imagebutton:
            xpos 244 ypos 216
            idle "images/skills/blank.png"
            tooltip "Тут пусто"
    
    if currentplayer.skills['предмет']:
        $ skll = currentplayer.skills['предмет']
        imagebutton:
            xpos 376 ypos 216 action Return(skll), SensitiveIf(sensIf(skll))
            idle getImage(skll)
            hover im.MatrixColor(getImage(skll), im.matrix.brightness(0.2))
            insensitive im.MatrixColor(getImage(skll), im.matrix.saturation(0.1))
            tooltip "Сила: {0}\nМана: {1}".format(skll.pwr + (currentplayer.lvl * (skll.pwr/4)), skll.mp_cost)
    else:
        imagebutton:
            xpos 376 ypos 216
            idle "images/skills/blank.png"
    
    if len(currentplayer.p_skills):
        $ skll = currentplayer.p_skills[0]
        imagebutton:
            xpos 142 ypos 439 action Return(skll), SensitiveIf(sensIf(skll))
            idle getImage(skll)
            hover im.MatrixColor(getImage(skll), im.matrix.brightness(0.2))
            insensitive im.MatrixColor(getImage(skll), im.matrix.saturation(0.1))
            tooltip "Сила: {0}\nМана: {1}".format(skll.pwr + (currentplayer.lvl * (skll.pwr/4)), skll.mp_cost)
    else:
        imagebutton:
            xpos 142 ypos 439
            idle "images/skills/blank.png"
    
    if currentplayer.skills['свиток']:
        $ skll = currentplayer.skills['свиток']
        imagebutton:
            xpos 328 ypos 439 action Return(skll), SensitiveIf(sensIf(skll))
            idle getImage(skll)
            hover im.MatrixColor(getImage(skll), im.matrix.brightness(0.2))
            insensitive im.MatrixColor(getImage(skll), im.matrix.saturation(0.1))
            tooltip "Сила: {0}\nМана: {1}".format(skll.pwr + (currentplayer.lvl * (skll.pwr/4)), skll.mp_cost)
    else:
        imagebutton:
            xpos 328 ypos 439
            idle "images/skills/blank.png"
    style_group "skills"
    vpgrid:
        cols 2
        rows 2
        spacing 20
        align (0.285, 0.25)
        imagebutton:
            idle "images/skills/inv.png" align (.5,.5) style_group "skills" action Return("item")
        imagebutton:
            idle "images/skills/atack.png" align (.5,.5) style_group "skills" action Return("attack")
        imagebutton:
            idle "images/skills/blank.png" align (.5,.5) style_group "skills" action Return("defend")
        imagebutton:
            idle "images/skills/blank.png" align (.5,.5) style_group "skills" action Function(renpy.pop_call), Jump("turn_actions")
    timer 300 action Hide('choose_skill'), Function(renpy.pop_call), Jump("turn_actions")

label target_select(targs=1):
    if target == "enemy":
        $ message = "target_who"
        while targs > 0 and len(picked_targs) < (monsters_total - monsters_dead):
            call screen select_monster
            $ picked_targs.append(_return)
            $ targs -= 1
    elif target == "ally":
        $ message = "use_on_who"
        while targs > 0 and len(picked_targs) < len(alive_players):
            call screen select_ally
            $ picked_targs.append(_return)
            $ targs -= 1
    elif target == "ko":
        $ message = "use_on_who"
        while targs > 0 and len(picked_targs) < (len(battle_players)-len(alive_players)):
            call screen select_ally
            $ picked_targs.append(_return)
            $ targs -= 1
    if target == "row":
        $ message = "target_who"
        call screen select_monster
        if _return in monster_slot[0:4]:
            python:
                for m in monster_slot[0:4]:
                    if not m.dead:
                        picked_targs.append(m)
        elif _return in monster_slot[4:8]:
            python:
                for m in monster_slot[4:8]:
                    if not m.dead:
                        picked_targs.append(m)
    return

screen select_ally():
    key "mouseup_3" action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not picked_targs)
    style_prefix "confirm"
    frame:
        yalign 0.2
        has vbox:
            label "Select a player"
            for p in battle_players:
                if not p in picked_targs:
                    if target == "ko":
                        if p.hp == 0:
                            textbutton "[p.name]" xalign 0.5 action Return(p)
                    else:
                        if p.hp > 0:
                            textbutton "[p.name]" xalign 0.5 action Return(p)
            textbutton "Cancel" xalign 0.5 action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not picked_targs)

screen select_monster():
    key "mouseup_3" action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not picked_targs)
    frame:
        yalign 0.2
        has vbox:
            textbutton "Cancel" xalign 0.5 action Function(renpy.pop_call), Jump("player_skill"), SensitiveIf(not picked_targs)

screen monster_dmg():
    style_group "dmg"
    for m in monster_slot:
        if m in missed_t:
            text "[misstext]" anchor (.5,.5) pos m.dmg_pos at shake_fade
        elif m in skill_t:
            text "[skilltext]" anchor (.5,.5) pos m.dmg_pos at shake_fade
        elif m in hit_t:
            text "[m.finaldmg]" anchor (.5,.5) pos m.dmg_pos at shake_fade
    timer 1 action Hide('monster_dmg')

screen player_dmg():
    style_group "dmg"
    for p in battle_players:
        if p in missed_t:
            text "[misstext]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
        elif p in hit_t:
            text "[m_damage]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
        elif p in skill_t:
            if radar_block:
                add "radar" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
                text "[skilltext]" anchor (.5,.5) xpos p.dmg_pos ypos 800 at shake_fade
    timer 1 action Hide('player_dmg')
