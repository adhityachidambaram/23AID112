#a) print each number
num =  [12, 45, 3, 98, 7, 34, 21]
for i in num:
    print(i)

#b) print only numbers greater than 30 
for i in num:
    if i > 30:
        print(i)

#c) count how many numbers are greater than 30
count = 0
for i in num:
    if i > 30:
        count += 1
print("Count of numbers greater than 30:",count)

