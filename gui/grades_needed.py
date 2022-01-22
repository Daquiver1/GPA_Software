import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic2 import *

class InputDialog2(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.random()


	def random(self):
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		self.old_cgpa = self.getOldGpa()
		self.new_cgpa = self.getNewGpa()
		self.old_cred = self.getOldCredit()
		self.new_cred = self.getNewCredit()
		self.course_num = self.getNumCourse()

		self.yaw = calc_gpa_needed(self.old_cgpa, self.new_cgpa, self.old_cred, self.new_cred)
		self.nii = gpa_to_grades(self.yaw, self.course_num)

		self.showGPA()
		  
	def getOldGpa(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Your Current GPA: ", 0.00, 0, 100000, 2)
		return i

	def getNewGpa(self):
		i, okPressed = QInputDialog.getDouble(self, "Desired","Your Desired GPA: ", 0.00, 0, 100000, 2)
		return i

	def getNumCourse(self):
		i, okpressed = QInputDialog.getInt(self, "Number of Courses", "How many courses: ", 0, 0, 100000, 1)
		return i

	def getOldCredit(self):
		i, okpressed = QInputDialog.getInt(self, "Old Credit Hours", "Your current credit hours: ", 0, 0, 100000, 1)
		return i

	def getNewCredit(self):
		i, okpressed = QInputDialog.getInt(self, "New Credit Hours", "Your new credit hours: ", 0, 0, 100000, 1)
		return i

	def showGPA(self):
		if type(self.yaw) == str:
			return QMessageBox.about(self, "Title", self.yaw)

		return QMessageBox.about(self, "Title", f"""In order to move from a CGPA of {self.old_cgpa} to a CGPA of {self.new_cgpa} you need to get a gpa of {self.yaw} this semester and a GPA of {self.yaw} requries minimum grade(s) of {self.nii}""")

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog()
	exit(0)

