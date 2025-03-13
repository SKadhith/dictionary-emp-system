# Solution
employees = {}

def add_employee():
    emp_id = "E" + str(100 + len(employees) + 1) 
    name = input("Enter Name: ")
    if not name.replace(" ", "").isalpha():
        print("Invalid name! Only alphabets allowed.")
        return
    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Invalid age! Age must be a positive number.")
            return
    except ValueError:
        print("Invalid input! Age must be a number.")
        return
    department = input("Enter Department: ")
    employees[emp_id] = {"name": name, "age": age, "department": department}
    print(f"Employee {emp_id} added successfully!\n")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee {emp_id} removed successfully!\n")
    else:
        print("Employee ID not found!\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        name = input("Enter New Name (leave blank to keep unchanged): ")
        if name and not name.replace(" ", "").isalpha():
            print("Invalid name! Only alphabets allowed.")
            return
        age_input = input("Enter New Age (leave blank to keep unchanged): ")
        if age_input:
            try:
                age = int(age_input)
                if age <= 0:
                    print("Invalid age!")
                    return
            except ValueError:
                print("Invalid input! Age must be a number.")
                return
            employees[emp_id]["age"] = age
        department = input("Enter New Department (leave blank to keep unchanged): ")
        if name:
            employees[emp_id]["name"] = name
        if department:
            employees[emp_id]["department"] = department
        print(f"Employee {emp_id} updated successfully!\n")
    else:
        print("Employee ID not found!\n")

def search_employee():
    search = input("Enter Employee ID or Name to search: ").lower()
    found = False
    for emp_id, details in employees.items():
        if search == emp_id.lower() or search == details["name"].lower():
            print(f"{emp_id}: {details}")
            found = True
    if not found:
        print("No matching employee found!\n")

def sort_employees():
    print("Sort by: 1. Name  2. Age  3. Department")
    choice = input("Enter choice: ")
    if choice == "1":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]["name"])
    elif choice == "2":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]["age"])
    elif choice == "3":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]["department"])
    else:
        print("Invalid choice!\n")
        return
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details}")
    print()

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee\n2. Remove Employee\n3. Update Employee\n4. Search Employee\n5. Sort Employees\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()

