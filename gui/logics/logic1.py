# TODO: Add the weighting system
# TODO: Document program



main_grades = {"A": 4.0, "B+": 3.5,
		 "B": 3.0, "C+": 2.5, 
		 "C": 2.0, "D+": 1.5,
		 "D": 1.0, "E": 0,
		 "F": 0}

def gpa_calc():
	"""Calculate the GPA of a student

	Args: 
		None

	Returns:
		The resulting gpa

	Raises:
		ValueError: If the user enters invalid value types.
	"""
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
			
		count += main_grades[grades] * c_hours	# Total grade point.
		hours += c_hours	# Total credit hours

	return count/hours		# Gpa value

def new_gpa_calc(grades):
	count = 0
	total_hours = sum(grades.values())
	for i,v in grades.items():
		if i not in main_grades.keys():
			return "Invalid grade"
		count += main_grades[i] * grades[i]

	return count/total_hours

yaw = {"A":3, "B": 2, "D": 10}
print(new_gpa_calc(yaw))
print(gpa_calc())
