init python:
    class Effect:
        def __init__(self, name, desc, icon=False, tags={}, condition={}):
            # Шаблон всех возможных состояний
            base_conditions = {
                'огонь': False, 'заморозка': False, 'воскревший': False,
                'отравление': False, 'сон': False, 'стан': False,
                'путаница': False, 'кровотичение': False, 'ярость': False,
                'здоровье': False, 'мана': False, 'защита': False,
                'бонусная_атака': False
            }

            # Обновляем базовые состояния переданными значениями
            base_conditions.update(condition)

            self.name = name
            self.desc = desc
            self.icon = icon
            self.tags = tags
            self.condition = base_conditions

        @property
        def getImage(self):
            return 'images/effetcs/' + self.icon

        @property
        def огонь(self):
            return self.condition['огонь']
        @property
        def заморозка(self):
            return self.condition['заморозка']
        @property
        def воскрвший(self):
            return self.condition['воскревший']
        @property
        def отравление(self):
            return self.condition['отравление']
        @property
        def сон(self):
            return self.condition['сон']
        @property
        def стан(self):
            return self.condition['стан']
        @property
        def путаница(self):
            return self.condition['путаница']
        @property
        def кровотичение(self):
            return self.condition['кровотичение']
        @property
        def ярость(self):
            return self.condition['ярость']
        @property
        def здоровье(self):
            return self.condition['здоровье']
        @property
        def мана(self):
            return self.condition['мана']
        @property
        def защита(self):
            return self.condition['защита']
        @property
        def бонусная_атака(self):
            return self.condition['бонусная_атака']

        def changeCondition(self, condition, value):
            self.condition[condition] = value

        def changeConditionProp(self, condition, prop, value):
            self.condition[condition][prop] = value

        def mathXd(self, condition):
            # if not self.condition[condition].get('ходов'):
                # print('полная хуйня')
                # return False
            if self.condition[condition]['ходов'] > 0:
                print('минус')
                self.condition[condition]['ходов'] -= 1
            if self.condition[condition]['ходов'] <= 0:
                print('смерть')
                self.condition[condition] = False

            return all(value is False for value in self.condition.values())


            
define огонь = Effect('Горит', 'Подожённый будет гореть', 'fire.png', condition={'огонь': {'урон': 10, 'ходов': 3}})
define заморозка = Effect('Заморожен', 'Замороженный не сможет ходить', 'ice.png', condition={'заморозка': {'ходов': 2}})
define воскревший = Effect('Воскрешён', 'Эффект стакается при каждом воскришении, делая носителя слабее', 'resurrect.png', condition={'воскрвший': {'stack': 1}})
define отравление = Effect('Отравлен', 'Отравленный будет терять здоровье каждый ход. При этом это не может убить врага', 'poison.png', condition={'отравление': {'урон': 5, 'ходов': 3}})
define сон = Effect('Спит', 'Спящий не может ходить', 'sleep.png', condition={'сон': {'ходов': 2}})
define стан = Effect('Оглушен', 'Оглушенный не может ходить', 'stun.png', condition={'стан': {'ходов': 1}})
define путаница = Effect('Путан', 'Путаный атакует случайного персонажа', 'confusion.png', condition={'путаница': {'ходов': 2}})
define кровотичение = Effect('Кровотечение', 'Кровотечение наносит урон каждый ход', 'bleed.png', condition={'кровотичение': {'урон': 5, 'ходов': 3}})
define ярость = Effect('Ярость', 'Ярость увеличивает атаку', 'rage.png', condition={'ярость': {'урон': 5, 'ходов': 3}})
define здоровье = Effect('Здоровье', 'Увеличивает максимальный запас здоровья', 'health.png', condition={'здоровье': {'урон': 20, 'ходов': 3}})
define мана = Effect('Мана', 'Увеличивает максимальный запас маны', 'mana.png', condition={'мана': {'урон': 20, 'ходов': 3}})
define защита = Effect('Защита', 'Увеличивает защиту', 'defence.png', condition={'защита': {'урон': 20, 'ходов': 3}})
define бонусная_атака = Effect('Бонусная атака', 'Даёт дополнительную атаку', 'attack.png', condition={'бонусная_атака': {'ходов': 3}})
