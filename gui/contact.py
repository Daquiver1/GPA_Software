import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic6 import Myself

class InputDialog6(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.showMyself()

	def showMyself(self):
		yaw = Myself()
		QMessageBox.about(self, "Title", yaw)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog6()
	exit(0)

