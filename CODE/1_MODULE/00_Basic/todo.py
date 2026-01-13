task = {}

while True:
    user_input = int(input("\nWrite 1 For Add Or Update Task\n 2 For Delete Task \n 3 For View Task \n 4 For Exiting\n"))
    if user_input == 1:
        def add_update_task(task_name, task_description):
            try:
                print("\nTask Name Should Be Unique For Adding New Task \n For Updating Task Name Must Need To Be Same.")
                task[task_name] = task_description
                print("\nTask Added")
                print(task)
                return
            except Exception:
                print("\nERROR OCCUR: ",Exception)
            return 
        task_name = input("\nEnter Your Task Name: ")
        task_description = input("\nEnter Your Task Description: ")
        add_update_task(task_name,task_description)
                

    elif user_input == 2:
        def delete_task(task_name):
            print("\nFor Deleting Task, Task Needed To Be Exist")
            try:
                task.pop(task_name)
                print(f"\nTask List Updated Succesfully")
                return
            except Exception:
                print("\nTask Name is not Correct Or Task Is Not Availble")
            
        task_name = input("Enter Your Task Name: ")
        delete_task(task_name)
                
    elif user_input == 3:
        def view_task():
            for task_name , task_description in task.items():
                print(f"\nTask Name: {task_name} ({task_description})")
                return
            if task == {}:
                print("\nThere is No Task To Show")
        view_task()
    
    elif user_input == 4:
        print("\nTHANK YOU FOR USING")
        break
    
    else:
        print("\nAccept Only 1,2,3,4")
