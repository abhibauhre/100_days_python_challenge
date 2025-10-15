# ==================== STUDENT MANAGEMENT SYSTEM ====================
# Mini Project using: Variables, Lists, Tuples, Dictionaries, Functions, Loops, Conditionals

import json
import os
from datetime import datetime

print("🎓 STUDENT MANAGEMENT SYSTEM")
print("="*50)

# ==================== DATA STRUCTURES ====================

# List to store all students (using tuples for immutable student records)
students_database = []

# Dictionary for subject codes
subject_codes = {
    "MATH": "Mathematics",
    "SCI": "Science", 
    "ENG": "English",
    "HIST": "History",
    "CS": "Computer Science"
}

# Tuple for grade boundaries (immutable)
grade_boundaries = (
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F")
)

# ==================== FUNCTIONS ====================

def add_student():
    """Add a new student to the database"""
    print("\n📝 ADD NEW STUDENT")
    print("-" * 20)
    
    # Input validation
    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("❌ Name cannot be empty!")
    
    while True:
        try:
            student_id = int(input("Enter student ID: "))
            # Check if ID already exists
            for student in students_database:
                if student[1] == student_id:  # student[1] is ID
                    print("❌ Student ID already exists!")
                    continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    while True:
        try:
            age = int(input("Enter age: "))
            if 5 <= age <= 100:
                break
            print("❌ Age must be between 5 and 100!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Get grades for subjects
    grades = {}
    print("\nEnter grades for subjects (0-100):")
    
    for code, subject in subject_codes.items():
        while True:
            try:
                grade = float(input(f"{subject} ({code}): "))
                if 0 <= grade <= 100:
                    grades[code] = grade
                    break
                print("❌ Grade must be between 0 and 100!")
            except ValueError:
                print("❌ Please enter a valid number!")
    
    # Create student tuple (immutable record)
    student_record = (name, student_id, age, grades, datetime.now().strftime("%Y-%m-%d"))
    students_database.append(student_record)
    
    print(f"✅ Student {name} added successfully!")

def calculate_grade(average):
    """Calculate letter grade from average using tuple boundaries"""
    for boundary, letter in grade_boundaries:
        if average >= boundary:
            return letter
    return "F"

def display_student(student):
    """Display a single student's information"""
    name, student_id, age, grades, date_added = student
    
    print(f"\n👤 Student Information:")
    print(f"   Name: {name}")
    print(f"   ID: {student_id}")
    print(f"   Age: {age}")
    print(f"   Date Added: {date_added}")
    print(f"   Subjects & Grades:")
    
    total_marks = 0
    subject_count = 0
    
    for code, grade in grades.items():
        subject_name = subject_codes[code]
        letter_grade = calculate_grade(grade)
        print(f"     {subject_name}: {grade}% ({letter_grade})")
        total_marks += grade
        subject_count += 1
    
    if subject_count > 0:
        average = total_marks / subject_count
        overall_grade = calculate_grade(average)
        print(f"   📊 Average: {average:.1f}% ({overall_grade})")
        
        # Performance category
        if average >= 90:
            performance = "🏆 Excellent"
        elif average >= 80:
            performance = "🥇 Very Good"
        elif average >= 70:
            performance = "👍 Good"
        elif average >= 60:
            performance = "📈 Average"
        else:
            performance = "📉 Needs Improvement"
        
        print(f"   Performance: {performance}")

def view_all_students():
    """Display all students in the database"""
    if not students_database:
        print("\n❌ No students in database!")
        return
    
    print(f"\n📚 ALL STUDENTS ({len(students_database)} total)")
    print("="*60)
    
    for i, student in enumerate(students_database, 1):
        print(f"\n{i}. {student[0]} (ID: {student[1]})")
        display_student(student)

def search_student():
    """Search for a student by ID or name"""
    if not students_database:
        print("\n❌ No students in database!")
        return
    
    print("\n🔍 SEARCH STUDENT")
    print("1. Search by ID")
    print("2. Search by Name")
    
    while True:
        choice = input("Choose option (1/2): ")
        if choice in ['1', '2']:
            break
        print("❌ Please enter 1 or 2!")
    
    found = False
    
    if choice == '1':
        try:
            search_id = int(input("Enter Student ID: "))
            for student in students_database:
                if student[1] == search_id:
                    display_student(student)
                    found = True
                    break
        except ValueError:
            print("❌ Please enter a valid number!")
            return
    
    else:  # Search by name
        search_name = input("Enter Student Name: ").strip().lower()
        for student in students_database:
            if search_name in student[0].lower():
                display_student(student)
                found = True
    
    if not found:
        print("❌ Student not found!")

def generate_report():
    """Generate class performance report"""
    if not students_database:
        print("\n❌ No students in database!")
        return
    
    print("\n📊 CLASS PERFORMANCE REPORT")
    print("="*50)
    
    # Calculate statistics for each subject
    subject_stats = {}
    
    for code, subject_name in subject_codes.items():
        grades_list = []
        for student in students_database:
            if code in student[3]:  # student[3] is grades dict
                grades_list.append(student[3][code])
        
        if grades_list:
            avg = sum(grades_list) / len(grades_list)
            highest = max(grades_list)
            lowest = min(grades_list)
            
            subject_stats[subject_name] = {
                'average': avg,
                'highest': highest,
                'lowest': lowest,
                'count': len(grades_list)
            }
    
    # Display subject-wise statistics
    for subject, stats in subject_stats.items():
        print(f"\n📝 {subject}:")
        print(f"   Students: {stats['count']}")
        print(f"   Average: {stats['average']:.1f}%")
        print(f"   Highest: {stats['highest']}%")
        print(f"   Lowest: {stats['lowest']}%")
        print(f"   Class Grade: {calculate_grade(stats['average'])}")
    
    # Overall class statistics
    all_averages = []
    grade_distribution = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for student in students_database:
        grades = list(student[3].values())
        if grades:
            student_avg = sum(grades) / len(grades)
            all_averages.append(student_avg)
            student_grade = calculate_grade(student_avg)
            grade_distribution[student_grade] += 1
    
    if all_averages:
        class_average = sum(all_averages) / len(all_averages)
        print(f"\n🎯 OVERALL CLASS STATISTICS:")
        print(f"   Class Average: {class_average:.1f}%")
        print(f"   Class Grade: {calculate_grade(class_average)}")
        print(f"   Total Students: {len(students_database)}")
        
        print(f"\n📈 GRADE DISTRIBUTION:")
        for grade, count in grade_distribution.items():
            percentage = (count / len(students_database)) * 100
            print(f"   {grade}: {count} students ({percentage:.1f}%)")

def save_data():
    """Save student data to JSON file"""
    try:
        # Convert tuples to lists for JSON serialization
        data_to_save = []
        for student in students_database:
            student_dict = {
                'name': student[0],
                'id': student[1],
                'age': student[2],
                'grades': student[3],
                'date_added': student[4]
            }
            data_to_save.append(student_dict)
        
        with open('students_data.json', 'w') as file:
            json.dump(data_to_save, file, indent=2)
        
        print("✅ Data saved successfully!")
    
    except Exception as e:
        print(f"❌ Error saving data: {e}")

def load_data():
    """Load student data from JSON file"""
    if not os.path.exists('students_data.json'):
        print("📝 No previous data found. Starting fresh!")
        return
    
    try:
        with open('students_data.json', 'r') as file:
            data = json.load(file)
        
        # Convert back to tuples
        students_database.clear()
        for student_dict in data:
            student_tuple = (
                student_dict['name'],
                student_dict['id'],
                student_dict['age'],
                student_dict['grades'],
                student_dict['date_added']
            )
            students_database.append(student_tuple)
        
        print(f"✅ Loaded {len(students_database)} students from file!")
    
    except Exception as e:
        print(f"❌ Error loading data: {e}")

# ==================== MAIN PROGRAM ====================

def main():
    """Main program loop"""
    # Load existing data
    load_data()
    
    while True:
        print("\n" + "="*50)
        print("🎓 STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Save Data")
        print("6. Exit")
        print("-"*50)
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            save_data()
        elif choice == '6':
            save_data()  # Auto-save before exit
            print("\n👋 Thank you for using Student Management System!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# ==================== DEMO DATA ====================

def add_demo_data():
    """Add some demo students for testing"""
    demo_students = [
        ("Alice Johnson", 1001, 16, {"MATH": 92, "SCI": 88, "ENG": 85, "HIST": 90, "CS": 95}, "2024-10-01"),
        ("Bob Smith", 1002, 17, {"MATH": 78, "SCI": 82, "ENG": 75, "HIST": 80, "CS": 88}, "2024-10-02"),
        ("Charlie Brown", 1003, 16, {"MATH": 65, "SCI": 70, "ENG": 68, "HIST": 72, "CS": 75}, "2024-10-03"),
        ("Diana Prince", 1004, 17, {"MATH": 95, "SCI": 92, "ENG": 89, "HIST": 94, "CS": 97}, "2024-10-04")
    ]
    
    students_database.extend(demo_students)
    print("✅ Demo data added!")

# ==================== PROGRAM START ====================

if __name__ == "__main__":
    print("🚀 Welcome to Student Management System!")
    print("="*50)
    
    # Ask if user wants demo data
    if not students_database:
        demo = input("Would you like to add demo data for testing? (y/n): ").lower()
        if demo == 'y':
            add_demo_data()
    
    main()

print("\n🎉 Program completed successfully!")
print("📚 Concepts used:")
print("  ✅ Variables & Data Types")
print("  ✅ Lists & Tuples") 
print("  ✅ Dictionaries")
print("  ✅ Functions")
print("  ✅ Loops & Conditionals")
print("  ✅ File Handling (JSON)")
print("  ✅ Error Handling")
print("  ✅ String Operations")
print("  ✅ Mathematical Operations")