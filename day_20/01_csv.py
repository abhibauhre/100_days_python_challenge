# with open("my_weather.csv") as data_files :
#     data = data_files.readlines()
#     print(data)
# import csv

# with open("my_weather.csv") as data_files :
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data:
#         if row[1] != "temperature":  
#             temperature.append(float(row[1]))  # Use float for decimal numbers
#     print(temperature)        
import pandas

data = pandas.read_csv("my_weather.csv")
print(data)