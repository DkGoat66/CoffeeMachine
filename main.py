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


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """returns the total calculated from coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    """return true for the correct payment"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """minus the ingredient from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕ ")


is_on = True

while True:
    user_input = input("what would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee:{resources['coffee']} g")
        print(f"Money:${profit}")
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
