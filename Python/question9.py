#Determining exam results based on score
#Input 
score1 = int(input("Enter the score for first exam(0-100) :"))
score2 = int(input("Enter the score for second exam(0-100) :"))

#Output
if score1>=50 and score2>=50:
    print("You Passed!")
else:
    print("You need to retake some exams.")
    