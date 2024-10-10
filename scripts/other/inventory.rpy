init python:
    import renpy.store as store
    import math
    
    class Item(store.object):
        def __init__(self, name, desc, cost, icon=False, skill=False, value=0, dependencies=[], act=Show("inventory_popup", message="Nothing happened!"), type="item", recipe=False, tags={}):
            global cookbook
            self.name = name
            self.desc = desc
            self.cost = cost 
            self.icon = icon
            self.skill = skill
            self.value = value
            self.dependencies = dependencies
            self.act = act # screen action
            self.type = type # type of item
            self.recipe = recipe # nested list of [ingredient, qty]
            self.tags = tags

            if recipe:
                cookbook.append(self)
                cookbook.sort(key=lambda i: i.name) #alpha order

        def change(self, name, desc=False, icon=False, value=False, act=False, recipe=False):
            self.name = name
            if desc:
                self.desc = desc
            if icon:
                self.icon = icon
            if value:
                self.value = value
            if act:
                self.act = act
            if recipe:
                self.recipe = recipe

    class Armor(Item):
        def __init__(self, name, desc, cost, defense, skill=False, icon=False, value=0, dependencies=[], act=Show("inventory_popup", message='as'), type="броня", recipe=False, tags={}):
            super().__init__(name, desc, cost, icon, value, act, type, recipe, tags)
            self.cost = cost
            self.defense = defense
            self.skill = skill
            self.type = "броня"
            self.act = Show("inventory_popup", message=self.type)
            self.inventory_item = Item(name, desc, cost, icon, value, act, "броня", recipe, tags)
            self.dependencies = dependencies

    class Weapon(Item):
        def __init__(self, name, desc, cost, damage, skill=False, icon=False, value=0, dependencies=[], act=Show("inventory_popup", message="Nothing happened!"), type="оружие", recipe=False, tags={}):
            super().__init__(name, desc, cost, icon, value, act, type, recipe, tags)
            self.cost = cost
            self.damage = damage
            self.skill = skill
            self.type = "оружие"
            self.act = Show("inventory_popup", message=self.type)
            self.inventory_item = Item(name, desc, cost, icon, value, act, type, recipe, tags)
            self.dependencies = dependencies

    class Accessory(Item):
        def __init__(self, name, desc, cost, bonus, icon=False, skill=False, value=0, dependencies=[], act=Show("inventory_popup", message="Nothing happened!"), type="аксессуар", recipe=False, tags={}):
            super().__init__(name, desc, cost, icon, value, act, type, recipe, tags)
            self.cost = cost
            self.bonus = bonus
            self.act = Show("inventory_popup", message=self.type)
            self.inventory_item = Item(name, desc, cost, icon, value, act, "аксессуар", recipe, tags)
            self.dependencies = dependencies
            self.skill = skill
            self.type = "аксессуар"


    class Inventory(store.object):
        def __init__(self, name, money=0, barter=100):
            self.name = name
            self.money = money
            self.barter = barter #percentage of value paid for items
            self.inv = []  # items stored in nested list [item object, qty]
            self.sort_by = self.sort_name
            self.sort_order = True #ascending, dependencies
            self.grid_view = True

        def buy(self, item):
            if item.name == "Обсидиановый меч":
                global obs_sworlds
                obs_sworlds += 1
                ach_back_to_hell.progress(obs_sworlds)
                if obs_sworlds == 12:
                    renpy.hide_screen('by_item')
                    renpy.hide_screen('shop_menu')
                    renpy.jump('obs_end')
            self.deposit(item.cost*cost_multiplate)
            self.take(item)
            renpy.play("audio/game/buy.ogg")

        def check(self, item):
            if self.qty(item):
                for i in self.inv:
                    if i[0] == item:
                        return self.inv.index(i) # returns item index (location)

        def check_recipe(self, item): # verify all ingredients are in inv
            checklist = list()
            for i in item.recipe:
                if self.qty(i[0]) >= i[1]:
                    checklist.append(True)
            if len(checklist) == len(item.recipe):
                return True
            else:
                return False

        def craft(self, item):
            for line in item.recipe:
                self.drop(line[0], line[1])
            self.take(item)
            message = "Crafted a %s!" % (item.name)
            renpy.show_screen("inventory_popup", message=message)

        def deposit(self, amount):
            self.money -= amount

        def drop(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)
                if self.inv[item_location][1] > qty:
                    self.inv[item_location][1] -= qty
                else:
                    del self.inv[item_location]

        def qty(self, item):
            for i in self.inv:
                if i[0] == item:
                    return i[1] # returns quantity

        def sell(self, item, price):
            self.withdraw(price)
            self.drop(item[0])

        def sort_name(self):
            self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)

        def sort_qty(self):
            self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)

        def sort_value(self):
            self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)

        def take(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)
                self.inv[item_location][1] += qty
            else:
                self.inv.append([item,qty])

        def takes(self, items, qty=1):
            for item in items:
                self.take(item, qty)

        def withdraw(self, amount):
            self.money += amount

    def calculate_price(item, buyer):
        if buyer:
            price = item[0].value * (buyer.barter * 0.01)
            return int(price)

    def money_transfer(depositor, withdrawer, amount):
        if depositor.money >= amount:
            depositor.deposit(amount)
            withdrawer.withdraw(amount)
        else:
            message = "Sorry, %s doesn't have %d!" % (buyer.name, amount)
            renpy.show_screen("inventory_popup", message=message)

    def trade(seller, buyer, item):
        seller.drop(item[0])
        buyer.take(item[0])

    def transaction(seller, buyer, item):
        price = calculate_price(item, buyer)
        if buyer.money >= price:
            seller.sell(item, price)
            buyer.buy(item, price)
        else:
            message = "Sorry, %s doesn't have enough money!" % (buyer.name)
            renpy.show_screen("inventory_popup", message=message)
    def consume(owner, item):
        owner.drop(item[0])

    transfer_amount = 0

