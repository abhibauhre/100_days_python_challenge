from art import simple_calc

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(simple_calc)
    print("Welcome to Python Calculator")
    print("=" * 50)
    num1 = float(input("Enter the first number: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        continue_choice = continue_choice.lower()
        
        if continue_choice == 'y':
            num1 = answer  # Use the answer as the first number for next calculation
        else:
            should_continue = False
            calculator()  # Start fresh calculation

# Start the calculator
calculator()
