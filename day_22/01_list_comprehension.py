#list comprehension is use to create new list from existing list in single line
# number = [1,3,5,6]
# new_item = [n + 1 for n in number]
# print(new_item)

# name = "abhi bauhre "
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num + num for num in range(1,5)]
# print(new_list)
#list comprehension using list
names = ["abhishek","aryan","arnav","abhi"]
list_comprehension = [name.upper() for name in names if len(name) < 6 ]
print(list_comprehension)