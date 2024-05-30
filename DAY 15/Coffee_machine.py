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


# TODO 3. take the input and check if there is enough resources.
# TODO 4. enough resources = continue OR not enough resources = let him know that and ask again for input of coffee type (TODO 1)

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# TODO 5. if enough resource, take input of money.
# TODO 6. money input : "please insert coins." (How many quarters: * 0.25  \n--> How many dimes: * 0.1 \n--> How many nickel: * 0.05 \n--> How many penny: * 0.01 \n)
# TODO 7. sum the coins into and check transaction

def process_coins():
    total = int(input("How many quarters:")) * 0.25
    total += int(input("How many dimes:")) * 0.1
    total += int(input("How many nickel:"))* 0.05
    total += int(input("How many penny: "))* 0.01
    return total

def transaction_check(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink["cost"], 2)
        print(f"here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 8. make coffee -print({coffee choice} and bless him)

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:

        # TODO 9. update coffee machine resources

        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} . Enjoy!")
    print(order_ingredients)



# TODO 1. take an input of coffee type
## coffee type: espresso = 1.5$ , latte = 2.5$ , cappuccino = 3.0$
is_on = True

# TODO 10. repeat the function

while is_on:
    user_choice = (input("what would you like? (espresso/latte/cappuccino):"))
    if user_choice == "off":
        is_on = False

    # TODO 2. if user ask for report, print report.

    elif user_choice == "report":
        report = f"water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}g\nMoney: {profit}$"
        print(report)


    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_check(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])



