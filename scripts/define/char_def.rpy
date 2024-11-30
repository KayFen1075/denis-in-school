init python:
    import copy
    class Char(object):
        def __init__(self, name, img="player", debility=0, need_debility=2, atk=7, dfn=0, lvl=1, exp=0, hpmax=60, mpmax=100, skills={"старт":None,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None, 'weapon': None, 'armor': None, 'accessory': None},effects=[], turn=False, defending=False,
        dead=False, bonus_atk=0, bonus_dfn=0, img_pos=0, bar_pos=0, dmg_pos=0):
            self.name = name
            self.img = img
            self.atk = atk
            self.dfn = dfn
            self.lvl = lvl
            self.debility = debility
            self.need_debility = need_debility
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
            self.effects = effects
            self.dead = dead
            self.bonus_atk = bonus_atk
            self.bonus_dfn = bonus_dfn
            self.img_pos = img_pos
            self.bar_pos = bar_pos
            self.dmg_pos = dmg_pos

        @property
        def iamge(self):
            return 'images/effects/' + self.img + '.png'

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

        def addSkill(self, skill, slot):
            self.skills[slot] = skill

        def addEquip(self, slot, item):
            if self.equip[slot] is None:
                self.equip[slot] = item
                player_inv.drop(item, 1)
                if isinstance(item, Weapon):
                    self.bonus_atk += item.damage
                elif isinstance(item, Armor):
                    self.bonus_dfn += item.defense
                elif isinstance(item, Accessory):
                    self.bonus_atk += item.bonus.get('atk', 0)
                    self.bonus_dfn += item.bonus.get('def', 0)
            else:
                if isinstance(self.equip[slot], Weapon):
                    self.bonus_atk -= self.equip[slot].damage
                    self.bonus_atk += item.damage
                elif isinstance(self.equip[slot], Armor):
                    self.bonus_dfn -= self.equip[slot].defense
                    self.bonus_dfn += item.defense
                elif isinstance(self.equip[slot], Accessory):
                    self.bonus_atk -= self.equip[slot].bonus.get('atk', 0)
                    self.bonus_dfn -= self.equip[slot].bonus.get('def', 0)
                    self.bonus_dfn += item.bonus.get('def', 0)
                    self.bonus_atk += item.bonus.get('atk', 0)
                player_inv.take(self.equip[slot], 1)
                player_inv.drop(item)
                self.equip[slot] = item
                if isinstance(item, Armor) or isinstance(item, Accessory):
                    if getattr(item, 'skill', None) is not None:
                        self.addSkill(None, 'предмет')

        def removeEquip(self, slot, item):
            if self.equip[slot] is not None:
                player_inv.take(self.equip[slot], 1)
                if isinstance(item, Weapon):
                    self.bonus_atk -= item.damage
                elif isinstance(item, Armor):
                    self.bonus_dfn -= item.defense
                elif isinstance(item, Accessory):
                    self.bonus_atk -= item.bonus.get('atk', 0)
                    self.bonus_dfn -= item.bonus.get('def', 0)
                if isinstance(item, Armor) or isinstance(item, Accessory):
                    if getattr(item, 'skill', None) is not None:
                        self.addSkill(None, 'предмет')
                self.equip[slot] = None

define character.p1 = Character("p1")
default p1 = Char("p1")
define character.p2 = Character("p2")
default p2 = Char("p2")

define character.a = Character("[name]", image="[name]")
default a = Char("[name]", img="[img_player]", p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.sasha = Character("Саша", image="sasha")
default sasha = Char("Саша", lvl=1, hpmax=30, img="sasha", mpmax=110, skills={"старт":doubleattack,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.boris = Character("Борис", image="boris")
default boris = Char("Борис", lvl=1, hpmax=70, img="boris", mpmax=0, skills={"старт":None,"предмет":None,"свиток":None}, atk=20, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.maks = Character("Макс", image="mq see")
default maks = Char("Макс", lvl=1, hpmax=25, img="maks", mpmax=140, skills={"старт":circleofhealing,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.lox = Character("Кирилл", image="lox")
default lox = Char("Кирилл", lvl=19, hpmax=57, img="lox", mpmax=100, skills={"старт":None,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.sanek = Character("Санёк", image="sanek")
default sanek = Char("Санёк", lvl=26, hpmax=86, img="sanek", mpmax=170, skills={"старт":attackall,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.tanka = Character("Тянка", image="tanka")
default tanka = Char("Тянка", lvl=11, hpmax=54, img="tanka", mpmax=90, skills={"старт":spikeshield,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})

define character.maksim = Character("Любимый", image="maksim")
default maksim = Char("Любимый", lvl=11, hpmax=54, img="maksim", mpmax=95, skills={"старт":loved,"предмет":None,"свиток":None}, p_skills=[], equip={'оружие': None, 'head': None, 'броня': None, 'аксессуар': None})