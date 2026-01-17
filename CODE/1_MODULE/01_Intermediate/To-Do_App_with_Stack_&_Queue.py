tasks = []

def add_task(task_name):
    if task_name in tasks:
        print(f"\n'{task_name}' already exists in the task list.")
    else:
        tasks.append(task_name)
        print("\nYour task has been added!")

def undo_task():
    if tasks:
        removed = tasks.pop()
        print(f"\nLast task '{removed}' has been undone.")
    else:
        print("\nNo tasks to undo.")

def complete_first_task():
    if tasks:
        completed = tasks.pop(0)
        print(f"\nFirst task '{completed}' has been completed.")
    else:
        print("\nNo tasks to complete.")

def remove_task(task_name):
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"\nTask '{task_name}' removed.")
    else:
        print("\nTask not found.")

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("""
Choose an option:
1. Add Task
2. Undo Last Task
3. Complete First Task
4. Remove Specific Task
5. Show Tasks
6. Exit
""")

    try:
        user_input = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if user_input == 1:
        task_name = input("Enter task name: ")
        add_task(task_name)

    elif user_input == 2:
        undo_task()

    elif user_input == 3:
        complete_first_task()

    elif user_input == 4:
        task_name = input("Enter task name to remove: ")
        remove_task(task_name)

    elif user_input == 5:
        show_tasks()

    elif user_input == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
