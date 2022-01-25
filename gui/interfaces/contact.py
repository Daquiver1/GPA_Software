import sys
sys.path.insert(0, "C:\\Users\\Anita Agyepong\\Documents\\Daquiver's Quivers\\Python\\GPA_Software\\gui\\logics")
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from logic7 import Myself

class InputDialog7(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.showMyself()

	def showMyself(self):
		""" A function that returns a message box displaying a short intro of me. """
		my_info = Myself()
		QMessageBox.about(self, "Title", my_info)

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	dialog = InputDialog7()
	exit(0)

