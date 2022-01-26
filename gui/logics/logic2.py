main_grades = {"A": 4.0, "B+": 3.5,
		 "B": 3.0, "C+": 2.5, 
		 "C": 2.0, "D+": 1.5,
		 "D": 1.0, "E": 0,
		 "F": 0}

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
	if type(old_cgpa) and type(new_cgpa) not in [float, int] and type(old_chours) and type(new_chours) != int:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal for your CGPA and an integer for your credit hours"

	if old_cgpa < 0 and old_cgpa > 4 and new_cgpa < 0 and new_cgpa > 4:
		return "Your CGPA should be between 4 and 0"

	total_chours = old_chours + new_chours
	new_points = total_chours * new_cgpa		# Average weight of your desired gpa over your total course hours.
	old_points = old_chours * old_cgpa			# Average weight of your current gpa over your current course hours.
	diff_points = new_points - old_points		# Difference between your desired weight and your current weight.
	try: 
		min_gpa = diff_points / new_chours			# Your diff weight scaled to your new hours, to reflect the GPA you need. 
	except ZeroDivisionError:
		return "Invalid values"

	if min_gpa > 4.00:
		return f"You can't achieve a {new_cgpa} CGPA this semester, try again next semester"

	if min_gpa <0.00:
		return f"You can't achieve a {new_cgpa} CGPA this semester, it's impossible. The lowest you can achieve is"

	min_gpa = round(min_gpa, 2)

	return min_gpa

def getList(dict):
	"""Returns dict keys as list.

	Args: 
		dict: Dictionary. Type: dict

	Returns:
		Dictionary keys of type list

	Raises:
		None
	""" 
	return list(dict.keys())
	  
def gpa_to_grades(gpa, course_num):
	"""Converts GPA to grades

	Args: 
		gpa: Your current cgpa. Type: float or int.
		course_num: number of courses. Type: int

	Returns:
		The grades needed to acquire a specific gpa. Type: list

	Raises:
		None
	"""
	if type(gpa) == str:	# Handles error
		return gpa 

	i = 0 								# Grade
	temp = 0.00							# Temporary gpa, 
	grade = getList(main_grades)		# Get the grades (A to F)
	grades_needed = []			
	while True:					
		temp += main_grades[grade[i]]/course_num	# Add gradepoint of grade to temp	

		if temp > gpa and i > 5: 	# E and F carry zero weight. So end loop, when grade is on 5(E) and temp > gpa
			break

		if temp > gpa:				# If Grade[i] can't be added without exceeding gpa, delete added value and rollover to next grade.
			temp -= main_grades[grade[i]]/course_num		
			i += 1
		else:
			grades_needed.append(grade[i])			#If it can, add grade letter to list and continue.

	return f"For this info, you'll need a {gpa} GPA which requires minimum grade(s) of {grades_needed}"


if __name__ == "__main__":
	try:
		old = float(input("Please enter your current cgpa: "))
		new = float(input("Please enter your desired cgpa: "))
		c_old = int(input("Please enter your old credit hours: "))
		c_new = int(input("Please enter your new credit hours: "))
		yaw = calc_gpa_needed(old, new, c_old, c_new)
		print(gpa_to_grades(yaw, 7))
	except ValueError:
		print("Please enter a decimal for your gpa and an integer for your credit hours")
	