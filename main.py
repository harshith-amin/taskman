from storage import add_task, list_tasks, replace_task, delete_task, mark_done
from datetime import datetime,date
from itertools import zip_longest
import unicodedata

MENU = ["1. Add", "2. Replace", "3. Done", "4. Delete", "5. Exit"]

def display_width(text):
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in text)

def pad(text, width):
    return text+ " " * (width - display_width(text))

def show_screen(tasks):
    left = ["--- Menu ---"] + MENU
    right = ["--- Your tasks ---"] + show_tasks(tasks)
    left_width = 16
    right_width = max(display_width(text) for text in right)
    line = "─" * (left_width + right_width + 6)
    print()
    print(line)
    for left_txt, right_txt in zip_longest(left, right, fillvalue=""):
        print(f"│ {pad(left_txt, left_width)}│  {pad(right_txt, right_width)}│")
    print(line)

def get_due_date():
    while True:
        text = input("Due date (DD-MM-YYYY, or Enter to skip): ")
        if not text:
            return None
        try:
            parsed = datetime.strptime(text, "%d-%m-%Y")
        except ValueError:
            print("Invalid date, use DD-MM-YYYY")
            continue
        return parsed.strftime("%Y-%m-%d")

def format_due(due):
    return datetime.strptime(due, "%Y-%m-%d").strftime("%d-%m-%Y")

def is_overdue(due):
    return datetime.strptime(due, "%Y-%m-%d").date() < date.today()

def show_tasks(tasks):
    if not tasks:
        return ["No tasks yet", "Choose 1 to add a task"]
    lines = []
    for number, task in enumerate(tasks, start=1):
        mark = "🗹" if task.done else "□"
        due_text = ""
        if task.due:
            due_text = f" (due {format_due(task.due)})"
            if not task.done and is_overdue(task.due):
                due_text += "[OVERDUE]"
        lines.append(f"{number}.  {mark} {task.title}{due_text}")
    return lines

def get_task_number(total):
    while True:
        try:
            number = int(input("Task number: "))
        except ValueError:
            print("please enter a valid number")
            continue
        if 1 <= number <= total:
            return number
        print(f"Enter a number between 1 and {total}")

message = ""
while True:
    tasks = list_tasks()
    show_screen(tasks)
    if message:
        print(message)
        message = ""
    choice = input("Choose: ").strip()

    if choice == "1":
        title = (input("Task: "))
        add_task(title, get_due_date())
    elif choice in ("2", "3", "4"):
        if not tasks:
            message = "No tasks available. Choose 1 to add a task"
            continue
        number = get_task_number(len(tasks))
        task = tasks[number - 1]
        if choice == "2":
            replace_task(task.id, input("New title: "))
        elif choice == "3":
            mark_done(task.id)
        else:
            delete_task(task.id)
    elif choice == "5":
        break
    else:
        message = "Invalid choice"