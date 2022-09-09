import transaction
import resources

choice = ""
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "espresso":
        paid = transaction.payment(choice)
        resources.make_drink(choice, paid)
    elif choice == "latte":
        paid = transaction.payment(choice)
        resources.make_drink(choice, paid)
    elif choice == "cappuccino":
        paid = transaction.payment(choice)
        resources.make_drink(choice, paid)
    elif choice == "report":
        resources.report()
    else:
        break