screen by_item(item, baff):
    modal True
    zorder 102
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            style_group "invstyle"
            label "{{image=images/inv/{0}}} Потвердить покупку?".format(item.icon)
            vbox:
                text "{b}[item.name]{/b} {size=25}[baff]{/size}"
                text item.desc 
                text "Цена: {0}₴".format(math.ceil(item.cost*cost_multiplate))
            hbox:
                textbutton "Купить":
                    if player_inv.money >= item.cost*cost_multiplate:
                        action Function(player_inv.buy, item)
                textbutton "Отмена":
                    action Hide("by_item")

screen shop_menu():
    modal True
    zorder 101 
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            style_group "invstyle"
            xsize 1280 ysize 720
            yalign 0
            label "{size=30}Запретный магазин бориса{/size}"
            label "[a.name] имеет {0}₴".format(math.ceil(player_inv.money))
            vbox:
                # Броня
                xalign 0.5
                vbox:
                    xalign 0.5
                    label "Броня"
                    hbox:
                        for item in items:
                            if item.type == "броня":
                                textbutton "{{image=images/inv/{0}}}".format(item.icon) action Show("by_item", None, item, "{0}защ".format(item.defense))
                                text "{0}₴".format(math.ceil(item.cost*cost_multiplate))
                # Оружие
                vbox:
                    xalign 0.5
                    label "Оружие"
                    hbox:
                        for item in items:
                            if item.type == "Оружие":
                                textbutton "{{image=images/inv/{0}}}".format(item.icon) action Show("by_item", None, item, "{0}атк".format(item.damage))
                                text "{0}₴".format(math.ceil(item.cost*cost_multiplate))
                # Артефакты
                vbox:
                    xalign 0.5
                    label "Артефакты"
                    hbox:
                        for item in items:
                            if item.type == "аксессуар":
                                textbutton "{{image=images/inv/{0}}}".format(item.icon) action Show("by_item", None, item, "{0}атк {1}защ".format(item.bonus['atk'], item.bonus['def']))
                                text "{0}₴".format(math.ceil(item.cost*cost_multiplate))
                vbox:
                    xalign 0.5
                    label "Предметы"
                    hbox:
                        for item in items:
                            if item.type == "cons":
                                textbutton "{{image=images/inv/{0}}}".format(item.icon) action Show("by_item", None, item, "")
                                text "{0}₴".format(math.ceil(item.cost*cost_multiplate))
            textbutton "{b}Закрыть{/b}":
                xalign 0.5 yalign 0
                action Hide("shop_menu")
