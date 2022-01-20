import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# class App(QWidget):

#    def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 input dialogs - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
    
#    def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
        
#         self.yaw = self.getCourses()
#         for i in range(self.yaw):
#            self.getGrade()
#            self.getCredit()
           
#         self.show()
        
#    def getCourses(self):
#       i, okPressed = QInputDialog.getInt(self, "Courses","Number of Courses:", 4, 0, 100, 1)
#       return i

#    def getGrade(self):
#       text, okPressed = QInputDialog.getText(self, "Get text","Enter Grade:", QLineEdit.Normal, "")
#       return text

#    def getCredit(self):
#       i, okPressed = QInputDialog.getInt(self, "Credit Hours","Enter Credit Hours:", 2, 0, 100, 1)
#       return i 


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Enter your grade: ", self.first)
        layout.addRow("Enter the grade's credit hour: ", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return (self.first.text(), self.second.text())

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = InputDialog()
    if dialog.exec():
        print(dialog.getInputs())
    exit(0)