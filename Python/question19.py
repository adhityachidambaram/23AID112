grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
count_A = 0
count_B = 0
count_C = 0
below_70 = 0
for i in grades:
    if i >= 90:
        count_A += 1
    elif 80 <= i <= 89:
        count_B += 1
    elif 70 <= i <= 79:
        count_C += 1
    else:
        below_70 += 1
    
print("Number of A grades:", count_A)
print("Number of B grades:", count_B)
print("Number of C grades:", count_C)
print("Number of below 70 grades:", below_70)