from data import MENU, resources

profit = 0

def substract_resources(resources, coffee_type):

    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type == "espresso":
        resources["milk"] -= 0
    else:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    return resources

def calculate_money():

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies? "))
    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(money, 2)

def check_resources_stock(resources):

    if resources["coffee"] <= 0:
        print("Sorry there is not enough coffee")
    if resources["water"] <= 0:
        print("Sorry there is not enough water")
    if resources["milk"] <= 0:
        print("Sorry there is not enough milk")
    if resources["coffee"] <= 0 or resources["water"] <= 0 or resources["milk"] <= 0:
        return False
    else:
        return True

def check_credit(credit, cost, coffee_type):

    if credit > cost:
        print(f"Here is ${round((credit-cost),2)} in change.")
        print(f"Here is your {coffee_type}. Enjoy! ☕ ")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that is not enough money. Money refunded")
        return False

def coffee_machine(resources):

    enough_stock = True
    enough_credit = True

    while enough_stock and enough_credit:

        credit = 0
        coffee_type = input("What coffee would you like? (espresso/latte/cappuccino): ")

        if coffee_type == "off":
            return

        elif coffee_type == "report":
            print(f"These are the resources left: {resources}")
            print(f"This is the profit made so far: {profit}")

        elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":

            resources = substract_resources(resources, coffee_type)
            enough_stock = check_resources_stock(resources)

            if enough_stock == True:

                credit = calculate_money()
                cost = MENU[coffee_type]["cost"]
                enough_credit = check_credit(credit, cost, coffee_type)
        else:
            print("Please make another selection")

coffee_machine(resources)