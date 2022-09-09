from transaction import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


def report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\n'
          f'Money: ${resources["money"]}')


def resource_check(drink):
    unavailable_resources = []
    req_water = MENU[drink]["ingredients"]["water"]
    req_milk = MENU[drink]["ingredients"]["milk"]
    req_coffee = MENU[drink]["ingredients"]["coffee"]
    if req_milk > resources["milk"]:
        unavailable_resources.append("milk")
    if req_coffee > resources["coffee"]:
        unavailable_resources.append("coffee")
    if req_water > resources["water"]:
        unavailable_resources.append("water")
    if req_coffee < resources["coffee"] and req_milk < resources["milk"] and req_water < resources["water"]:
        x = True
    else:
        x = False
        print("Unfortunately that drink cannot be made due to a lack of the following resources: ")
        for n in unavailable_resources:
            print(n.title())
    return x


def make_drink(drink, paid):
    if resource_check(drink):
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if paid:
            print(f"Here is your {drink} enjoy!")
            resources["money"] += MENU[drink]["cost"]
