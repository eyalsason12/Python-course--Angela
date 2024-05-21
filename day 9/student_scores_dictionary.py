student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    grade = student_scores[name]
    if grade > 90:
        student_grades[name] = "Outstanding"
    elif grade > 80:
        student_grades[name] = "Exceeted Expectation"
    elif grade > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "fail"

# 🚨 Don't change the code below 👇
print(student_grades)