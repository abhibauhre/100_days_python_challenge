
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


resources = {
    "water": 300, 
    "milk": 200,   
    "coffee": 100,}


profit = 0


MONEY = {
    "quarters": 0.25,  # 25 cents
    "dimes": 0.10,     # 10 cents
    "nickles": 0.05,   # 5 cents
    "pennies": 0.01    # 1 cent
}

def is_resources_sufficient(order_ingredients):
    """
    This function checks if we have enough ingredients to make the requested drink.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """this function processes the coins inserted by the customer and calculates the total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * MONEY["quarters"]
    total += int(input("How many dimes?: ")) * MONEY["dimes"]
    total += int(input("How many nickles?: ")) * MONEY["nickles"]
    total += int(input("How many pennies?: ")) * MONEY["pennies"]
    return total

def is_payment_successful(money_received, drink_cost):
    """
    This function checks if the customer paid enough money
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)  # Round to 2 decimal places for money
        print(f"Here is ${change} in change.")
        global profit  # Access the global profit variable
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    This function actually makes the coffee by using up the ingredients.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def print_report():
    """
    This function shows the current status of the machine.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


is_on = True  

print("☕ Welcome to the Coffee Machine! ☕")
print("Available drinks: espresso, latte, cappuccino")
print("Special commands: 'report' (check resources), 'off' (turn off machine)")

while is_on:
   
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        
        print("Machine is shutting down. Goodbye!")
        is_on = False
        
    elif choice == "report":
       
        print("\n--- MACHINE REPORT ---")
        print_report()
        
    elif choice in MENU:
       
        print(f"\nYou selected: {choice.title()}")
        
        drink = MENU[choice]  
        
        if is_resources_sufficient(drink["ingredients"]):
            print(f"Cost: ${drink['cost']}")
            
            payment = process_coins()

            if is_payment_successful(payment, drink["cost"]):
               
                make_coffee(choice, drink["ingredients"])
          
            
        
        
    else:
        # Customer typed something invalid
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
        print("Or type 'report' to check machine status, or 'off' to shut down.")


