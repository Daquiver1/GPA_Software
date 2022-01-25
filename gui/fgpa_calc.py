import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic5 import fgpa

class InputDialog5(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.main()


	def main(self):
		buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);
		layout = QFormLayout(self)
		
		self.first = self.getCGPA1()
		self.second = self.getCGPA2()
		self.third = self.getCGPA3()
		self.fourth = self.getCGPA4()

		self.showFGPA()
		  
	def getCGPA1(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Level 100 CGPA: ", 0.00, 0, 4.0, 2)
		return i

	def getCGPA2(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Level 200 CGPA: ", 0.00, 0, 4.0, 2)
		return i

	def getCGPA3(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Level 300 CGPA: ", 0.00, 0, 4.0, 2)
		return i

	def getCGPA4(self):
		i, okPressed = QInputDialog.getDouble(self, "Current","Level 400 CGPA: ", 0.00, 0, 4.0, 2)
		return i

	def showFGPA(self):
		FGPA = fgpa(self.first, self.second, self.third, self.fourth)
		QMessageBox.about(self, "Title", FGPA)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog5()
	exit(0)

