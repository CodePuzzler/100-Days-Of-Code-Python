# Day15 of my 100DaysOfCode Challenge
# Coffee Machine program

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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: Check resources sufficient?


def is_resources_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO: Process coins.


def process_coins():
    """Returns total sum of coins inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

# TODO: Check transaction successful?


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO: Make Coffee


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


machine_running = True

while machine_running:

    # TODO: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    item_ordered = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: Turn off the Coffee Machine by entering "off" to the prompt
    if item_ordered == "off":
        machine_running = False

    # TODO: Print report
    elif item_ordered == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[item_ordered]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(item_ordered, drink["ingredients"])






