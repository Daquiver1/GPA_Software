# TODO: Add the weighting system
# TODO: Document program

# Calculate the GPA of a student
"""
Inputs: # number of courses, grades(A), credit hours of courses.

Output: A grade
"""


main_grades = {"A": 4.0, "B+": 3.5,
		 "B": 3.0, "C+": 2.5, 
		 "C": 2.0, "D+": 1.5,
		 "D": 1.0, "E": 0,
		 "F": 0}

def gpa_calc():
	count = 0
	hours = 0
	try:
		course_num = int(input("Please enter the num of courses you are offering: "))
	except ValueError:
		return "value must be an integer"
	for i in range(course_num):
		grades = input(f"Enter grade{i+1}: ").upper()

		if grades not in main_grades:
			return "Enter a valid grade"

		try:
			c_hours = int(input(f"Enter the credit hour of grade {grades}: "))
		except ValueError:
			return "Value must be an integer."
			
		count += main_grades[grades] * c_hours
		hours += c_hours

	return count/hours


print(gpa_calc())