from main import MENU, resources


def payment():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total_payment


def is_enough_money(money, cost):
    if money > cost:
        change = round((money - cost), 2)
        print(f"Here is ${change} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def remaining_resources(drink):
    if drink != "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def check_resources(drink):
    enough_resources = True
    if drink != "espresso":
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            enough_resources = False
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            enough_resources = False
        if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            enough_resources = False
    else:
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            enough_resources = False
        if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            enough_resources = False
    return enough_resources

is_on = True
resources["money"] = 0
order = input("What would you like? (espresso/latte/cappuccino): ").lower()
while is_on:
    if order == "report":
        print(resources)
    elif order != "off":
        if order == "latte":
            print("Please insert coins.")
            is_enough_money(payment(), MENU["latte"]["cost"])
            remaining_resources("latte")
        elif order == "cappuccino":
            print("Please insert coins.")
            is_enough_money(payment(), MENU["cappuccino"]["cost"])
            remaining_resources("cappuccino")
        elif order == "espresso":
            print("Please insert coins.")
            is_enough_money(payment(), MENU["espresso"]["cost"])
            remaining_resources("espresso")
    elif order == "off":
        is_on = False
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
