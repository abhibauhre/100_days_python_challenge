import random

# random_number_between_1_to_10 = random.randint(1 ,10)
# print(random_number_between_1_to_10)

# random_number_between_0_to_1 = random.random()
# print(random_number_between_0_to_1) #it gives float value bw 0 to 1 

# random_number_between_1_to_10 = random.uniform(1,10)#it prints float value bw 1 to 10
# print(random_number_between_1_to_10)
random_number_between_0_to_1 = random.randint(0,1) 
# print(random_number_between_0_to_1)
if random_number_between_0_to_1 == 0 :
    print("heads")
else :
    print("tails")