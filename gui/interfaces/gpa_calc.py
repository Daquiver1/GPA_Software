import sys
sys.path.insert(0, "C:\\Users\\Anita Agyepong\\Documents\\Daquiver's Quivers\\Python\\GPA_Software\\gui\\logics")
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QInputDialog, QApplication, QMessageBox, QLineEdit
from logic5 import *

class InputDialog5(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.main()


	def main(self):
		self.course_num = self.getCourses()
		self.grades = []
		self.credits = []

		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		for i in range(self.course_num):			# Retrieve all grades and corresponding credit hours. 
			self.grades.append(self.getText())
			if self.grades[i] == None:
				break
			self.credits.append(self.getCredit())

		self.showGPA()
		  
	def getCourses(self):
		""" A function to retrieve the number of courses of a student. """
		i, okPressed = QInputDialog.getInt(self, "Courses","Number of Courses:", 4, 0, 100, 1)
		return i

	def getText(self):
		""" A function to retrieve the grade of a student. """
		text, okPressed = QInputDialog.getText(self, "Grades","Enter your grade:", QLineEdit.Normal, "")
		if len(text) == 1 or len(text) == 2:
			return text.upper()
		return None

	def getCredit(self):
		""" A function to retrieve the credit hours of a student. Corresponds with grade. """
		i, okpressed = QInputDialog.getInt(self, "Credit Hours", "Credit hour of grade:", 4, 0, 10, 1)
		return i

	def showGPA(self):
		""" A function to display the GPA of a student. """
		GPA = new_gpa_calc(self.grades, self.credits)
		QMessageBox.about(self, "Title", GPA)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog5()
	exit(0)

