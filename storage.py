import sqlite3
from models import Task

conn = sqlite3.connect("tasks.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS tasks("
    "id INTEGER PRIMARY KEY, title TEXT, due TEXT, done INTEGER DEFAULT 0)"
)

def add_task(title, due=None):
    conn.execute("INSERT INTO tasks (title, due) VALUES (?, ?)", (title, due))
    conn.commit()

def list_tasks():
    rows = conn.execute("SELECT id, title, due, done FROM tasks").fetchall()
    return [
        Task(id=row[0], title=row[1], due=row[2], done=bool(row[3]))
        for row in rows
    ]

def replace_task(task_id, new_title):
    cursor = conn.execute(
        "UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id)
    )
    conn.commit()
    return cursor.rowcount > 0

def delete_task(task_id):
    cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    return cursor.rowcount > 0

def mark_done(task_id):
    cursor = conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    return cursor.rowcount > 0

