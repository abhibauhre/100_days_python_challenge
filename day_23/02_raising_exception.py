height = float(input("Enter your height"))
weight = int(input("Enter your weight"))

if height > 3:#it will stop the execution of the program and show the error
    raise ValueError("Human height should not be greater than 3 meters")
print(bmi)
