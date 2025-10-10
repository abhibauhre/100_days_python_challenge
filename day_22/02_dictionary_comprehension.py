# Syntax: {key: value for item in iterable}
# Essential for data preprocessing and feature engineering in ML

numbers = [1, 2, 3, 4, 5]

# Traditional way
squared_dict = {}
for num in numbers:
    squared_dict[num] = num ** 2

# Dictionary comprehension (one liner)
squared_comp = {num: num**2 for num in numbers}
print(f"Traditional: {squared_dict}")
print(f"Comprehension: {squared_comp}")


# Raw dataset features
raw_data = {
    "age": [20, 25, 30, 35, 40],
    "income": [30000, 45000, 60000, 75000, 90000],
    "score": [65, 78, 82, 91, 88]
}

# Min-Max scaling: (value - min) / (max - min)
scaled_data = {
    feature: [(val - min(values)) / (max(values) - min(values)) 
              for val in values]
    for feature, values in raw_data.items()
}

print("Original data:")
for feature, values in raw_data.items():
    print(f"  {feature}: {values}")

print("\nScaled data (0-1 range):")
for feature, values in scaled_data.items():
    print(f"  {feature}: {[round(v, 2) for v in values]}")

