# Definition: Tuple is an ordered collection of items that cannot be changed (immutable)

# Creating tuples
empty_tuple = ()
single_item_tuple = (42,)  # Comma is important for single item
coordinates = (10, 20)
rgb_colors = (255, 128, 0)
mixed_tuple = ("Python", 3.9, True, 100)

print(f"Empty tuple: {empty_tuple}")
print(f"Single item: {single_item_tuple}")
print(f"Coordinates: {coordinates}")
print(f"RGB Colors: {rgb_colors}")
print(f"Mixed data: {mixed_tuple}")

# 2. TUPLE vs LIST COMPARISON
# List (mutable - can be changed)
my_list = [1, 2, 3]
print(f"Original list: {my_list}")
my_list[0] = 100  # This works
print(f"Modified list: {my_list}")

# Tuple (immutable - cannot be changed)
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")
# my_tuple[0] = 100  # This would cause an error!


# 3. ACCESSING TUPLE ELEMENTS
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"Fruits tuple: {fruits}")

# Positive indexing
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")

# Negative indexing
print(f"Last fruit: {fruits[-1]}")
print(f"Second last: {fruits[-2]}")

# Slicing
print(f"First 3 fruits: {fruits[0:3]}")
print(f"Last 2 fruits: {fruits[-2:]}")
print(f"Every second fruit: {fruits[::2]}")

# 4. TUPLE UNPACKING
# Basic unpacking
point = (100, 200)
x, y = point
print(f"Point: {point}")
print(f"X coordinate: {x}")
print(f"Y coordinate: {y}")

# Multiple assignment
person_info = ("Alice", 25, "Engineer")
name, age, profession = person_info
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Swapping variables using tuples
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")


# 5. TUPLE METHODS

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Numbers tuple: {numbers}")

# count() - counts occurrences of an element
count_of_2 = numbers.count(2)
print(f"Number of 2's: {count_of_2}")

# index() - finds first occurrence of an element
index_of_4 = numbers.index(4)
print(f"Index of 4: {index_of_4}")

# Length of tuple
print(f"Length of tuple: {len(numbers)}")

# 6. TUPLE OPERATIONS

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Tuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print(f"Combined: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repeated 3 times: {repeated}")

# Membership testing
print(f"Is 2 in tuple1? {2 in tuple1}")
print(f"Is 7 in tuple1? {7 in tuple1}")


# Example 1: Storing coordinates
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

point_a = (0, 0)
point_b = (3, 4)
dist = calculate_distance(point_a, point_b)
print(f"Distance between {point_a} and {point_b}: {dist}")

# ==================== BASIC PROGRAMS ====================

# Program 1: Student Grade System
print("\n" + "="*50)
print("📚 PROGRAM 1: STUDENT GRADE SYSTEM")
print("="*50)

# Store student information as tuples
students = [
    ("Alice", 85, 92, 78),
    ("Bob", 76, 88, 82),
    ("Charlie", 95, 87, 91),
    ("Diana", 82, 90, 88)
]

print("Student Grade Report:")
print("-" * 40)

for student in students:
    name, math, science, english = student  # Tuple unpacking
    
    # Calculate average
    total = math + science + english
    average = total / 3
    
    # Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Student: {name}")
    print(f"  Math: {math}, Science: {science}, English: {english}")
    print(f"  Average: {average:.1f}, Grade: {grade}")
    print()

# Find top student
best_student = None
highest_avg = 0

for student in students:
    name, math, science, english = student
    avg = (math + science + english) / 3
    if avg > highest_avg:
        highest_avg = avg
        best_student = name

print(f"🏆 Top Student: {best_student} with {highest_avg:.1f} average")

# Program 2: Restaurant Menu System
print("\n" + "="*50)
print("🍕 PROGRAM 2: RESTAURANT MENU SYSTEM")
print("="*50)

# Menu items as tuples (item_name, price, category)
menu = [
    ("Pizza Margherita", 250, "Main"),
    ("Burger Deluxe", 180, "Main"),
    ("Caesar Salad", 120, "Starter"),
    ("Garlic Bread", 80, "Starter"),
    ("Chocolate Cake", 150, "Dessert"),
    ("Ice Cream", 90, "Dessert"),
    ("Coke", 50, "Beverage"),
    ("Fresh Juice", 70, "Beverage")
]

# Customer order (item_name, quantity)
customer_order = [
    ("Pizza Margherita", 2),
    ("Caesar Salad", 1),
    ("Coke", 3),
    ("Chocolate Cake", 1)
]

print("🍽️ RESTAURANT MENU:")
print("-" * 30)

# Display menu by category
categories = ["Starter", "Main", "Dessert", "Beverage"]

for category in categories:
    print(f"\n{category.upper()}:")
    for item_name, price, item_category in menu:
        if item_category == category:
            print(f"  {item_name}: ₹{price}")

print("\n" + "="*30)
print("📝 CUSTOMER ORDER:")
print("="*30)

total_bill = 0
print("Order Details:")

for order_item, quantity in customer_order:
    # Find price from menu
    for menu_item, price, category in menu:
        if menu_item == order_item:
            item_total = price * quantity
            total_bill += item_total
            print(f"  {order_item} x {quantity} = ₹{item_total}")
            break

print("-" * 30)
print(f"💰 TOTAL BILL: ₹{total_bill}")

# Add service charges and tax
service_charge = total_bill * 0.10  # 10%
tax = total_bill * 0.05  # 5%
final_amount = total_bill + service_charge + tax

print(f"Service Charge (10%): ₹{service_charge:.2f}")
print(f"Tax (5%): ₹{tax:.2f}")
print("-" * 30)
print(f"🧾 FINAL AMOUNT: ₹{final_amount:.2f}")

# Program bonus: Most expensive and cheapest items
print("\n📊 MENU ANALYSIS:")
print("-" * 20)

# Find most expensive item
most_expensive = max(menu, key=lambda x: x[1])  # x[1] is price
cheapest = min(menu, key=lambda x: x[1])

print(f"Most Expensive: {most_expensive[0]} - ₹{most_expensive[1]}")
print(f"Cheapest: {cheapest[0]} - ₹{cheapest[1]}")

print("\n✅ Tuple Programs Complete!")
