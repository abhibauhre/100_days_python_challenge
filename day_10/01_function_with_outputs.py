def format_name(f_name ,l_name):
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return f"{formated_f_name} {formated_l_name}"#return function is basically used to return some value from the function


# output = format_name("abhi","BOHRE")#it will store the return value of function in op variable 
# print(output)

print(format_name("abhi","BOHRE"))#it will store the return value of function in op variable 

    
def function1(text):
    return text + text

def function2(text):
    return text.title()

output = function2(function1("abhi"))  
print(output)



     