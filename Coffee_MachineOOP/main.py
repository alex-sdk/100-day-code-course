from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"Wha would you like? ({options})")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            can_pay = money_machine.make_payment(drink.cost)
            if can_pay:
                    coffee_maker.make_coffee(drink)



