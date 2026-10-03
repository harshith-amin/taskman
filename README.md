# Taskman

A simple to-do list that runs in the terminal. Tasks are saved in a SQLite database, so they are still there after you close the program.

## Features

- Add a task with an optional due date
- Replace (rename) a task
- Mark a task as done
- Delete a task
- Tasks show `[OVERDUE]` when the due date has passed
- Menu and task list shown side by side in a box
- Wrong input (letters, bad dates, wrong numbers) does not crash the program

## How to run

You need Python 3.10 or newer. No extra packages are needed.

```
python3 main.py
```

## How to use

Type the number of an option and press Enter:

| Option | What it does |
|---|---|
| 1. Add | Add a new task. Enter the due date as `DD-MM-YYYY`, or press Enter to skip. |
| 2. Replace | Choose a task number and type a new title. |
| 3. Done | Choose a task number to mark it as done. |
| 4. Delete | Choose a task number to remove it. |
| 5. Exit | Close the program. |

## Project files

| File | Purpose |
|---|---|
| `main.py` | The screen and menu (what the user sees) |
| `models.py` | The `Task` class |
| `storage.py` | All database work (add, list, replace, delete, done) |
| `tasks.db` | The database, created automatically on first run |

## What I learned

- Using SQLite from Python (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Splitting code into files: screen in one, database in another
- Using a `dataclass` instead of plain tuples
- Handling errors with `try/except`
- Working with dates (`strptime`, `strftime`)