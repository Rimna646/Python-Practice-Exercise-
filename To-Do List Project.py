# To-Do List Application

tasks = [] 


def display_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task():
    display_tasks()
    if len(tasks) > 0:
        number = int(input("Enter task number to remove: "))
        if number > 0 and number <= len(tasks):
            tasks.pop(number - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

def edit_task():
    display_tasks()
    if len(tasks) > 0:
        number = int(input("Enter task number to edit: "))
        if number > 0 and number <= len(tasks):
            new_task = input("Enter new task name: ")
            tasks[number - 1] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")

def mark_completed():
    display_tasks()
    if len(tasks) > 0:
        number = int(input("Enter task number to mark as completed: "))
        if number > 0 and number <= len(tasks):
            tasks[number - 1] = tasks[number - 1] + " (Completed)"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

def main_menu():
    print("\nMenu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Edit Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

while True:
    display_tasks()
    main_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
