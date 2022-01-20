import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic1 import new_gpa_calc

class InputDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.course_num = self.getCourses()

		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		self.grades = {}
		for i in range(self.course_num):
			self.grades[self.getText()] = self.getCredit()

		showGPA(self)
		  
	def getCourses(self):
		i, okPressed = QInputDialog.getInt(self, "Courses","Number of Courses:", 4, 0, 100, 1)
		return i

	def getText(self):
		text, okPressed = QInputDialog.getText(self, "Grades","Enter your grade:", QLineEdit.Normal, "")
		return text 

	def getCredit(self):
		i, okpressed = QInputDialog.getInt(self, "Credit Hours", "Credit hour of grade:", 4, 0, 100, 1)
		return i

	def showGPA(self):
		new_gpa_calc(self.grades)


if __name__ == '__main__':

	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog()
	if dialog.exec():
		print(dialog.getInputs())
	exit(0)

