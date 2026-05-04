# Oscar Avina
# 05/3/2026
# Module 8.2 Assignment
# This program reads a JSON file, prints it, adds a new student, and writes the updated list back to the file.

import json

def print_student_list(student_list):
    for student in student_list: # loops through the student list and print each student's information
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

filename = "module-8/Student.json"
student_list = []

# reads JSON file
with open(filename) as student_file:
    student_list = json.load(student_file)

print("\nThis is the original Student list.")
print_student_list(student_list)

student_list.append({ # adds my info as a new student to the list
    "F_Name": "Oscar",
    "L_Name": "Avina",
    "Student_ID": 45606,
    "Email": "oscar.c.avina@gmail.com"
})

print("\nThis is the updated Student list.")
print_student_list(student_list)

# writes the updated student list back to the Student.json file
with open(filename, "w") as student_file:
    json.dump(student_list, student_file, indent=4)

print("\nThe student.json file was updated.")