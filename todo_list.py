# To-Do List Application
import json

FILE_NAME = "tasks.json"


def load_tasks():
    # Read the tasks from the file. If there is no file yet, start with an empty list.
    try:
        file = open(FILE_NAME, "r")
        tasks = json.load(file)
        file.close()
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    file = open(FILE_NAME, "w")
    json.dump(tasks, file, indent=4)
    file.close()


def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    number = 1
    for task in tasks:
        if task["done"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(number, status, task["title"])
        number = number + 1


def add_task(tasks):
    title = input("Enter the task: ")
    if title == "":
        print("Task can't be empty")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Enter the task number to delete: "))
        tasks.pop(number - 1)
        save_tasks(tasks)
        print("Task deleted")
    except ValueError:
        print("Please enter a number")
    except IndexError:
        print("This task doesn't exist")


def mark_done(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Enter the task number to mark as done: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done")
    except ValueError:
        print("Please enter a number")
    except IndexError:
        print("This task doesn't exist")


tasks = load_tasks()

while True:
    print()
    print("To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
