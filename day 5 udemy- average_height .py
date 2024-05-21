# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇

#calculate total height of the students
total_heights = 0
for height in student_heights:
    total_heights += height

#calculate the number of students
number_of_students = 0
for student in student_heights:
    number_of_students += 1

#calculate the average height of students
average_height = round(total_heights/number_of_students)

print(f"total heights= {total_heights}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")


