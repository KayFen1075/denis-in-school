label load_monsters:
    # var = Monster(name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim, skills)
    $ empty = Monster(None, None, None, None, None, None, None, None, dead=True)
    
    # Лес 1
    $ mon1 = Monster("Слайм", 13, 4, 1.5, 10, 3, "1", "water", anim=squeeze, skills=[])
    $ mon2 = Monster("Муха цц", 6, 5, 1.0, 35, 5, "2", "pound", anim=idle_y, skills=[arrowhail])
    $ mon3 = Monster("Огненный шар",9, 12, 3.0, 50, 7, "3", "fire", anim=idle_shake, skills=[mindfire])

    # Лес 2
    $ mon4 = Monster("Шкафчик", 20, 30, 6.0, 65, 9, "4", "water", anim=idle_y, skills=[devastationbeam])
    $ mon5 = Monster("Крепкий орешик", 47, 17, 14.0, 80, 11, "5", "thunder", anim=idle_xy, skills=[mindfire])
    $ mon6 = Monster("Злой слайм", 13, 15, 9.0, 30, 3, "6", "fire", anim=idle_x, skills=[swordofdeath])
    
    # Лес 3
    $ mon7 = Monster("Сенсей", 50, 30, 15.0, 45, 18, "7", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon8 = Monster("Червячёк)))", 65, 35, 10.0, 50, 19, "8", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon9 = Monster("БЛЯТЬ НЕГР", 80, 40, 10.0, 60, 22, "9", "leaf", anim=idle_xy, skills=[lavaburst])
    
    # Лес 4
    $ mon10 = Monster("ZELEBOBA", 333, 60, 6.0, 150, 27, "10", "water", anim=idle_shake, skills=[arrowhail, deathmissile, lavaburst, swordofdeath])

    # Данж 1
    $ mon11 = Monster("Морская лоли", 100, 50, 10.0, 70, 25, "11", "cut", anim=idle_shake, skills=[spikeshield])
    $ mon12 = Monster("Слизень лоли", 110, 55, 10.0, 75, 27, "12", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon13 = Monster("Спортивная лоли", 120, 60, 12.0, 65, 29, "13", "leaf", anim=idle_xy, skills=[lavaburst])
    
    # Данж 2
    $ mon14 = Monster("Кошка девочка", 110, 60, 15.0, 80, 30, "14", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon15 = Monster("Зачик лоли", 130, 65, 10.0, 85, 33, "15", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon16 = Monster("Рыба фонарь", 160, 70, 20.0, 90, 35, "16", "leaf", anim=idle_xy, skills=[lavaburst])

    # Данж 3
    $ mon17 = Monster("Лоли танк", 265, 75, 15.0, 95, 36, "17", "cut", anim=idle_shake, skills=[rockthrow])
    $ mon18 = Monster("Монахиня лоли", 185, 125, 10.0, 100, 39, "18", "scratch", anim=idle_shake, skills=[mindburn])
    $ mon19 = Monster("Анальные шарики лоли", 165, 110, 20.0, 120, 42, "19", "leaf", anim=idle_xy, skills=[lavaburst])

    # Данж 4
    $ mon20 = Monster("Генерал лоли", 666, 100, 20.0, 500, 55, "20", "cut", anim=idle_shake, skills=[rockthrow])
    # Финал
    $ denis = Monster("Денис", 998, 85, 23.0, 998, 100, "21", "water", need_debility=5, anim=idle_x, skills=[souldrain, mindfreeze, mindfire, arrowhail, lavaburst, swordofdeath, spikeshield])
    $ ui22 = Monster("Великое божество Юй", 999, 70, 15.0, 999, 100, "22", "water", need_debility=3, anim=idle_x, skills=[souldrain, mindfreeze, mindfire, arrowhail, lavaburst, swordofdeath, spikeshield])
    return

init python:
    class Monster(object):
        def __init__(self, name, hpmax, atk, dfn, exp, lvl, img, sfx_atk, anim=idle_shake, debility=0, need_debility=2, skills=[], state=None, dead=False, finaldmg=0, slot=1, sprite_pos=0, dmg_pos=(0,0)):
            self.name = name
            self.hpmax = hpmax
            self._hp = 0
            self._mp = 0
            self.debility = debility
            self.need_debility = need_debility
            self.atk = atk
            self.dfn = dfn
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
        @property
        def hp(self):
            value = self._hp
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp
