#name = input("what is your name?")
#age = int(input("what is your age?"))

#print("Helloo","My name is",name,"and", "I am",age,"years old")

"""num = [1,2,3,4,5]
num.append(6)
num.remove(4)
print(num)"""

#LOOPS
"""for i in range(1,11):
    print(i)"""
#Functions
"""def greet(name):
    return "Hello" + name
print(greet("Alice"))"""
#Conditions
"""num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")"""

#Reverse a string
"""s = "Hello python"
reverse_s = s[::-1]
print(reverse_s)"""
# Palindrome Check
"""s = "hello"
if s == s[::-1]:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome:")"""
#factorial
"""n = 5
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("factorial of",n,"is",factorial)"""

#Maximum in a list
"""nums = [20,30,40,50]
print(max(nums))"""
"""n = 7
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b"""

#Student Management Ststem(CLI)

print("(:: Welcome to the Student Management System ::)")


students = []

def add_student(name):
    students.append(name)
    print("Student added successfully.")

def view_students():
    if not students:
        print("No students found.")
    else:
        print("List of students:")
        for student in students:
            print(students)

while True:
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
     name = input("Enter student name:")
     add_student(name)
    elif choice == 2:
     view_students()
    elif choice == 3:
     print("Exiting the system. Goodbye!")
     break
    else:
     print("Invalid choice. Please try again.")
