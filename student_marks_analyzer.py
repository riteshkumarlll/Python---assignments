# Student Marks Analyzer

name = input("Enter student name: ")

marks = []

subjects = ["Python", "Java", "Mathematics", "English", "Computer"]

for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

print("\n--- STUDENT RESULT ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
