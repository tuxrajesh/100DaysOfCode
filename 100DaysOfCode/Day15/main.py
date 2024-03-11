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
EMOJI = "☕"
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def menu():
    """ Prints the cost of each menu item."""
    for item in MENU:
        item_cost = MENU.get(item)["cost"]
        print(f"{item.title()} : ${item_cost}")

def report():
    """ Prints a report of resources available at the vending machine.
    """
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")

def check_resources(ordered_item_ingredients):
    """ Checks if the resources are sufficient for a menu item. Returns a 
    list of resources that are not sufficient.
    """
    not_enough = []
    # print(f"Choice: {choice}, {ordered_item}")
    for ingredient in ordered_item_ingredients:
        if (resources[ingredient] < ordered_item_ingredients[ingredient]):
            not_enough.append(ingredient)
    return not_enough

def calculate_coins(coins):
    """ Returns the value of the coins inserts by the user."""
    total_value = 0
    for coin in coins:
        total_value += coins[coin]["count"] * coins[coin]["value"]
        # print(f"{coin}: {coins[coin]['count']} * {coins[coin]['value']} = {coins[coin]['count'] * coins[coin]['value']}")
    return total_value

def brew(ordered_item):
    """ Make coffed and update resources to deduct the quantity of ingredients used to make the choice"""
    for ingredient in ordered_item["ingredients"]:
        # print(f"Ingredient: {ingredient}. Before Usage: {resources[ingredient]}")
        resources[ingredient] -= ordered_item["ingredients"][ingredient]
        # print(f"Ingredient: {ingredient}. After Usage: {resources[ingredient]}")
    return

machine_on = True
resources["money"] = 0
while machine_on:
    menu()
    # report()
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_on = False
        continue
    elif user_choice == "report":
        report()
    else:    
        selected_item = MENU[user_choice]
        insufficient_resources = check_resources(selected_item["ingredients"])

        if len(insufficient_resources):
            print(f"Sorry there is not enough {insufficient_resources}")
        else:
            print("Please insert coins.")
            user_coins = {
                "quarters" : { "count" : 0, "value" : 0.25 },
                "dimes" : { "count" : 0, "value" : 0.10 },
                "nickles" : { "count" : 0, "value" : 0.05 },
                "pennies" : { "count" : 0, "value" : 0.01 }
            }
            for coin in user_coins:
                user_coins[coin]["count"] = int(input(f"How many {coin}? "))
            
            value_of_coins_inserted = calculate_coins(user_coins)
            item_cost = selected_item["cost"]
            if value_of_coins_inserted < item_cost:
                print(f"Sorry there is not enough money. Money refunded.")
            else:
                if value_of_coins_inserted > item_cost:
                    print(f"Here is ${round(value_of_coins_inserted - item_cost, 2)} in change.")
                resources["money"] += value_of_coins_inserted - item_cost
                brew(selected_item)
                print(f"Here is your {user_choice}{EMOJI}. Enjoy!")