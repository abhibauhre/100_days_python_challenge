import csv

with open("my_weather.csv") as data_files:
    data = csv.reader(data_files)
    for i, row in enumerate(data):
        print(f"Row {i}: {row}")
        if i >= 3:  # Just show first few rows
            break