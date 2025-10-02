#LOCAL vs GLOBAL VARIABLLE

def my_function_local():
    x = 10  # Local variable - only exists inside this function
    print(f"Value of x inside the function: {x}")

my_function_local()
# print(x)  # This would cause an ERROR because x doesn't exist outside the function


x = 10  # Global variable - defined outside any function
def my_function_global():
    print(f"Value of global x inside the function: {x}")  # Can read global x

my_function_global()
print(f"Value of global x outside the function: {x}")

y = 100  # Global variable
def my_function_shadow():
    y = 13  # Local variable - shadows the global y
    print(f"Value of local y inside the function: {y}")

my_function_shadow()
print(f"Value of global y outside the function: {y}")  # Global y unchanged

z = 500  # Global variable
def my_function_modify_global():
    global z  # Tell Python: "I want to use the global z, not create a local one"
    z = 999   # Now this modifies the global z
    print(f"Modified global z inside function: {z}")

print(f"Global z before function call: {z}")
my_function_modify_global()
print(f"Global z after function call: {z}")  # Global z is now changed!


def create_global_variable():
    global new_var  # Declare that new_var should be global
    new_var = "I'm created inside a function but I'm global!"
    print(f"Created global variable: {new_var}")

# new_var doesn't exist yet
create_global_variable()  # Now new_var is created as global
print(f"Accessing new_var outside function: {new_var}")  # Works!


def modify_multiple_globals():
    global a, b, c  # Declare multiple global variables
    a = 1
    b = 2
    c = 3
    print(f"Inside function - a: {a}, b: {b}, c: {c}")

modify_multiple_globals()
print(f"Outside function - a: {a}, b: {b}, c: {c}")
