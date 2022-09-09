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
