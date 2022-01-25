import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic3 import *

class InputDialog3(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.random()


	def random(self):
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)

		self.old_cgpa = self.getOldGpa()
		self.old_cred = self.getOldCredit()
		self.new_cred = self.getNewCredit()

		self.showGPA()
		  
	def getOldGpa(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Your Current GPA: ", 0.00, 0, 4.0, 2)
		return i

	def getOldCredit(self):
		i, okpressed = QInputDialog.getInt(self, "Old Credit Hours", "Your current credit hours: ", 0, 0, 100000, 1)
		return i

	def getNewCredit(self):
		i, okpressed = QInputDialog.getInt(self, "New Credit Hours", "Credit hours for this semester ", 0, 0, 100000, 1)
		return i

	def showGPA(self):
		yaw = highest_cgpa(self.old_cred, self.new_cred, self.old_cgpa)

		return QMessageBox.about(self, "Title", yaw)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog3()
	exit(0)
