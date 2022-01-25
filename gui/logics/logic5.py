def fgpa(cgpa1, cgpa2, cgpa3, cgpa4):

	if type(cgpa1) and type(cgpa2) and type(cgpa3) and type(cgpa4) not in [float,int]:	# Error handling for when the function is imported from another file.
		return "Please enter a decimal or integer for your cgpas"

	if cgpa1 >4 or cgpa2 > 4 or cgpa3 > 4 or cgpa4 > 4:
		return "Your cgpas should be between 0 and 4"

	if cgpa1 < 0 or cgpa1 <0 or cgpa3 < 0 or cgpa4 <0:
		return "Your cgpas should be between 0 and 4"

	temp1 = cgpa1 *1/6
	temp2 = cgpa2 * 1/6
	temp3 = cgpa3 * 2/6
	temp4 = cgpa4 * 2/6

	final_gpa = temp1 + temp2 + temp3 + temp4

	final_gpa = round(final_gpa, 2)

	return f"Your FGPA is {final_gpa}"

if __name__ == "__main__":
	try:
		cgpa1 = float(input("Please enter level 100's cgpa: "))
		cgpa2 = float(input("Please enter level 200's cgpa: "))
		cgpa3 = float(input("Please enter level 300's cgpa: "))
		cgpa4 = float(input("Please enter level 400's cgpa: "))
		print(fgpa(cgpa1, cgpa2, cgpa3, cgpa4))
	except ValueError:
		print("Please enter a decimal for your gpas")