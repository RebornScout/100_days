from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

switched_on = True

while switched_on:
    choice = input("What would you like? " + menu.get_items() + ": ")
    if choice == "off":
        switched_on = False
        continue
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappunccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        continue
