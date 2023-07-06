from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_choice = menu.find_drink(choice)

        if drink_choice is None:
            print(f"These are the available options: {menu.get_items()}")

        elif coffee_maker.is_resource_sufficient(drink_choice):
            money_machine = MoneyMachine()
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)