screen magic_shop_menu():
    modal True
    zorder 101 
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            style_group "invstyle"
            xsize 1280 ysize 720
            yalign 0
            label "{size=30}Гримуары древних укров евреев{/size}"
            label "[a.name] имеет {0}₴".format(math.ceil(player_inv.money))
            vbox:
                # Магия
                xalign 0.5
                vbox:
                    xalign 0.5
                    label "Заблокированные свитки"
                    hbox:
                        for magic in magics:
                            textbutton "{{image=images/skills/{0}.png}}".format(magic.img) action Show("by_magic", None, magic, a)
                            text "{0}₴".format(math.ceil(magic.cost))
            textbutton "{b}Закрыть{/b}":
                xalign 0.5 yalign 0
                action Hide("magic_shop_menu")
screen by_magic(magic, player):
    modal True
    zorder 102
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            style_group "invstyle"
            label "{{image=images/skills/{0}.png}} Потвердить покупку?".format(magic.img)
            vbox:
                text "{b}[magic.name]{/b}" 
                text "Цена: {0}₴".format(magic.cost)
            hbox:
                textbutton "Купить":
                    if player_inv.money >= magic.cost:
                        action Call("lb_by_magic", magic)
                textbutton "Отмена":
                    action Hide("by_magic")
screen EquipmentPlayersScreen():
    modal True
    zorder 100
    default full_party = [a] + party_list
    add "battle/blackui.png"
    text "Выбери персонажа" xpos 0.5 ypos 0.54
    for i, char in enumerate(full_party):
        imagebutton:
            idle "images/char/{0}_battle.png".format(char.img)
            xpos (0.8 - 0.09* len(full_party) + 0.10 * i) ypos 1.0
            anchor ('center', 'bottom')
            action Show("EquipmentScreen", None, char), renpy.hide_screen("EquipmentPlayersScreen")
            

screen EquipmentScreen(char):
    modal True
    zorder 101 
    $ xalingpos = 0.45
    $ yalignpos = 0.04
    $ i = 1
    
    add "battle/blackui.png"
    add "images/char/{0}_battle.png".format(char.img) zoom 1.5 xpos 0.12 ypos 0.2
    add "images/battle/inv_bg.png" xpos 0.33 ypos 0.1 zoom 0.9
    text "{size=+30}{b}[char.name]{/b} [char.lvl]lvl" xpos 0.55 ypos 0.18
    imagebutton: 
        xpos 0.23 ypos 0.23
        xsize 192 ysize 192
        if char.equip.get('броня') is not None:
            idle "images/inv/{0}".format(char.equip.get('броня').icon)
        else:
            idle "images/inv/vibrator_sworld.png"
    # Eqp
    
    for slot in ['броня', 'оружие', 'аксессуар']:
        vbox:
            xpos xalingpos ypos 0.35
            hbox:
                text "{0}".format(slot.capitalize())
            hbox:
                ypos 0.4 xpos -1.1
                xsize 10 
                spacing 3
                for item_inv in player_inv.inv:
                    $ name = item_inv[0].name
                    $ icon = item_inv[0].icon
                    $ desc = item_inv[0].desc
                    $ type = item_inv[0].type
                    if type == slot:
                        pass
                        # textbutton "{{image=images/inv/{0}}}".format(icon) action Function(char.addEquip, slot, item_inv[0]), Function(item_inv[0].act)
        
        $ xalingpos += 0.15
        $ i = i + 1



    # for player in party_list:
        # $ i +=1
        # if i > 3:
            # if i == 4:
                # $ yalignpos = 0.95
                # $ xalingpos = 0.25
        # frame:
            # style "neat_frame"
            # xalign xalingpos yalign yalignpos
            # vbox:
                # hbox:
                    # xalign 0.5
                    # text "{sc=1.5}{b}[player.name]{/b} [player.lvl]lvl{/sc}" 
                # hbox:
                    # xalign 0.5
                    # text "Атака: {1}, Защита: {2}".format(player.name, player.atk+player.bonus_atk, player.dfn+player.bonus_dfn) size 15 
                # hbox:
                    # xalign 0.5
                    # text "{0}xp / {1}xp".format((player.exp-(player.lvl**3)), (player.lvl+1)**3-(player.lvl)**3) font "fonts/damages.ttf" size 15
                # for slot in ['броня', 'оружие', 'аксессуар']:
                    # vbox:
                        # hbox:
                            # text "{0}:".format(slot.capitalize())
                            # $ item = player.equip.get(slot)
                            # if item is not None:
                                # textbutton "{{image=images/inv/{0}}}".format(item.icon) action Function(player.removeEquip, slot, item)
                        # hbox:
                            # for item_inv in player_inv.inv:
                                # $ name = item_inv[0].name
                                # $ icon = item_inv[0].icon
                                # $ desc = item_inv[0].desc
                                # $ type = item_inv[0].type
                                # if type == slot:
                                    # textbutton "{{image=images/inv/{0}}}".format(icon) action Function(player.addEquip, slot, item_inv[0])
        # if i < 3:
            # $ xalingpos += 0.5
        # else:
            # $ xalingpos += 0.25
    # frame:
        # style "neat_frame"
        # xalign 0.5 yalign 0.03
        # vbox:
            # hbox:
                # xalign 0.5
                # text "{sc=2}{b}[a.name]{/b} [a.lvl]lvl{/sc}"
            # hbox:
                # xalign 0.5
                # text "Атака: {1}, Защита: {2}".format(a.name, a.atk+a.bonus_atk, a.dfn+a.bonus_dfn) size 15
            # hbox:
                # xalign 0.5
                # text "{0}xp / {1}xp".format((a.exp-(a.lvl**3)), (a.lvl+1)**3-(a.lvl)**3) font "fonts/damages.ttf" size 15
            # for slot in ['броня', 'оружие', 'аксессуар']:
                # vbox:
                    # hbox:
                        # text "{0}:".format(slot.capitalize())
                        # $ item = a.equip.get(slot)
                        # if item is not None:
                            # textbutton "{{image=images/inv/{0}}}".format(item.icon) action Function(a.removeEquip, slot, item)
                    # hbox:
                        # for item_inv in player_inv.inv:
                            # $ name = item_inv[0].name
                            # $ icon = item_inv[0].icon
                            # $ desc = item_inv[0].desc
                            # $ type = item_inv[0].type
                            # if type == slot:
                                # textbutton "{{image=images/inv/{0}}}".format(icon) action Function(a.addEquip, slot, item_inv[0])
            # textbutton "{b}Закрыть{/b}":
                # xalign 0.5
                # action Hide("EquipmentScreen")

