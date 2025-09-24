print("welcome to treasure hunt")
print("your mission is to find treasure")
choice_1 = input("where want to be go left or right")
if choice_1 == "left":
    choice_2 = input("you pass 1st level you in second level so choose swim or wait")
    if choice_2 == "wait":
        choice_3 = input("you pass the level 2 choose which gate red, blue, orange")
        if choice_3 == "red":
            print("you win")
        elif choice_3 == "blue" or choice_3 == "orange":
            print("you lost")
    else :
        print("lost")      
else:
    print ("you lost")            