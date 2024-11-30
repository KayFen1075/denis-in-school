init python:
    def monsterTurns():
        global message
        global battleEnd
        global hit_t
        global missed_t
        global skill_t
        global msg_mons
        global atk_sfx
        global use_skill
        global damage
        global effects
        global rage_attack
        rage_attack = False
        for m in battle_monsters:
            hit_t = []
            missed_t = []
            effects = []
            skill_t = []
            use_skill = False
            if not m.dead:
                message = "none"
                skip_turn = False
                for e in m.effects:
                    print('есть эффекты')
                    c = e.condition
                    print(c)
                    if c['огонь']:
                        damage = c['огонь']['урон'] * random.randint(0.8,1.2)
                        dmgFormula(m)
                        if e.mathXd('огонь'):
                            m.effects.remove(e)
                    if c['отравление']:
                        if e._hp > c['отравление']['урон']:
                            damage = c['отравление']['урон']
                            dmgFormula(m)
                        if e.mathXd('отравление'):
                            m.effects.remove(e)
                    if c['кровотичение']:
                        damage = c['кровотичение']['урон']
                        dmgFormula(m)
                        if e.mathXd('кровотичение'):
                            m.effects.remove(e)
                    if c['ярость']:
                        rage_attack = c['ярость']['урон']
                        rage_attack = True
                        if e.mathXd('ярость'):
                            m.effects.remove(e)
                    if c['здоровье']:
                        m._hp += c['здоровье']['урон']
                        if e.mathXd('здоровье'):
                            m.effects.remove(e)
                    if c['мана']:
                        if e.mathXd('мана'):
                            effects.remove(e)
                    if c['защита']:
                        m.dfn = m.def_dfn+c['защита']['урон']
                        if e.mathXd('защита'):
                            m.dfn = m.def_dfn
                            m.effects.remove(e)
                    if c['заморозка']:
                        print("Заморозка")
                        if e.mathXd('заморозка'):
                            m.effects.remove(e)
                        skip_turn = True
                if skip_turn:
                    continue
                print('всё хуйня')
                # if condition.burn:
                #     damage = condition.burn.damage
                #     dmgFormula(m)
                #     if condition.burn.xd > 0:
                #         condition.burn.xd -= 1
                #     else:
                #         condition.burn = False
                # if condition.freeze:
                #     if condition.freeze.xd > 0:
                #         m.state = None
                #         condition.freeze.xd -= 1
                #         return playersChk()
                #     else:
                #         condition.freeze = False
                # if condition.rage:
                #     if condition.rage.xd > 0:
                #         rage_attack = condition.rage.damageX 
                #         condition.rage.xd -= 1
                #     else:
                #         condition.rage = False
                if not battleEnd:
                    monsterTarg(m)
                    renpy.play(sfx_whoosh.draw())
                    renpy.pause(0.3, hard=True)
                    renpy.play(atk_sfx)
                    msg_mons = m.name
                    if use_skill:
                        msg_skill = b_skill.name
                        message = "m_skill"
                    else:
                        message = "m_atk"
                    for t in picked_targs:
                        monsterAtk(m, t)

                    m.state = None
                    renpy.show_screen("player_dmg")
                    renpy.pause(0.2, hard=True)
                    renpy.pause(0.5)
                    renpy.hide_screen("player_dmg")
                    playersChk()
        spawnMst(mon12)
        if len(battle_monsters)<=3 and len(reserve_monsters)>0:
            spawnMst(mon12)
    def monsterTarg(m):
        global picked_targs
        global alive_players
        global atk_sfx
        global b_skill
        global use_skill
        global roll_target
        playersCnt()
        targs = 1
        picked_targs = []
        atk_sfx = "audio/battle/monsters/" + m.sfx_atk + ".ogg"
        if m.skills:
            use_skill = renpy.random.choice([True, False, False])
            if use_skill:
                b_skill = renpy.random.choice(m.skills)
                b_skill.useSkill(monster=m)
                if b_skill.targ == "all":
                    picked_targs = alive_players
                    return
                else:
                    targs = b_skill.targs
        while targs > 0:
            roll_target = renpy.random.choice(alive_players)
            picked_targs.append(roll_target)
            targs -= 1

    def monsterAtk(m, p):
        global hit_t
        global missed_t
        global rage_attack
        m.state = "attacking"
        monsterDmg(m, p)
        if accFormula(m, p):
            if skillChk(p):
                hit_t.append(p)
                if rage_attack:
                    p._hp -= math.ceil(m_damage*rage_attack)
                else:
                    p._hp -= math.ceil(m_damage)
                roll_shake = renpy.random.randint(1,2)
                if roll_shake == 1:
                    renpy.with_statement(hpunch)
                if roll_shake == 2:
                    renpy.with_statement(vpunch)

    def monsterDmg(m, p):
        global roll_target
        global m_damage
        global damage
        global currdmg
        global use_skill
        turnbonus = 0
        if use_skill:
            currdmg = damage
        else:
            currdmg = int(m.atk*1.1 - (m.atk * renpy.random.randint(1,20) / 100))
        if p.defending == True:
            turnbonus += 1*p.lvl
            renpy.play("audio/battle/skills/block.ogg")
        m_damage = math.ceil(currdmg*currdmg/(currdmg+p.dfn+p.bonus_dfn+turnbonus))

    def spawnMst(m):
        print('ВСЁ ЗАЕБИСЛ')
        monster_slot[0] = m
        battle_monsters.append(m)
        asignPos()
        

    def monsterImg(m):
        if m.state == "attacking":
            return im.MatrixColor(getImage(m), im.matrix.tint(1,.5,.5))
        if m.state == "hit":
            return im.MatrixColor(getImage(m), im.matrix.tint(1,.5,.5))
        if m.state == "heal": # green
            return im.MatrixColor(getImage(m), im.matrix.tint(.5,1,.5))
        if m.state == "dying":
            return im.MatrixColor(getImage(m), im.matrix.invert())
        if m.state == "other": # blue
            return im.MatrixColor(getImage(m), im.matrix.tint(.5,.5,1))
        if m.state == "other2": # hue
            return im.MatrixColor(getImage(m), im.matrix.hue(90))
        else:
            return getImage(m)
