#function is a block of code which only runs when its called it helps to reuse the code

# ============ BASIC FUNCTIONS ============

# Example 1: Simple function without parameters
def greet():
    """This function prints a greeting message"""
    print("Hello! Welcome to Python functions!")
    print("Functions help us organize code better")

# Calling the function
greet()

print("\n" + "="*50 + "\n")

# Example 2: Function with one parameter
def greet_person(name):
    """This function takes a name and greets that person"""
    print(f"Hello {name}!")
    print(f"Nice to meet you, {name}")

# Calling function with different names
greet_person("Abhi")
greet_person("Python Learner")

print("\n" + "="*50 + "\n")

# Example 3: Function with multiple parameters
def introduce_person(name, age, city):
    """Function with multiple parameters"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Hello {name}, you are {age} years old and live in {city}")

# Calling with multiple arguments
introduce_person("Abhi", 20, "Delhi")

print("\n" + "="*50 + "\n")

# Example 4: Function with return value
def add_numbers(num1, num2):
    """This function adds two numbers and returns the result"""
    result = num1 + num2
    return result  # Return statement sends value back to caller

# Using returned value
sum_result = add_numbers(10, 25)
print(f"10 + 25 = {sum_result}")

print("\n" + "="*50 + "\n")

# Example 5: Function with default parameters
def greet_with_title(name, title="Mr."):
    """Function with default parameter value"""
    print(f"Hello {title} {name}!")

# Calling with and without title
greet_with_title("Abhi")  # Uses default title "Mr."
greet_with_title("Priya", "Ms.")  # Uses custom title

print("\n" + "="*50 + "\n")

# Example 6: Calculator functions
def calculator(num1, num2, operation):
    """Calculator function that performs different operations"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"

# Using calculator function
print(f"15 + 5 = {calculator(15, 5, '+')}")
print(f"15 - 5 = {calculator(15, 5, '-')}")
print(f"15 * 5 = {calculator(15, 5, '*')}")
print(f"15 / 5 = {calculator(15, 5, '/')}")

print("\n" + "="*50 + "\n")

# Example 7: Function that calls another function
def format_name(first_name, last_name):
    """Function that formats a full name"""
    return f"{first_name.title()} {last_name.title()}"

def create_email(first_name, last_name, domain="gmail.com"):
    """Function that creates email using another function"""
    full_name = format_name(first_name, last_name)  # Calling another function
    email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
    print(f"Full Name: {full_name}")
    print(f"Email: {email}")
    return email

# Using nested function calls
user_email = create_email("abhi", "bauhre")

print("\n" + "="*50 + "\n")

# Example 8: Function with list parameter
def calculate_average(numbers):
    """Function that calculates average of a list of numbers"""
    if len(numbers) == 0:
        return 0
    
    total = sum(numbers)  # Built-in sum function
    average = total / len(numbers)
    return average

# Using with list
marks = [85, 92, 78, 88, 91]
avg = calculate_average(marks)
print(f"Marks: {marks}")
print(f"Average: {avg:.2f}")

print("\n" + "="*50 + "\n")

# Example 9: Function that modifies global variable
student_count = 0  # Global variable

def add_student(name):
    """Function that adds a student and updates count"""
    global student_count  # Access global variable
    student_count += 1
    print(f"Added student: {name}")
    print(f"Total students: {student_count}")

# Adding students
add_student("Abhi")
add_student("Priya")
add_student("Raj")

print("\n" + "="*50 + "\n")

print("🎉 All function examples completed!")
print("Functions help us:")
print("✅ Organize code better")
print("✅ Reuse code without repetition")
print("✅ Make code more readable")
print("✅ Easier debugging and testing")

