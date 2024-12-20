label load_monsters:
    # var = Monster(name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim, skills)
    $ empty = Monster(None, None, None, None, None, None, None, None, dead=True)
    
    # Лес 1
    $ mon1 = Monster("Слайм", 13, 4, 1.5, 10, 3, "1", "water", anim=squeeze, skills=[])
    $ mon2 = Monster("Муха цц", 6, 5, 1.0, 35, 5, "2", "pound", anim=idle_y, skills=[arrowhail])
    $ mon3 = Monster("Огненный шар", 9, 12, 3.0, 50, 7, "3", "fire", anim=idle_shake, skills=[mindfire])

    # Лес 2
    $ mon4 = Monster("Шкафчик", 20, 30, 6.0, 65, 9, "4", "water", anim=idle_y, skills=[devastationbeam])
    $ mon5 = Monster("Крепкий орешик", 47, 17, 14.0, 80, 11, "5", "thunder", anim=idle_xy, skills=[mindfire])
    $ mon6 = Monster("Злой слайм", 13, 20, 9.0, 30, 3, "6", "fire", anim=idle_x, skills=[])
    
    # Лес 3
    $ mon7 = Monster("Сенсей", 50, 30, 15.0, 45, 18, "7", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon8 = Monster("Червячёк)))", 65, 35, 17.0, 50, 19, "8", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon9 = Monster("БЛЯТЬ НЕГР", 80, 40, 20.0, 60, 22, "9", "leaf", anim=idle_xy, skills=[lavaburst])
    
    # Лес 4
    $ mon10 = Monster("ZELEBOBA", 333, 60, 26.0, 150, 27, "10", "water", anim=idle_shake, skills=[arrowhail, deathmissile, lavaburst, swordofdeath])

    # Данж 1
    $ mon11 = Monster("Морская лоли", 100, 50, 30.0, 70, 25, "11", "cut", anim=idle_shake, skills=[spikeshield])
    $ mon12 = Monster("Слизень лоли", 110, 55, 33.0, 75, 27, "12", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon13 = Monster("Спортивная лоли", 120, 60, 35.0, 65, 29, "13", "leaf", anim=idle_xy, skills=[lavaburst])
    
    # Данж 2
    $ mon14 = Monster("Кошка девочка", 110, 70, 40.0, 80, 30, "14", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon15 = Monster("Зачик лоли", 130, 75, 43.0, 85, 33, "15", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon16 = Monster("Рыба фонарь", 160, 80, 45.0, 90, 35, "16", "leaf", anim=idle_xy, skills=[lavaburst])

    # Данж 3
    $ mon17 = Monster("Лоли танк", 265, 85, 47.0, 95, 36, "17", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon18 = Monster("Монахиня лоли", 185, 125, 50.0, 100, 39, "18", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon19 = Monster("Анальные шарики лоли", 165, 110, 55.0, 120, 42, "19", "leaf", anim=idle_xy, skills=[lavaburst])

    # Данж 4
    $ mon20 = Monster("Генерал лоли", 666, 200, 66.0, 500, 55, "20", "cut", anim=idle_shake, skills=[rockthrow])
    # Финал
    $ denis = Monster("Денис", 998, 190, 70.0, 998, 100, "21", "water", need_debility=5, anim=idle_x, skills=[souldrain, mindfreeze, mindfire, arrowhail, lavaburst, swordofdeath, spikeshield])
    $ ui22 = Monster("Великое божество Юй", 999, 200, 80.0, 999, 100, "22", "water", need_debility=3, anim=idle_x, skills=[souldrain, mindfreeze, mindfire, arrowhail, lavaburst, swordofdeath, spikeshield])
    return


init python:
    class Monster(object): 
        def __init__(self, name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, def_dfn=0, anim=idle_shake, debility=0, need_debility=2, skills=[], state=None,effects=[], dead=False, finaldmg=0, slot=1, sprite_pos=0, dmg_pos=(0,0)):
            xpdiff = 0.6
            dmgdiff = 0.6
            rewardX = 0.8
            if persistent.difficulty == 2:
                xpdiff = 1
                dmgdiff = 1
                rewardX = 1
            elif persistent.difficulty == 3:
                xpdiff = 1.3
                dmgdiff = 1.2
                rewardX = 1.4
            elif persistent.difficulty == 4:
                xpdiff = 2
                dmgdiff = 1.6
                rewardX = 1
            
            self.name = name
            self.hpmax = hpmax
            self._hp = 0
            self._mp = 0
            self.debility = debility
            self.need_debility = need_debility
            self.effects = effects
            self.atk = atk
            self.dfn = dfn
            self.def_dfn = dfn
            #self.vel = vel
            self.state = state
            self.lvl = lvl
            self.exp = exp
            self.dead = dead
            self.skills = skills
            self.img = img
            self.sfx_atk = sfx_atk
            #self.sfx_cry = sfx_cry
            #self.sfx_die = sfx_die
            self.finaldmg = finaldmg
            self.slot = slot
            self.anim = anim
            self.sprite_pos = sprite_pos
            self.dmg_pos = dmg_pos
            #self.rarity = rarity
            if not name == None:
                self.hpmax = hpmax * xpdiff
                self.atk = atk * dmgdiff
                self.exp = exp * rewardX
                
        @property
        def hp(self):
            value = self._hp
            
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp
