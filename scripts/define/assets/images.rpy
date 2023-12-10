$ bb = 1

image battle_background = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "bb == 1", "images/bg/1.png",
    "bb == 2","images/bg/2.png")

image sasha_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "sasha.dead or a.name == 'Саша' and a.dead","images/char/dead/maks_dead.png",
    "not sasha.dead or a.name == 'Саша' and not a.dead", "images/char/sasha_battle.png")

image maks_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "maks.dead or a.name == 'Макс' and a.dead ","images/char/dead/maks_dead.png",
    "not maks.dead or a.name == 'Макс' and not a.dead", "images/char/maks_battle.png")

image lox_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "lox.dead or a.name == 'Кирилл' and a.dead ","images/char/dead/lox_dead.png",
    "not lox.dead or a.name == 'Кирилл' and not a.dead", "images/char/lox_battle.png")

image maksim_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "maksim.dead","images/char/dead/maksim_dead.png",
    "not maksim.dead", "images/char/maksim_battle.png")

image tank_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "tank.dead","images/char/dead/tank_dead.png",
    "not tank.dead", "images/char/tank_battle.png")

image sanek_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "sanek.dead","images/char/dead/sanek_dead.png",
    "not sanek.dead", "images/char/sanek_battle.png")

image boris_battle = TransitionConditionSwitch(Dissolve(0.5, alpha=True),
    "boris.dead","images/char/dead/boris_dead.png",
    "not boris.dead", "images/char/boris_battle.png")