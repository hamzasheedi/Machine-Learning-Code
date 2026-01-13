task = []


while True:
    user_input = int(input("\nEnter \n 1 To Add \n 2 To Display Task \n 3 To Delete Task \n 4 To Update Task \n 5 To Exit\n Your Input:"))
    
    if user_input == 1:
        print("\n Add A New Task")
    
        def add_task(name, priority, status):
            try:
                new_task = {"name":name , "priority": priority , "status":status}
                task.append(new_task)
                return

            except Exception:
                print(f"Error Occured {Exception}, Please Try Again..!")
                return
    
        name = input("Enter a Task Name: \n")
        priority = input("Enter Task Prioirity: \n")
        status = input("Enter Task Status: \n")
    
        add_task(name, priority, status)

    elif user_input == 2:      
    
        def display_task(task):
            try:
                if task == []:
                    print("\n No Task To Display \n")
                    return
                
                for index , task in enumerate(task):
                    print(f"\n {index}. Task Name: {task["name"]}, Priority {task["priority"]}, status: {task["status"]} \n")
            
            except ValueError and IndexError:
                print(f"\n There is Error as {IndexError or ValueError} while displaying task\n ")
    
        display_task(task)

    elif user_input == 3:
        print("\n Delete Task \n ")
    
        def delete_task(index):
            try:
                task.pop(index)
            except IndexError:
                print(f"\nThere is Error as {IndexError} while Deleting task, Make sure to recheck Task Number\n")

        index =  int(input("\n Enter Your Task Number:"))
        
        delete_task(index)

    elif user_input == 4 :
        def update_task(index , update_key , updated_value):
            try:
                task[index][update_key] = updated_value
            except ValueError or IndexError:
                print(f"\nThere is Error as {ValueError or IndexError} while updating task, make sure to recheck Task Number and Value\n")
        
        index =  int(input("\n Enter Your Task Number: "))
        update_key = str(input("\n Enter Value Name (e.g name , priority , status) To Update: "))
        updated_value = input("\n Enter Updated Value: ")
        update_task(index,update_key,updated_value)

    elif user_input == 5:
            print("\nTHANK YOU FOR USING")
            break
        
    else:
        print("\nAccept Only 1,2,3,4")

