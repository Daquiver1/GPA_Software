import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logics'))
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QMessageBox, QApplication, QInputDialog
from logic2 import *

class InputDialog2(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.main()


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
		""" A function to retrieve the current CGPA of student. """
		i, okPressed = QInputDialog.getDouble(self, "Current","Your Current GPA: ", 0.00, 0, 4.0, 2)
		return i

	def getNewGpa(self):
		""" A function to retrieve the desired CGPA of student. """
		i, okPressed = QInputDialog.getDouble(self, "Desired","Your Desired GPA: ", 0.00, 0, 4.0, 2)
		return i

	def getNumCourse(self):
		""" A function to retrieve the number of courses of a student. """
		i, okpressed = QInputDialog.getInt(self, "Number of Courses", "How many courses: ", 0, 0, 20, 1)
		return i

	def getOldCredit(self):
		""" A function to retrieve the current credit hours of a student. """
		i, okpressed = QInputDialog.getInt(self, "Old Credit Hours", "Your current credit hours: ", 0, 0, 1000, 1)
		return i

	def getNewCredit(self):
		""" A function to retrieve a student's credit hours. Only for a particular sem. Not cumulative. """
		i, okpressed = QInputDialog.getInt(self, "New Credit Hours", "Your new credit hours: ", 0, 0, 30, 1)
		return i

	def showGPA(self):
		""" A function to display the grades a student needs to attain a particular cgpa. """

		return QMessageBox.about(self, "Title", f"""Courses: {self.course_num}\n Current CGPA: {self.old_cgpa}\n Desired CGPA: {self.new_cgpa}\n Current Credit Hours: {self.old_cred}\n Semesters Credit Hours: {self.new_cred}\n {self.GRADES}""")

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog2()
	exit(0)

