init python:
    def atkAll():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        for t in battle_monsters:
            if not t.dead:
                if accFormula(currentplayer, t):
                    dmgFormula(t)
                    t._hp -= t.finaldmg
                    t._mp -= mpdmg
        renpy.show_screen("monster_dmg")
        renpy.with_statement(s_trans)

    def atkRow():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        for t in picked_targs:
            if accFormula(currentplayer, t):
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(s_trans)

    def atkEnemy():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            if accFormula(currentplayer, t):
                dmgFormula(t)
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(s_trans)
                afterFX(b_skill, t)

    def atkAlly():
        for t in picked_targs:
            renpy.play(atk_sfx)
            renpy.pause(0.2, hard=True)
            t._hp -= damage
            t._mp -= mpdmg
            renpy.with_statement(s_trans)

    def atkSelf():
        renpy.play(atk_sfx)
        renpy.pause(0.2, hard=True)
        currentplayer._hp -= damage
        currentplayer._mp -= mpdmg
        renpy.with_statement(s_trans)

    def Defend():
        currentplayer.defending = True
        renpy.play("audio/battle/skills/defend.ogg")
        renpy.with_statement(vpunch)

    def accFormula(a, d):
        global miss_roll
        global message
        global atk_sfx
        global damage

        misschance = 0
        if d.debility > 0:
            deb_multiplier = min(1, d.debility / d.need_debility)
            misschance = 10 * (1 - deb_multiplier) 

        accuracy = 10 - int(misschance * 0.7)
        miss_roll = renpy.random.randint(1, 10)

        if miss_roll > accuracy:
            missed_t.append(d)
            renpy.play(sfx_whoosh.draw())
            renpy.show_screen("monster_dmg")
            return False
        else:
            return True

    def dmgFormula(m):
        global damage
        global effects
        m.effects += effects

        pre_dmg = int(damage*1.1 - (damage * renpy.random.randint(1, 20) / 100))
        m.finaldmg = math.ceil(int(pre_dmg*(100/(100+m.dfn))))
        hit_t.append(m)
        
    def accFormula(a, d):
        global miss_roll
        global message
        global atk_sfx
        global damage
        misschance = 0
        if atk_sfx == "audio/battle/skills/lovedefence.ogg":
            misschance = 0
        elif d.debility > 0:
            deb_multiplier = min(1, d.debility / d.need_debility)
            misschance = 10 * (1 - deb_multiplier) 
        elif d.lvl > a.lvl:
            misschance = d.lvl - a.lvl
        accuracy = 10 - int(misschance*0.7)
        miss_roll = renpy.random.randint(1, 10)
        if miss_roll > accuracy:
            missed_t.append(d)
            renpy.play(sfx_whoosh.draw())
            renpy.show_screen("monster_dmg")
            return False
        else:
            return True

    def Attack():
        global damage
        global message
        global msg_mons
        global effects
        for t in picked_targs:
            damage = currentplayer.atk + currentplayer.bonus_atk
            msg_mons = t.name
            message = "attack_skill"
            renpy.play("audio/battle/skills/sword.ogg")
            renpy.pause(0.2, hard=True)
            if accFormula(currentplayer, t):
                t.state = "hit"
                dmgFormula(t)
                t.effects += effects
                t._hp -= t.finaldmg
                t._mp -= mpdmg
                renpy.show_screen("monster_dmg")
                renpy.with_statement(hpunch)
                renpy.pause(0.2)
                t.state = None

    def expFormula():
        global players
        global curr_exp
        global monsters_total
        global curr_money
        curr_exp = 0
        playersCnt()
        for m in battle_monsters:
            if monsters_total > 0:
                curr_exp += m.exp
                monsters_total -= 1
        curr_money = math.ceil((curr_exp * a.lvl) / 3)
        curr_exp = math.ceil((curr_exp * a.lvl) / players)
        player_inv.money += curr_money
        ach_cash_1000.progress(player_inv.money)
        ach_cash_10000.progress(math.ceil(player_inv.money/1000))
        ach_cash_inf.progress(math.ceil(player_inv.money/1000))

        renpy.say(None, "За этот бой вы заработали [curr_money] грывни")
        for p in battle_players:
            if p.hp > 0:
                renpy.play("audio/game/exp.ogg")
                if p.lvl == 60:
                    ach_max_level.grant()
                if p.lvl <= max_level:
                    p.exp += curr_exp
                    renpy.say(None, "%s получил %i опыта!" % (p.name, curr_exp))
                    while p.exp >= (p.lvl+1)**3:
                        if p.lvl >= max_level:
                            break
                        p.lvl += 1
                        p.hpmax += math.ceil((5 / (p.lvl/2)))
                        renpy.play("audio/game/lvlup.ogg")
                        renpy.say(None, "%s получил %i уровень!" % (p.name, p.lvl))
                else:
                    renpy.say(None, "{0} имеет максимальный уровень!".format(p.name))