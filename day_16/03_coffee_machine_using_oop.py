from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from the imported classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Main program loop
is_on = True

while is_on:
    # Get available menu options
    options = menu.get_items()
    
    # Ask user what they want
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == "off":
        is_on = False
        print("Machine shutting down. Goodbye!")
        
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        
    else:
        # Find the drink in the menu
        drink = menu.find_drink(choice)
        
        # Check if drink exists and process order
        if drink:
            # Check if enough resources
            if coffee_maker.is_resource_sufficient(drink):
                # Process payment
                if money_machine.make_payment(drink.cost):
                    # Make the coffee
                    coffee_maker.make_coffee(drink)
        else:
            print("Sorry, that item is not available.") 
