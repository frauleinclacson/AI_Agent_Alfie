#imports the os module and checks if the file exists
import os

#imports datetime module to add timestamps
from datetime import datetime

TODO_FILE = "fietodo.txt"

#Load tasks from file (checks if todo.txt exists)
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

#Save tasks to file with timestamp
def save_tasks(tasks):
    with open(TODO_FILE, "a") as file:
        for task in tasks:
            file.write(f"{task}|{datetime.now()}\n")

#Display tasks
def show_tasks(tasks):
    #ANSI Color Codes
    Red = '\033[91m'
    BabyPink = '\033[38;5;218m'
    DarkPink = '\033[38;5;162m'
    Pink = '\033[38;5;213m'
    RESET = '\033[0m'
    
    if not tasks:
        print(Red + "No things to do for now!" + RESET)
        return
    
    #Table header
    print(DarkPink + "\n================")
    print("   To-Do List   ")
    print("================" + RESET)

    #Numbered table rows
    print(Pink + f"{'No.': <5} {'Task' : <50}" + RESET)
    print(BabyPink + "-" * 60 + RESET)

    for i, task in enumerate(tasks, 1):
        print(f"{DarkPink}{str(i)+ '.':<5}{RESET} {task}")
    
    print(Pink + "." * 60 + RESET)

#Adding a new task with category
def add_task(tasks):
    task_name = input("enter task name: ").strip()
    #Default to other if blank
    category = input("enter the task category: ").strip() or "other"
    task = f"{task_name} [{category}]"
    tasks.append(task)
    print(f"task '{task_name}' added under category '{category}'.")
    return tasks

# Main program
if __name__ == "__main__":
    tasks = load_tasks()
    
    while True:
        print("\n1. View tasks\n2. Add task\n3. Save & Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
        elif choice == "3":
            save_tasks(tasks)
            print("Tasks saved. Good job!")
            break
        else:
            print("Invalid choice!")

#Deleting a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

#Main Program Loop
def main():
    tasks = load_tasks()
    while True:
        print("\n TO-DO LIST MAIN MENU:")
        print("1. Display Tasks for the day ahead")
        print("2. Add new Task")
        print("3. Delete Task")
        print("4. Save and Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Your tasks are saved. Goodjob and go rock it!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()