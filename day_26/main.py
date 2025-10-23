"""
Personal Productivity Tracker
 Log daily tasks
 Fetch motivational quotes from API
 Analyze productivity with pandas
 Save/load data (CSV/JSON)
 Uses: functions, OOP, comprehensions, error handling, API, pandas, file I/O
"""
import os
import json
import csv
import requests
from datetime import datetime
try:
    import pandas as pd
except ImportError:
    pd = None

# --- OOP: Task class ---
class Task:
    def __init__(self, description, completed=False, timestamp=None):
        self.description = description
        self.completed = completed
        self.timestamp = timestamp or datetime.now().isoformat()
    def to_dict(self):
        return {"description": self.description, "completed": self.completed, "timestamp": self.timestamp}
    @staticmethod
    def from_dict(d):
        return Task(d["description"], d["completed"], d["timestamp"])

# --- File I/O: Load/Save tasks ---
TASKS_FILE = "tasks.json"
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as f:
        return [Task.from_dict(d) for d in json.load(f)]

# --- API: Get motivational quote ---
def get_motivational_quote():
    try:
        r = requests.get("https://api.quotable.io/random?tags=motivational|inspirational", timeout=5)
        if r.status_code == 200:
            return r.json()["content"]
    except Exception:
        pass
    return "Keep going! You can do it!"

# --- Pandas: Analyze productivity ---
def analyze_tasks(tasks):
    if not pd:
        print("pandas not installed. Skipping analysis.")
        return
    if not tasks:
        print("No tasks to analyze.")
        return
    df = pd.DataFrame([t.to_dict() for t in tasks])
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date
    summary = df.groupby("date")["completed"].sum()
    print("\nProductivity by day:")
    print(summary)

# --- Main menu ---
def main():
    tasks = load_tasks()
    while True:
        print("\n--- Personal Productivity Tracker ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Save tasks to CSV")
        print("5. Analyze productivity (pandas)")
        print("6. Get motivational quote")
        print("7. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            desc = input("Task description: ").strip()
            if desc:
                tasks.append(Task(desc))
                print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "✓" if t.completed else "✗"
                    print(f"{i}. {t.description} [{status}] ({t.timestamp[:10]})")
        elif choice == "3":
            incompletes = [t for t in tasks if not t.completed]
            if not incompletes:
                print("No incomplete tasks.")
            else:
                for i, t in enumerate(incompletes, 1):
                    print(f"{i}. {t.description}")
                try:
                    idx = int(input("Mark which task as completed? ")) - 1
                    if 0 <= idx < len(incompletes):
                        incompletes[idx].completed = True
                        print("Task marked as completed.")
                except Exception:
                    print("Invalid input.")
        elif choice == "4":
            with open("tasks.csv", "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["description", "completed", "timestamp"])
                writer.writeheader()
                writer.writerows([t.to_dict() for t in tasks])
            print("Tasks saved to tasks.csv.")
        elif choice == "5":
            analyze_tasks(tasks)
        elif choice == "6":
            print("Motivational quote:")
            print(get_motivational_quote())
        elif choice == "7":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

# --- Random User Info Fetcher ---
def fetch_random_user():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        user = data['results'][0]
        name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        email = user['email']
        country = user['location']['country']
        picture = user['picture']['large']
        print("--- Random User Info ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Country: {country}")
        print(f"Profile Picture URL: {picture}")
    except Exception as e:
        print("Failed to fetch user data:", e)

if __name__ == "__main__":
    fetch_random_user()
