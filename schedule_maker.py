import json
import datetime

SCHEDULE_FILE = 'schedule.json'

def load_schedule():
    try:
        with open(SCHEDULE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

def save_schedule(schedule):
    with open(SCHEDULE_FILE, 'w') as f:
        json.dump(schedule, f, indent=4)

def add_task(schedule):
    day = input("Enter day (e.g., Monday): ").capitalize()
    if day not in schedule:
        print("Invalid day.")
        return
    task = input("Enter task title: ")
    time = input("Enter time (optional): ")
    schedule[day].append({'task': task, 'time': time})
    print("Task added.")

def view_day(schedule):
    day = input("Enter day (e.g., Monday): ").capitalize()
    if day not in schedule:
        print("Invalid day.")
        return
    print(f"\n--- {day} ---")
    if not schedule[day]:
        print("No tasks.")
    else:
        for i, task in enumerate(schedule[day], start=1):
            time_display = f" at {task['time']}" if task['time'] else ''
            print(f"{i}. {task['task']}{time_display}")

def view_today(schedule):
    today = datetime.datetime.now().strftime("%A")
    print(f"\n--- Today ({today}) ---")
    if not schedule[today]:
        print("No tasks.")
    else:
        for i, task in enumerate(schedule[today], start=1):
            time_display = f" at {task['time']}" if task['time'] else ''
            print(f"{i}. {task['task']}{time_display}")

def remove_task(schedule):
    day = input("Enter day: ").capitalize()
    if day not in schedule or not schedule[day]:
        print("No tasks for this day.")
        return
    view_day(schedule)
    try:
        task_no = int(input("Enter task number to remove: "))
        removed = schedule[day].pop(task_no - 1)
        print(f"Removed: {removed['task']}")
    except (ValueError, IndexError):
        print("Invalid input.")

def menu():
    schedule = load_schedule()

    while True:
        print("\n=== Daily Schedule Maker ===")
        print("1. Add Task")
        print("2. View Today's Tasks")
        print("3. View Tasks by Day")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            add_task(schedule)
        elif choice == '2':
            view_today(schedule)
        elif choice == '3':
            view_day(schedule)
        elif choice == '4':
            remove_task(schedule)
        elif choice == '5':
            save_schedule(schedule)
            print("Schedule saved. Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
