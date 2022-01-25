def highest_cgpa(old_chours, new_chours, old_cgpa):
	if type(old_cgpa) not in [float, int] and type(old_chours) and type(new_chours) not in [int]:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal or integer for your cgpas"

	if old_cgpa <0 and old_cgpa >4:
		return "Your cgpas should be between 0 and 4"

	total_chours = old_chours + new_chours
	old_points = old_chours * old_cgpa

	max_cgpa = ((new_chours * 4) + old_points) / total_chours

	max_cgpa = round(max_cgpa, 2)

	levels = grade_to_classification(max_cgpa)

	return f"With a {old_cgpa} CGPA the highest CGPA you can attain this semester is {max_cgpa} which is {levels}"

def grade_to_classification(grade):
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
		old_cred = int(input("Please enter your current credit hours: "))
		new_cred = int(input("Please enter this semester's credit hours: "))
		old_cgpa = float(input("Please enter your current CGPA: "))
		print(highest_cgpa(old_cred, new_cred, old_cgpa))
	except ValueError:
		print("Please enter a decimal for your CGPAS")

