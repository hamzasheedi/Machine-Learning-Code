task = []


while True:
    # user_input

    user_input = int(input("\n Enter \n 1 To Add Task"))
    
    # if user input is 1 (For Adding Task)
    
    if user_input == 1:
        def add_task(task_name):
            if task_name not in task:
                task.append(task_name)
                print("\n Your Task Has Been Added..!")
                return
            elif task_name in task:
                print(f"\n {task_name} already exist in Task List.")
                return
        task_name = input("\n Enter Your Task Name: \n")
        add_task(task_name)

    # if user input is 2 (For Undo Task)

    elif user_input == 2:
        def undo_task():
            task.pop(-1)
            print("\n Your Last Added Task Have Been Removed")
        undo_task()
    
    # if user input is 3 (For Complete First Added Task)

    elif user_input == 3:
        def complete_first_task():
            task.pop(0)
            print("\n Your First Added Task Have Been Completed and Removed From Task List")
        complete_first_task()
    




    



# task.append("hello")
# task.pop(-1)
# task.pop(1)
# for items in task:
#     print(items)