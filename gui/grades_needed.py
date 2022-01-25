import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic2 import *

class InputDialog2(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.random()


	def main(self):
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		self.old_cgpa = self.getOldGpa()
		self.new_cgpa = self.getNewGpa()
		self.old_cred = self.getOldCredit()
		self.new_cred = self.getNewCredit()
		self.course_num = self.getNumCourse()

		self.GPA = calc_gpa_needed(self.old_cgpa, self.new_cgpa, self.old_cred, self.new_cred)
		self.GRADES = gpa_to_grades(self.GPA, self.course_num)

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
		return QMessageBox.about(self, "Title", f"""For {self.course_num} courses in order to move from a CGPA of {self.old_cgpa} to a CGPA of {self.new_cgpa}, {self.nii}""")

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog2()
	exit(0)

