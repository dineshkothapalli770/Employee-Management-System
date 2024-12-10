import mysql.connector
# Connect database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Dinu@11",  # Replace with your MySQL password
        database="employee_management"
    )
# Add employee
def add_employee(name,age,department,salary):
    conn = connect_db()
    cursor = conn.cursor()
    query = "insert into employees (name,age,department,salary) values (%s,%s,%s,%s)"
    values = (name,age,department,salary)
    cursor.execute(query,values)
    conn.commit()
    conn.close()
    print("Employee added successfully")
# view employees
def view_employees():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("Select*from employees")
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()
# Update Employee
def update_employee(employee_id,name,age,department,salary):
    conn = connect_db()
    cursor = conn.cursor()
    query = "update employees set name=%s,age=%s,department=%s,salary=%s where id=%s"
    values = (name,age,department,salary,employee_id)
    cursor.execute(query,values)
    conn.commit()
    conn.close()
# 
def delete_employee(employee_id):
    conn = connect_db()
    cursor = conn.cursor()
    query = "delete from employee where employee_id=%s"
    values = (employee_id)
    cursor.execute(query,values)
    conn.commit()
    conn.close()

# # Main menu
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            add_employee(name, age, department, salary)
        elif choice == '2':
            view_employees()
        elif choice == '3':
            employee_id = int(input("Enter Employee ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            department = input("Enter new department: ")
            salary = float(input("Enter new salary: "))
            update_employee(employee_id, name, age, department, salary)
        elif choice == '4':
            employee_id = int(input("Enter Employee ID to delete: "))
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



