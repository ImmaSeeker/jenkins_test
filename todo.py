# todo.py

import os

# Define a function to load tasks from a file
def load_tasks(filename="tasks.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

# Define a function to save tasks to a file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Define a function to display tasks
def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty!")

# Define a function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Define a function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
