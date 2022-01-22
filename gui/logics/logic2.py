def calc_gpa_needed(old_cgpa, new_cgpa, old_chours, new_chours):
	"""Calculate the GPA needed in order to hit a specified CGPA.

	Args: 
		old_cgpa: Your current cgpa. Type: float.
		new_cgpa: Your desired_cgpa. Type: float.
		old_chours: Your credit hours for your previous semestes. Type: int
		new_chours: Your credit hours for your current or next semester. Type: int

	Returns:
		The minimum gpa needed required to achieve your desired cgpa. Type: float 

	Raises:
		ValueError: If the user enters invalid value types.
	"""
	total_chours = old_chours + new_chours
	new_points = total_chours * new_gpa
	old_points = old_chours * old_gpa
	diff_points = new_points - old_points
	min_gpa = diff_points / new_chours
	if min_gpa > 4.00:
		return f"You can't achieve a {new_gpa} cgpa in this semester, try again next sem"

	return min_gpa

old = float(input("Please enter your current cgpa: "))
new = float(input("Please enter your desired cgpa: "))
c_old = int(input("Please enter your old credit hours: "))
c_new = int(input("Please enter your new credit hours: "))

print(calc_gpa_needed(old, new, c_old, c_new))