from menu import MENU, resources

resources["money"] = 0.00
MENU["espresso"]["ingredients"]["milk"] = 0
should_continue = True


def resources_check():
    if user_choice == "espresso":
        if resources['water'] < 50:
            return "water"
        elif resources['coffee'] < 18:
            return "coffee"
        elif resources['water'] >= 50 and resources['coffee'] >= 18:
            return "viable"
    elif user_choice == "latte":
        if resources['water'] < 200:
            return "water"
        elif resources['milk'] < 150:
            return "milk"
        elif resources['coffee'] < 24:
            return "coffee"
        elif resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            return "viable"
    else:
        if resources['water'] < 250:
            return "water"
        elif resources['milk'] < 100:
            return "milk"
        elif resources['coffee'] < 24:
            return "coffee"
        elif resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
            return "viable"


def enough_resources():
    if resources_check() == "viable":
        process_coins()
    else:
        print(f"Sorry, there is not enough {resources_check()}")


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total >= MENU[user_choice]["cost"]:
        change = total - MENU[user_choice]["cost"]
        print(f'here is {round(change, 2)} in change')
        make_drink()
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_drink():
    resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    resources["money"] += MENU[user_choice]["cost"]
    print(f"Here is your {user_choice}☕. Enjoy!")


while should_continue:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice.isdigit():
        print("Invalid drink, please type the drink name")
    elif user_choice == "off":
        exit()
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif user_choice == ("espresso" or "latte" or "cappuccino"):
        resources_check()
        enough_resources()
    else:
        print("Unexpected drink, please repeat the process")