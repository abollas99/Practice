MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def make_drink(drink):
    if resource_check(drink):
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if payment(drink):
            print(f"Here is your {choice} enjoy!")
            resources["money"] += MENU[drink]["cost"]


def give_change(change):
    qua = 0
    dim = 0
    nik = 0
    pen = 0
    while True:
        if change >= 0.25:
            qua += 1
            change = round(change - .25, 2)
        elif change >= 0.10:
            dim += 1
            change = round(change - .1, 2)
        elif change >= 0.05:
            nik += 1
            change = round(change - 0.05, 2)
        elif change >= 0.01:
            pen += 1
            change = round(change - 0.01, 2)
        elif change == 0:
            break
    print(f"Change Back\nQuarters: {qua}\nDimes: {dim}\nNickles: {nik}\nPennies: {pen}")


def payment(drink):
    total_owed = MENU[drink]["cost"]
    total_inserted = 0.0
    x = False
    while True:
        if total_inserted >= total_owed:
            give_change(round(total_inserted-total_owed, 2))
            x = True
            break
        inserted_coin = (input("Please enter coins: (q, d, n, p) ")).lower()
        if inserted_coin == "q":
            total_inserted += 0.25
            still_owed = "${:,.2f}".format(total_owed-total_inserted)
            print(f"LEFT TO PAY: {still_owed}")
        elif inserted_coin == "d":
            total_inserted += 0.10
            still_owed = "${:,.2f}".format(total_owed-total_inserted)
            print(f"LEFT TO PAY: {still_owed}")
        elif inserted_coin == "n":
            total_inserted += 0.05
            still_owed = "${:,.2f}".format(total_owed-total_inserted)
            print(f"LEFT TO PAY: {still_owed}")
        elif inserted_coin == "p":
            total_inserted += 0.01
            still_owed = "${:,.2f}".format(total_owed-total_inserted)
            print(f"LEFT TO PAY: {still_owed}")
        elif inserted_coin == "off":
            print("Type off again to turn unit off")
            x = False
            break

        else:
            still_owed = "${:,.2f}".format(total_owed-total_inserted)
            print(f"LEFT: ${still_owed}")
    return x


# main code
choice = ""
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "espresso":
        make_drink(choice)
    elif choice == "latte":
        make_drink(choice)
    elif choice == "cappuccino":
        make_drink(choice)
    elif choice == "report":
        report()
    else:
        break
