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
# # print(data)

# # data_temp = data.to_dict()
# # print(data_temp)

# temp_list = data["temperature"].to_list()
# print((temp_list))

# # average = sum(temp_list) / len(temp_list)
# # print(average)

# print(data["temperature"].mean())#it gives the average of the temperature column
# print(data["temperature"].min())#it gives the minimum value of the temperature column

# #get data in columns 
# print(data["temperature"])
# print(data.temperature)

# print(data[data.temperature == 22.5 ])
# print(data[data.temperature == data.temperature.max()])
# humidity = data[data.humidity ==  "Sunny" ]
# print(humidity.humidity)

data_dict = {
    "name":["abhi","aryan","arnav"],
    "score":["33","53","97"]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")