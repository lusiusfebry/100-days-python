from data_menu import MENU, resources,profit

def is_resources_sufficient (drink):
    for item in drink:
        if drink[item] >= resources[item] :
            print (f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print ("Please insert coind")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many penies: ")) * 0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def main():
    is_on = True
    # profit = 0

    while is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            is_on = False
        elif user_input == "report":
            print(f"Water = {resources['water']}ml")
            print(f"Milk = {resources['milk']}ml")
            print(f"Coffee = {resources['coffee']}ml")
            print (f"Money = ${profit}")
        else:
            drink = MENU[user_input]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coin()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_input, drink["ingredients"])




main()