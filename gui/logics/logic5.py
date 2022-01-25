def fgpa(cgpa1, cgpa2, cgpa3, cgpa4):

	if type(cgpa1) and type(cgpa2) and type(cgpa3) and type(cgpa4) not in [float,int]:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal or integer for your cgpas"

	if cgpa1 >4 and cgpa2 > 4 and cgpa3 > 4 and cgpa4 > 4:
		return "Your cgpas should be between 0 and 4"

	if cgpa1 < 0 and cgpa1 < 0 and cgpa3 < 0 and cgpa4 <0:
		return "Your cgpas should be between 0 and 4"

	temp1 = cgpa1 *1/6
	temp2 = cgpa2 * 1/6
	temp3 = cgpa3 * 2/6
	temp4 = cgpa4 * 2/6


	final_gpa = temp1 + temp2 + temp3 + temp4

	final_gpa = round(final_gpa, 2)

	yaw = grade_to_classification(final_gpa)

	return f"""
Level 100: {cgpa1}, Level 200: {cgpa2}, Level 300: {cgpa3}, Level 400: {cgpa4} 
For these CGPA, your FGPA is {final_gpa} which is {yaw}"""

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
		cgpa1 = float(input("Please enter level 100's cgpa: "))
		cgpa2 = float(input("Please enter level 200's cgpa: "))
		cgpa3 = float(input("Please enter level 300's cgpa: "))
		cgpa4 = float(input("Please enter level 400's cgpa: "))
		print(fgpa(cgpa1, cgpa2, cgpa3, cgpa4))
	except ValueError:
		print("Please enter a decimal for your gpas")