# Age in Integer
age = int(input("Enter your age: "))

#Output
if age<13:
    print("You are a child.")
elif 13<=age<=17:
    print("You are a teenager.")
elif 18<=age<=64:
    print("You are an adult.")
else:
    print("You are a senior")
