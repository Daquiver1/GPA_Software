import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from logics.logic7 import Myself

class InputDialog7(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.showMyself()

	def showMyself(self):
		my_info = Myself()
		QMessageBox.about(self, "Title", my_info)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog7()
	exit(0)

