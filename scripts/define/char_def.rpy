init python:
    import copy
    class Char(object):
        def __init__(self, name, img="player", atk=5, dfn=0, lvl=1, exp=0, hpmax=60, mpmax=100, skills=[], p_skills=[], equip={'hand': None, 'head': None, 'chest': None, 'accs': None},
        condition={'burn': False, 'freeze': False, 'paral': False, 'poison': False, 'sleep': False, 'stun': False, 'confus': False, 'wound': False, 'rage': False}, turn=False, defending=False,
        dead=False, bonus_atk=0, bonus_dfn=0, img_pos=0, bar_pos=0, dmg_pos=0):
            self.name = name
            self.img = img
            self.atk = atk
            self.dfn = dfn
            self.lvl = lvl
            self.exp = exp
            self.hpmax = hpmax
            self._hp = 60
            self.mpmax = mpmax
            self._mp = 100
            self.skills = skills
            self.p_skills = p_skills
            self.equip = equip
            self.turn = turn
            self.defending = defending
            self.condition = condition
            self.dead = dead
            self.bonus_atk = bonus_atk
            self.bonus_dfn = bonus_dfn
            self.img_pos = img_pos
            self.bar_pos = bar_pos
            self.dmg_pos = dmg_pos
        @property
        def hp(self):
            value = self._hp
            if not ( 0 <= value <= self.hpmax ):
                value = max( 0, min( self.hpmax, value ) )
                self._hp = value
            return self._hp
        @property
        def mp(self):
            value = self._mp
            if not ( 0 <= value <= self.mpmax ):
                value = max( 0, min( self.mpmax, value ) )
                self._mp = value
            return self._mp

        def addEquip(self, slot, item):
            if self.equip[slot] == None:
                self.equip[slot] = item
                renpy.say(None, "You equipped {0}.".format(self.equip[slot]))
            else:
                renpy.say(None, "Replacing {0} for {1}.".format(self.equip[slot],item))
        def removeEquip(self, slot, item):
            renpy.say(None, "Removed {0}.".format(self.equip[slot]))
            self.equip[slot] = None
        


define character.p1 = Character("p1")
default p1 = Char("p1")
define character.p2 = Character("p2")
default p2 = Char("p2")

define character.a = Character("[name]", image="[name]")
default a = Char("[name]", img="[img_player]", skills=[], p_skills=[passive1], equip={'hand': "Bow", 'head': None, 'chest': None, 'accs': None})

define character.sasha = Character("Саша", image="maks")
default sasha = Char("Саша", lvl=1, hpmax=110, img="maks", skills=[lifedrain], p_skills=[radar], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.maks = Character("Макс", image="mq see")
default maks = Char("Макс", lvl=1, hpmax=75, img="maks", skills=[circleofhealing, magicheal], p_skills=[passive2], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.k = Character("Кирилл", image="lox")
default lox = Char("Кирилл", lvl=1, hpmax=90, img="lox", skills=[], p_skills=[passive1], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})

define character.sanek = Character("Санёк", image="sanek")
default sanek = Char("Санёк", lvl=46, hpmax=650, img="sanek", skills=[souldrain, giftofangels, mindburn, attackall], p_skills=[radar], equip={'hand': None, 'head': None, 'chest': None, 'accs': None})