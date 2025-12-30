import random
set=[]

for item in range(8):
    set.append(random.randint(1,100))

print("Generated list:",set)

#A)biggest number in the list
biggest=set[0]

for n in set:
    if n>biggest:
        biggest=n

print("The Biggest Number is:",biggest)

#B)smallest number in the list
smallest=set[0]

for n in set:
    if n<smallest:
        smallest=n

print("The Smallest Number is:",smallest)