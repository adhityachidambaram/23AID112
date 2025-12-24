# Creating different data types in Python

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
Student = input("Are you a student? (yes/no): ")

# printing details
print("Name:", name)
print("Age:", age)
print("Height:", height)
if Student == "yes":
    print("Student: yes")
else:
    print(name, " is not a Student")
