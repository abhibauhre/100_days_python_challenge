# JSON = JavaScript Object Notation (but used everywhere, not just JavaScript)
# Purpose: Store and exchange data between systems in a readable format

import json
import pandas as pd
from datetime import datetime

#BASIC JSON CONCEPTS 
# Python data structures that can be converted to JSON
python_data = {
    "name": "Alice",           # string
    "age": 25,                 # number
    "is_student": True,        # boolean
    "grades": [85, 92, 78],    # array (list)
    "address": {               # nested object (dict)
        "city": "Mumbai",
        "pincode": 400001
    },
    "phone": None              # null value
}

print("🐍 Python Dictionary:")
print(python_data)
print(f"Type: {type(python_data)}")

#PYTHON TO JSON (SERIALIZATION)
print("\n🔄 STEP 2: Converting Python to JSON String")
print("-" * 50)

# Convert Python dict to JSON string
json_string = json.dumps(python_data, indent=2)  # indent=2 makes it readable#json.dumps converts python data to json data
print("📄 JSON String:")
print(json_string)
print(f"Type: {type(json_string)}")

# JSON TO PYTHON (DESERIALIZATION)
print("\n🔄 STEP 3: Converting JSON back to Python")
print("-" * 50)

# Convert JSON string back to Python
back_to_python = json.loads(json_string)#json.loads() it is use to convert json data to python data
print("🐍 Back to Python:")
print(back_to_python)
print(f"Type: {type(back_to_python)}")
print(f"Same as original? {python_data == back_to_python}")

# # ==================== STEP 4: SAVING JSON TO FILE ====================
# print("\n💾 STEP 4: Saving JSON to File")
# print("-" * 50)

# # Create sample student data for ML
# student_data = {
#     "dataset": "student_performance",
#     "created_date": "2025-10-12",
#     "students": [
#         {"id": 1, "name": "Raj", "math": 85, "science": 90, "passed": True},
#         {"id": 2, "name": "Priya", "math": 78, "science": 82, "passed": True},
#         {"id": 3, "name": "Amit", "math": 45, "science": 55, "passed": False},
#         {"id": 4, "name": "Sneha", "math": 92, "science": 88, "passed": True}
#     ],
#     "statistics": {
#         "total_students": 4,
#         "pass_rate": 0.75,
#         "avg_math": 75.0,
#         "avg_science": 78.75
#     }
# }

# # Save to file
# with open("student_data.json", "w", encoding="utf-8") as file:
#     json.dump(student_data, file, indent=2, ensure_ascii=False)

# print("✅ Data saved to 'student_data.json'")
# print("📊 Sample of saved data:")
# print(f"  Total students: {student_data['statistics']['total_students']}")
# print(f"  Pass rate: {student_data['statistics']['pass_rate'] * 100}%")

# # ==================== STEP 5: READING JSON FROM FILE ====================
# print("\n📖 STEP 5: Reading JSON from File")
# print("-" * 50)

# # Read the file we just created
# try:
#     with open("student_data.json", "r", encoding="utf-8") as file:
#         loaded_data = json.load(file)
    
#     print("✅ Data loaded successfully!")
#     print("📋 Dataset info:")
#     print(f"  Dataset name: {loaded_data['dataset']}")
#     print(f"  Created: {loaded_data['created_date']}")
#     print(f"  Number of students: {len(loaded_data['students'])}")
    
# except FileNotFoundError:
#     print("❌ File not found!")

