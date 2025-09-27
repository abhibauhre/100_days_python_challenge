import random
friends = ["abhi" , "arnav" , " aryan" ,"harsh" , "manish"]
#method 1
random_number_between_0_to_1 = random.randint(0, 4)
print(friends[random_number_between_0_to_1])
#method 2
randomm = random.choice(friends)
print(randomm)





