print("WELCOME TO THE CREATIVE GRADE CALCULATOR!")
score = int(input("ENTER YOUR SCORE: "))

print("PLEASE CUSTOMIZE THE GRADING SCALE BY SPECIFYING THE MINIMUM SCORE REQUIRED FOR EACH GRADE.")
a_min = int(input("Minimum score for an A: "))
b_min = int(input("Minimum score for a B: "))
c_min = int(input("Minimum score for a C: "))
d_min = int(input("Minimum score for a D: "))

print("CALCULATING YOUR GRADE...")

if score >= a_min:
    grade = 'A'
elif score >= b_min:
    grade = 'B'
elif score >= c_min:
    grade = 'C'
elif score >= d_min:
    grade = 'D'
else:
    grade = 'F'

print("Your grade is", grade)

if grade == 'A':
    print("Congratulations! You earned an A!")
elif grade == 'B':
    print("Good job! You earned a B.")
elif grade == 'C':
    print("Not bad! You earned a C.")
elif grade == 'D':
    print("You passed, but you'll need to work harder next time.")
else:
    print("Sorry, you failed. Better luck next time!")