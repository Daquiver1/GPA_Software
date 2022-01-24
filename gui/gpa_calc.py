import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic4 import new_gpa_calc

class InputDialog4(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.random()


	def random(self):
		self.course_num = self.getCourses()
		self.grades = []
		self.credits = []

		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		for i in range(self.course_num):
			self.grades.append(self.getText())
			if self.grades[i] == None:
				break
			self.credits.append(self.getCredit())

		self.showGPA()
		  
	def getCourses(self):
		i, okPressed = QInputDialog.getInt(self, "Courses","Number of Courses:", 4, 0, 10, 1)
		return i

	def getText(self):
		text, okPressed = QInputDialog.getText(self, "Grades","Enter your grade:", QLineEdit.Normal, "")
		if len(text) == 1 or len(text) == 2:
			return text.upper()
		return None

	def getCredit(self):
		i, okpressed = QInputDialog.getInt(self, "Credit Hours", "Credit hour of grade:", 4, 0, 10, 1)
		return i

	def showGPA(self):
		yaw = new_gpa_calc(self.grades, self.credits)
		QMessageBox.about(self, "Title", f"Your gpa is {yaw}")

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog4()
	exit(0)

