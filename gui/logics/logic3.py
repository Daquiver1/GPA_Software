def highest_cgpa(old_chours, new_chours, old_cgpa):
	"""Calculate the highest CGPA one can attain.

	Args: 
		old_chours: Your credit hours for your previous semesters. Type: int
		new_chours: Your credit hours for your current or next semester. Type: int
		old_cgpa: Your current cgpa. Type: float or int.

	Returns:
		Maximum CGPA a user can attain. Type: float 

	Raises:
		None
	"""
	if type(old_cgpa) not in [float, int] and type(old_chours) and type(new_chours) not in [int]:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal or integer for your cgpas"

	if old_cgpa <0 and old_cgpa >4:
		return "Your cgpas should be between 0 and 4"

	total_chours = old_chours + new_chours						# Total credit hours.
	old_points = old_chours * old_cgpa							# Weight of current gpa over current credit hours.
	try:
		max_cgpa = ((new_chours * 4) + old_points) / total_chours	# Weight of new gpa over sem's credit hours/ divided by total credit hours.
	except ZeroDivisionError:
		return "Invalid Inputs"
	max_cgpa = round(max_cgpa, 2)

	levels = grade_to_classification(max_cgpa)					# Retrieve level of maximum CGPA

	return f"With a {old_cgpa} CGPA the highest CGPA you can attain this semester is {max_cgpa} which is {levels}"

def grade_to_classification(gpa):
	"""Transorm a GPA to it's corresponding level.

	Args: 
		GPA: Users gpa. Type: float

	Returns:
		The corresponding level of inputted GPA. Type: String	

	Raises:
		None
	"""
	if gpa >= 3.60:
		return "First Class"
	elif gpa >= 3.00: 
		return "Second Class Upper"
	elif gpa >= 2.00:
		return "Second class Lower"
	elif gpa >= 1.50:
		return "Third Class"
	elif gpa >= 1.00:
		return "Pass"
	elif gpa < 1.00:
		return "Fail"
	else:
		return "Invalid Input"

if __name__ == "__main__":
	try:
		old_cred = int(input("Please enter your current credit hours: "))
		new_cred = int(input("Please enter this semester's credit hours: "))
		old_cgpa = float(input("Please enter your current CGPA: "))
		print(highest_cgpa(old_cred, new_cred, old_cgpa))
	except ValueError:
		print("Please enter a decimal for your CGPAS")

