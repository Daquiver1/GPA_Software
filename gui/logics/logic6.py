def fgpa(cgpa1, cgpa2, cgpa3, cgpa4):
	"""Calculates the FGPA of a student. Multiplies each level's cgpa by it's corresponding weight.
		Then sums it up.

	Args: 
		CGPA1: Level 100's cgpa. Type: float
		CGPA2: Level 200's cgpa. Type: float
		CGPA3: Level 300's cgpa. Type: float
		CGPA4: Level 400's cgpa. Type: float

	Returns:
		The FGPA of student. Type: String?

	Raises:
		None
	"""

	if type(cgpa1) and type(cgpa2) and type(cgpa3) and type(cgpa4) not in [float,int]:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal or integer for your CGPA"

	if cgpa1 >4 and cgpa2 > 4 and cgpa3 > 4 and cgpa4 > 4:
		return "Your CGPA should be between 0 and 4"

	if cgpa1 < 0 and cgpa1 < 0 and cgpa3 < 0 and cgpa4 <0:
		return "Your CGPA should be between 0 and 4"

	temp1 = cgpa1 *1/6 				# Weight 1
	temp2 = cgpa2 * 1/6 			# Weight 2
	temp3 = cgpa3 * 2/6 			# Weight 3
	temp4 = cgpa4 * 2/6 			# Weight 4

	final_gpa = temp1 + temp2 + temp3 + temp4
	final_gpa = round(final_gpa, 2)

	levels = grade_to_classification(final_gpa)

	return f"""
Level 100: {cgpa1}, Level 200: {cgpa2}, Level 300: {cgpa3}, Level 400: {cgpa4} 
For these CGPA, your FGPA is {final_gpa} which is a {levels}"""

def grade_to_classification(grade):
	"""Transorm a GPA to it's corresponding level.

	Args: 
		GPA: Users gpa. Type: float

	Returns:
		The corresponding level of inputted GPA. Type: String	

	Raises:
		None
	"""
	if grade >= 3.60:
	 return "First Class"
	elif grade >= 3.00: 
		return "Second Class Upper"
	elif grade >= 2.00:
		return "Second class Lower"
	elif grade >= 1.50:
		return "Third Class"
	elif grade >= 1.00:
		return "Pass"
	elif grade < 1.00:
		return "Fail"
	else:
		return "Invalid Input"


if __name__ == "__main__":
	try:
		cgpa1 = float(input("Please enter level 100's cgpa: "))
		cgpa2 = float(input("Please enter level 200's cgpa: "))
		cgpa3 = float(input("Please enter level 300's cgpa: "))
		cgpa4 = float(input("Please enter level 400's cgpa: "))
		print(fgpa(cgpa1, cgpa2, cgpa3, cgpa4))
	except ValueError:
		print("Please enter a decimal for your gpas")