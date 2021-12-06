"""
Coffee Machine: Three drink options, Type report see status of coffee machine
 or type 'off' to quit.
Could be refactored and made more readible with more functions I think
"""
from data import MENU
from data import resources


def resource_valid(drinks, water_check, milk_check, coffee_check):
    """
    Calculate if enough resources
    Return False if not enough resources to make drink
    Return True if there's enough resource to make drink
    """
    water_used = MENU[drinks]['ingredients']['water']
    coffee_used = MENU[drinks]['ingredients']['coffee']
    if drinks != 'espresso':
        milk_used = MENU[drinks]['ingredients']['milk']
        if milk_check < milk_used:
            print("Sorry not enough milk")
            return False
    if water_check < water_used:
        print("Sorry not enough water")
        return False
    if coffee_check < coffee_used:
        print("Sorry not enough coffee")
        return False
    return True


def process_coins(drinks):
    """
    Calculate the cost of the drink in coins
    return True if can cover the cost or False if too little
    """
    cost = MENU[drinks]['cost']
    total_change = 0
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01
    total_change = quarters + dimes + nickles + pennies
    if cost > total_change:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = total_change - cost
    print(f"Here is ${change:.2f} in change.\nEnjoy your {drinks}!")
    return True


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
valid_order = False
money = 0

while True:
    order = input("What would you like to drink?(espresso/latte/cappuccino)\n")
    if order == 'off':
        quit()
    elif order == 'report':
        print(f"Water: {water}, Milk: {milk}, Coffee {coffee}, Money: ${money}")
    elif order == 'cappuccino':
        if resource_valid(order, water, milk, coffee) and process_coins(order):
            valid_order = True
    elif order == 'latte':
        if resource_valid(order, water, milk, coffee) and process_coins(order):
            valid_order = True
    elif order == 'espresso':
        if resource_valid(order, water, milk, coffee) and process_coins(order):
            valid_order = True
    else:
        print("Please enter valid order.")
    if valid_order:
        if order != 'espresso':
            used_milk = MENU[order]['ingredients']['milk']
            milk -= used_milk
        used_water = MENU[order]['ingredients']['water']
        used_coffee = MENU[order]['ingredients']['coffee']
        water -= used_water
        coffee -= used_coffee
        valid_order = False
        cost_of_drink = MENU[order]['cost']
        money += cost_of_drink
