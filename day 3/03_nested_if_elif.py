print("welcome to the rollercoster")
height = int(input("enter the height"))
bill = 0

if height >= 110 :
    print("you can ride the rollercoster")
    age = int(input("enter your age"))
    if age <= 12:
        bill = 5
        print("you can pay 5$")
    elif age <= 18:
        bill = 7
        print("you can pay 7$")
    else :
        bill = 18 
        print("you pay 18$")   
    wants_photho = input("do you want to have a photho take : type y for yes and type n for no")
    if wants_photho == "y" :
        bill +=3 

    print(f"this is your final bill {bill}")    
else :
    print("you have grow taller than you can ride rollercoster")    