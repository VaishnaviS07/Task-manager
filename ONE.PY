import tkinter as tk
import sqlite3
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task TEXT
    )
''')
conn.commit()

def add_task():
    task = task_entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        task_entry.delete(0, tk.END)
        update_task_list()

def update_task_list():
    task_list.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        task_list.insert(tk.END, task[1])

root = tk.Tk()
root.title("Task Manager")

task_entry = tk.Entry(root, width=30)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, width=50)
task_list.pack()

update_task_list()

root.mainloop()

conn.close()
