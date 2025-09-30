# def greet():
#     print("hello")
#     print("how do you do abhi ?")
#     print("whats your occupation")

# greet()    

#function with inputs arguments

# def name_of_any_person(name):
#     print(f"hello abhi {name}")
#     print(f"where are you from {name}?")

# name_of_any_person("abhi")

#functions with many inputs and positional arguments
# def greet_with(name , location):
#     print(f"The name is {name} and he is from {location}")

# greet_with("abhi","jhansi")

#function with keyword arguments
#the keyword arguments can be in any order


def greet_with(name , location):
    print(f"The name is {name} and he is from {location}")

greet_with(location = "abhi",name = "jhansi")