print("Hey! there Welcome to a small grading sytem.")
print("This program will take some input and returns the grade according to that provided figure")
grade = int(input("Enter your marks between (0 and 100):"))
print("A+") if grade >= 90 and grade < 101 else print("B") if grade >=80 and grade < 90 else print("Fail") if grade < 80 and grade > 0 else print("Invalid number")