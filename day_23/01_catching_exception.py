#File not found
try:

    file = open("abhi_txt.txt")
    dict ={"key":"value"}
    print(dict["keyasd"])

except FileNotFoundError:
    file = open("abhi_txt.txt","w")#w is used to create a file if it is not 
    file.write("something")

except KeyError as error_message:
    print(f"right key is {error_message}on dictinary")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file was close")
    
