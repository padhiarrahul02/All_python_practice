#add new features like Store Student as Dictionary,Improved View,Delete Student,Update Menu

print("(:: welcome to the Student Management System:))")
students = []
def add_student():
    name = input("Enter student name:")
    age = int(input("Enter student age:"))
    marks = float(input("Enter student marks:"))
    student = {"name":name,"age":age,"marks":marks}
    students.append(student)
    print("Student added successfully.")

#view students
def view_students():
    if not students:
        print("No students found.")
    else:
        print("List of students:")
        for student in students:
            print("Name:",student["name"],"Age:",student["age"],"Marks:",student["marks"])
#delete student
def delete_student():
    name = input("Enter student name to delete:")
    found = False
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
            break
    if not found:
            print("Student not found.")
#update student
def update_student():
    name = input("Enter student name to update:")
    for student in students:
        if student["name"] == name:
            age = int(input("Enter new age:"))
            marks = float(input("Enter new marks:"))
            student["age"] = age
            student["marks"] = marks
            print("Student updated successfully.")
        else:
            print("Student not found.")
while True:
    print("\n1.Add Student::")
    print("2.View Students::")
    print("3.Delete Student::")
    print("4.Update Student::")
    print("5.Exit::")
    
    choice = int(input("Enter your choice:"))
    if choice == 1:
        add_student()
        
    elif choice == 2:
        if len(students) == 0:
            print("Invalid choice. First add students.")
        else:
            view_students()

        
    elif choice == 3:
        if len(students) == 0:
            print("Invalid choice. First add a student.")
        else:
            delete_student()
    elif choice == 4:
        if len(students) == 0:
            print("Invalid choice. First add a student.")
        else:
            update_student()
    elif choice == 5:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        

