from functions import clear
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def report():
    for item, qty in resources.items():
        print(f"{item}: {qty}".capitalize())

def check_resources(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def get_coins():
    total = 0
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many quarters?"))
    total += (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def make_drink(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    resources["money"] += MENU[drink]["cost"]

clear()
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        report()
    elif choice == "latte" or choice == "espresso" or choice == "cappunccino":
        enough_rescouces = check_resources(choice)
        if not enough_rescouces:
            continue
    else:
        continue

    coins_total = get_coins()
    if coins_total < MENU[choice]["cost"]:
        print("Sorry that's not enough money.  Money refunded.")
        continue

    make_drink(choice)
    print(f"Here is your {choice}. Enjoy!")
    if coins_total > MENU[choice]["cost"]:
        change = coins_total - MENU[choice]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")

