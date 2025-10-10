students ={
    "name":["abhi","shreya","aman","yuvraj"],
    "score":[32,64,79,90]
}

#Looping through dictionaries

# Traditional dictionary iteration
for (key, value) in students.items():  # items function return key and value
    print(f"{key}: {value}")

import pandas

students_score = pandas.DataFrame(students)
print(students_score)

# Loops through rows of a data frame
for (index, row) in students_score.iterrows():
    print(f"Student {index+1}: {row['name']} scored {row.score}") 