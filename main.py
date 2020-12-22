from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
items = MenuItem
while 1:
    order = input(f"What would you like? {menu.get_items()}: ").lower()
    if order == "off":
        break
    elif order == "report":
        coffeemaker.report()
        moneymachine.report()
        break
    else:
        drink = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost) :
                coffeemaker.make_coffee(drink)







