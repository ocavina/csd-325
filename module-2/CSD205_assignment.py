# Oscar Avina
# 03/1/2026
# Module 9.2 Assignment
# This program calculates and displays a student's cumulative GPA using a Student Class.

grade_points = {
  "A": 4.0,
  "B+": 3.5,
  "B": 3.0,
  "C+": 2.5,
  "C": 2.0,
  "D": 1.0,
  "F": 0.0,
}

class Student: # student class to store student information and calculate GPA
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.total_credits = 0
    self.total_grade_points = 0

  def add_course(self, credits, grade): # method to add a course's credits and grade points to the student's totals
      self.total_credits += credits
      self.total_grade_points += credits * grade_points[grade] # calculates the grade points for the course and adds it to the total grade points

  def get_gpa(self): # method to calculate and return the student's cumulative GPA
    if self.total_credits == 0:
      return 0.0
    return self.total_grade_points / self.total_credits

first_name = input("Please enter the student's first name: ").strip()
last_name = input("Please enter the student's last name: ").strip()
student = Student(first_name, last_name) # create a Student object with the provided first and last name

while True: # loop to allow the user to enter multiple courses until they choose to stop
  credits = float(input("Please enter the number of credits for a course: ").strip())
  grade = input("Please enter the grade received for this course (A, B+, B, C+, C, D, F): ").strip().upper()
  student.add_course(credits, grade) #use the add_course method to update the student's total credits and grade points

  more_courses_to_add = input("Do you want to enter another course? Please enter 'yes' or 'no'): ").strip().lower()
  if more_courses_to_add == 'no' or more_courses_to_add == 'n': # if the user does not want to add more courses, exit the loop
    break

print(f"{student.first_name} {student.last_name}'s cumulative GPA is: {student.get_gpa():.2f}")