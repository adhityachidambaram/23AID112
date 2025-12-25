# Enter inputs as Strings
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

#  converting the String inputs to integers
num1 = int(num1_str)
num2 = int(num2_str)
print("The sum of two numbers is :", num1 + num2)
print("The difference of two numbers is :", num1-num2)
print("The product of two numbers is :", num1 * num2)
if num1 > num2:
    print(num1, " is greater than ", num2)
elif num2 > num1:
    print(num2, " is greater than ", num1)
else:
    print("Both numbers are equal")
