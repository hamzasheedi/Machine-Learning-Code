db = {}

def get_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_str_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        else:
            print("❌ Input cannot be empty.")

def add_student(id, name, age, grades):
    if id in db:
        print("❌ ID already exists. Use a new ID.")
        return
    db[id] = {
        "name": name,
        "age": age,
        "grades": grades
    }
    print("✅ Student added successfully.")

def delete_student(id):
    if id in db:
        db.pop(id)
        print("✅ Student deleted.")
    else:
        print(f"❌ ID {id} does not exist.")

def search_student(id):
    if id in db:
        student = db[id]
        print(f"Name: {student['name']} | Age: {student['age']} | Grades: {student['grades']}")
    else:
        print(f"❌ ID {id} does not exist.")

def display_db():
    if not db:
        print("📂 Database is empty.")
        return
    for id, student in db.items():
        print(f"ID: {id} | Name: {student['name']} | Age: {student['age']} | Grades: {student['grades']}")

# -------- MENU --------
while True:
    print("\n1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display Database")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = get_int_input("Enter ID: ")
        name = get_str_input("Enter name: ")
        age = get_int_input("Enter age: ")
        grades = get_str_input("Enter grades: ")
        add_student(id, name, age, grades)

    elif choice == "2":
        id = get_int_input("Enter ID to delete: ")
        delete_student(id)

    elif choice == "3":
        id = get_int_input("Enter ID to search: ")
        search_student(id)

    elif choice == "4":
        display_db()

    elif choice == "5":
        print("👋 Exiting program.")
        break

    else:
        print("❌ Invalid choice. Try again.")
