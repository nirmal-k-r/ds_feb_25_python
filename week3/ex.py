print("Welcome to the Simple grade calculator")

num_subjects= int(input("Enter the number of subjects: "))

total=0

for i in range(num_subjects):
    mark=int(input(f"Enter the mark for subject {i+1}: "))
    total=total+mark

average=total/num_subjects

if (average>=90):
    grade="A"
elif (average>=80):
    grade="B"
elif (average>=70):
    grade="C"
elif (average>=60):
    grade="D"
else:
    grade="F"

print(f"The average mark is {average} and the grade is {grade}")