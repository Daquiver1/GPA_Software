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

main_grades = {"A": 4.0, "B+": 3.5,
		 "B": 3.0, "C+": 2.5, 
		 "C": 2.0, "D+": 1.5,
		 "D": 1.0, "E": 0,
		 "F": 0}