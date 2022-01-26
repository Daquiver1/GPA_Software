import sys
sys.path.insert(0, "C:\\Users\\Anita Agyepong\\Documents\\Daquiver's Quivers\\Python\\GPA_Software\\gui\\logics")
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QInputDialog, QMessageBox, QApplication
from logic3 import *

class InputDialog3(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.main()


	def main(self):
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		self.old_cgpa = self.getOldGpa()
		self.old_cred = self.getOldCredit()
		self.new_cred = self.getNewCredit()

		self.showGPA()
		  
	def getOldGpa(self):
		""" A function to retrieve the current CGPA of student. """
		i, okPressed = QInputDialog.getDouble(self, "Current","Your Current GPA: ", 0.00, 0, 4.0, 2)
		return i

	def getOldCredit(self):
		""" A function to retrieve the current credit hours of student. """
		i, okpressed = QInputDialog.getInt(self, "Old Credit Hours", "Your current credit hours: ", 0, 0, 100, 1)
		return i

	def getNewCredit(self):
		""" A function to retrieve the credit hours of a semester. """
		i, okpressed = QInputDialog.getInt(self, "New Credit Hours", "Credit hours for this semester ", 0, 0, 30, 1)
		return i

	def showGPA(self):
		""" A function to display the maximum CGPA of a student. """
		max_cgpa = highest_cgpa(self.old_cred, self.new_cred, self.old_cgpa)
		return QMessageBox.about(self, "Title", max_cgpa)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog3()
	exit(0)

