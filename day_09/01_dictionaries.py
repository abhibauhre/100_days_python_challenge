#a dictionaries is a collection of key value pairs and it is use to store data values like map
python_programming = {"bug":"the bug is a error in program that prevents the program from running as expected",
                      "loop":"a loop is a sequence of instruction",
                      "function":"a function is a block of code it only run when it is called"
}

print(python_programming["bug"])#its only print the value of key bug

#it will change the value of key bug
python_programming["bug"] = "the program when its produce error"
print(python_programming)

#wipe out dictionary data
# python_programming = {} #its wipe out all data from dictionary
# print(python_programming)

#add new item in dictionary
python_programming["sets"] ="a set is a collection of data type"
print(python_programming)

#loop through a dictionary
for data in python_programming:
    print(data)#its give only key of dictionary
    print(python_programming[data])