task = []


while True:
    user_input = int(input("\n Enter \n 1 To Add Task"))
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




    



# task.append("hello")
# task.pop(-1)
# task.pop(1)
# for items in task:
#     print(items)