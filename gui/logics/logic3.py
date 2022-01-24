def calc_gpa_needed(old_cgpa, new_cgpa, old_chours, new_chours):
	"""Calculate the GPA needed in order to hit a specified CGPA.

	Args: 
		old_cgpa: Your current cgpa. Type: float or int.
		new_cgpa: Your desired_cgpa. Type: float or int.
		old_chours: Your credit hours for your previous semestes. Type: int
		new_chours: Your credit hours for your current or next semester. Type: int

	Returns:
		The minimum gpa needed required to achieve your desired cgpa. Type: float 

	Raises:
		None
	"""
	if type(old_cgpa) not in [float,int] or type(new_cgpa) not in [float, int] or type(old_chours) != int or type(new_chours) != int:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal for your gpa and an integer for your credit hours"

	if old_cgpa < 0 or old_cgpa > 4 or new_cgpa < 0 or new_cgpa > 4:
		return "Your cgpas should be between 4 and 0"

	total_chours = old_chours + new_chours
	new_points = total_chours * new_cgpa		# Average weight of your desired gpa over your total course hours.
	old_points = old_chours * old_cgpa			# Average weight of your current gpa over your current course hours.
	diff_points = new_points - old_points		# Difference between your desired weight and your current weight.
	try: 
		min_gpa = diff_points / new_chours			# Your diff weight scaled to your new hours, to reflect the GPA you need. 
	except ZeroDivisionError:
		return "You are dividing by zero. That's illogical."

	# min_gpa = round(min_gpa, 2)

	# if min_gpa > 4.00:
	# 	return f"You can't achieve a {new_cgpa} cgpa this semester, try again next semester"


	return min_gpa

print(calc_gpa_needed(3.4, 3.76, 15, 21))