screen inv_tooltip(item=False,seller=False):
    zorder 101
    if item:
        hbox:
            xalign 0.5 yalign 0.14#0.7
            if seller:
                text ("[item[0].name]: [item[0].desc] (Sell Value: " + str(calculate_price(item, seller)) + ")")
            else:
                text "[item[0].name]: [item[0].desc]"# (Value: [item[0].value])

screen inventory_screen(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = False
    tag menu
    modal True
    zorder 101
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label "{0}, у тебя {1} грывень".format(first_inventory.name, math.ceil(first_inventory.money))
                if second_inventory:
                    use money(first_inventory, second_inventory, bank_mode)
                use inventory_view(first_inventory, second_inventory, trade_mode)
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                #if not second_inventory:
                    #textbutton "Crafting Mode" action ToggleScreenVariable("crafting_screen")
                textbutton "Закрыть" action Hide("inventory_screen")
            if second_inventory:
                vbox:
                    label second_inventory.name
                    use money(second_inventory, first_inventory, bank_mode)
                    use inventory_view(second_inventory, first_inventory, trade_mode)
                    use view_nav(second_inventory)
                    use sort_nav(second_inventory)
            #if crafting_screen:
                #use crafting(first_inventory)

screen inventory_view(inventory, second_inventory=False, trade_mode=False):
    zorder 101
    side "c r":
        style_group "invstyle"
        area (0, 0, 700, 500)
        vpgrid id ("vp"+inventory.name):
            draggable True
            mousewheel True
            xsize 700 ysize 500
            if inventory.grid_view:
                cols 9 spacing 10
            else:
                cols 1 spacing 25
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])
                hbox:
                    if item[0].icon:
                        $ icon = "images/inv/" + item[0].icon#$ icon = item[0].icon
                        $ hover_icon = im.Sepia(icon)
                        imagebutton:
                            idle LiveComposite((50,50), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((50,50), (0,0), hover_icon, (0,0), Text(qty))
                            action (If(not second_inventory, item[0].act, (If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item)))))
                            hovered Show("inv_tooltip",item=item,seller=second_inventory)
                            unhovered Hide("inv_tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                if not trade_mode:
                                    text "Ценность: [value]"
                                    if second_inventory:
                                        text ("Цена: " + str(calculate_price(item, second_inventory)) + ")")

                    else:
                        textbutton "[name] ([qty])" action (If(not second_inventory, item[0].act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("inv_tooltip",item=item,seller=second_inventory) unhovered Hide("inv_tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text "Ценность: [value]"
                                if not trade_mode and second_inventory:
                                    text "Цена: " + str(calculate_price(item, second_inventory)) + ")"

            ## maintains spacing in empty inventories.
            if len(inventory.inv) == 0:
                add Null(height=192,width=192)

        vbar value YScrollValue("vp"+inventory.name)


screen money(inventory, second_inventory, bank_mode=False):
    zorder 101
    hbox:
        style_group "invstyle"
        text "Деньги: [inventory.money]"
        if bank_mode and inventory.money:
            textbutton "Transfer" action Show("banking", depositor=inventory, withdrawer=second_inventory)

screen banking(depositor, withdrawer):
    key "mouseup_3" action Function(renpy.pop_call), Hide("banking")
    modal True
    frame:
        style_group "invstyle"
        vbox:
            label "Money Transfer"
            text "Amount: [transfer_amount]"
            bar value VariableValue("transfer_amount", depositor.money, max_is_zero=False, style='scrollbar', offset=0, step=0.1) xmaximum 200

            hbox: #examples of the types of controls you can set up
                for amount in [50,100,250,depositor.money]:
                    if depositor.money>=amount:
                        textbutton str(amount) action SetVariable("transfer_amount", amount)
            hbox:
                textbutton "Transfer" action [Function(money_transfer, depositor, withdrawer, transfer_amount), SetVariable("transfer_amount", 0), Hide("banking")]
                textbutton "Cancel" action Function(renpy.pop_call), Hide("banking")

screen crafting(inventory):
    vbox:
        label "Recipes"
        hbox:
            xmaximum 600 xminimum 600 xfill True
            text "Name" xalign 0.5
            text "Ingredients" xalign 0.5
        side "c r":
            area (0,0,600,400)
            viewport id "cookbook":
                draggable True
                mousewheel True
                vbox:
                    for item in cookbook:
                        hbox:
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 250 xminimum 250 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:
                                    text item.name
                            for i in item.recipe:
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])
            vbar value YScrollValue("cookbook")
        textbutton "Hide" action ToggleScreenVariable("crafting_screen") xalign 0.5

screen view_nav(inventory):
    zorder 101
    hbox:
        text "Просмотр: " yalign 0.5
        textbutton "Сетка" action SetField(inventory, "grid_view", True)
        textbutton "Список" action SetField(inventory, "grid_view", False)

screen sort_nav(inventory):
    zorder 101
    hbox:
        text "Сортировка: " yalign 0.5
        textbutton "Имя" action [ToggleField(inventory, "sort_by", inventory.sort_name), inventory.sort_name]
        textbutton "Клич." action [ToggleField(inventory, "sort_by", inventory.sort_qty), inventory.sort_qty]
        textbutton "Ценнос." action [ToggleField(inventory, "sort_by", inventory.sort_value), inventory.sort_value]
        if inventory.sort_order:
            textbutton "инфо." action [ToggleField(inventory, "sort_order"), inventory.sort_by]
        else:
            textbutton "опис." action [ToggleField(inventory, "sort_order"), inventory.sort_by]

screen inventory_popup(message):
    zorder 101
    frame:
        style_group "invstyle"
        hbox:
            text message
    timer 1.5 action Hide("inventory_popup")

init -2:

    ## STYLES ##
    style invstyle_frame:
        xalign 0.5
        yalign 0.5

    style invstyle_label_text:
        size 30

    style invstyle_label:
        xalign 0.5

    style invstyle_button_text:
        idle_color "#900c3f"
        hover_color "#ff5733"
        selected_color "#c70039"
        insensitive_color "#6c567b"
        take pixel_text
