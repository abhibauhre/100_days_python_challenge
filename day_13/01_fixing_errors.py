try:
    age = int(input("Enter your age :"))
except ValueError:
    print("type something in maths ")

if age > 18:
    print("you're able to drive")
    