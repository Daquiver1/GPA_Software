# TODO: Add the weighting system
# TODO: Document program

main_grades = {"A": 4.0, "B+": 3.5,
		 "B": 3.0, "C+": 2.5, 
		 "C": 2.0, "D+": 1.5,
		 "D": 1.0, "E": 0,
		 "F": 0}


def new_gpa_calc(grades, credit):
		"""Calculate the GPA or CGPA.

	Args: 
		grades: Student's grades. Type: List
		credit: Student's credit corresponding to grade. Type: List

	Returns:
		The GPA of the student. Type: String?

	Raises:
		None
	"""
	total_gpt = 0
	for i in range(len(grades)):
		if grades[i] not in main_grades.keys():
			return "Invalid grades"

		grades[i] = main_grades[grades[i]] 
		total_gpt += grades[i] * credit[i]		# Total gradepoint

	gpa = total_gpt / sum(credit)
	gpa = round(gpa, 2)

	levels = grade_to_classification(gpa)		# Retrieve level of maximum CGPA

	return f"For {total_gpt} total grade point and {sum(credit)} credit hours, your GPA is {gpa} which is {levels}"


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
	grades = ["A", "B", "C"]
	credit = [3,2,3]
	print(new_gpa_calc(grades, credit))
