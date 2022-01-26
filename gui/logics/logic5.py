from base import main_grades, grade_to_classification

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

	return f"For {total_gpt} total grade point and {sum(credit)} credit hours, your GPA is {gpa} which is a {levels}"

if __name__ == "__main__":
	grades = ["A", "B", "C"]
	credit = [3,2,3]
	print(new_gpa_calc(grades, credit))
