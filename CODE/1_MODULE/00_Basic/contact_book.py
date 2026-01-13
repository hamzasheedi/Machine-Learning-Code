contact_book = {}


while True:
    user_input = int(input("\nWrite 1 For Add Or Update Contact\n 2 For Delete Contact \n 3 For Search Task \n 4 For Exiting\n"))
    if user_input == 1:
        def add_or_update_contact(name,number):
            try:
                print("\nTask Name Should Be Unique For Adding New Task \n For Updating Task Name Must Need To Be Same.")
                contact_book[name] = int(number)
                return
            except Exception:
                print("\nERROR OCCUR: ",Exception)
                return     
        name = str(input("Enter Contact Name: "))
        number = input("Enter Your Number")
        add_or_update_contact(name,number)

    elif user_input == 2:
        def delete_contact(name):
            contact_book.pop(name)
            return
        name = str(input("Enter Contact Name: "))
        delete_contact(name)
            
    elif user_input == 3:
        def search_contact(name):
            print(f"Name {name}: {contact_book[name]}")
            return
        name = str(input("Enter Contact Name: "))
        search_contact(name)

    
    elif user_input == 4:
        print("\nTHANK YOU FOR USING")
        break
    
    else:
        print("\nAccept Only 1,2,3,4")