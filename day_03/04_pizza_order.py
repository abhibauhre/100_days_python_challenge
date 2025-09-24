print("welcome to python pizza deliviries")
size = input("what size do you want in pizza ? S ,M OR L")
pepperoni = input("do you want to add pepperoni ? Y OR N")
extra_cheeze = input("do you want to add extra cheeze? Y OR N")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 25
elif size == "L":
    bill = 35
else :
    print("please choose the correct size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if extra_cheeze == "Y":    
    bill += 3
print(f"the total bill is {bill}")




