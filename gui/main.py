import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from grades_needed import InputDialog2
from gpa_calc import InputDialog4
from contact import InputDialog6

class window(QWidget):
   def __init__(self, parent = None):
      super().__init__()
      #super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("PyQt5")

      self.l1 = QLabel()
      self.l2 = QLabel()
      self.btn1 = QPushButton()
      self.btn2 = QPushButton()
      self.btn3 = QPushButton()
      self.btn4 = QPushButton()
      self.btn5 = QPushButton()
      self.btn6 = QPushButton()

      self.l1.setText("Hey, Welcome To Daquiver's GPA Self Care")
      self.l2.setText("Below are the features we support")
      self.btn1.setText("LEVEL PREDICTOR")
      # Add connect
      self.btn2.setText("GRADES YOU NEED IN ORDER TO ATTAIN A LEVEL")
      self.btn2.clicked.connect(self.button2)
      self.btn3.setText("HIGHEST CGPA YOU CAN ATTAIN IN A SEM")
      # Add connect
      self.btn4.setText("GPA CALCULATOR")
      self.btn4.clicked.connect(self.button4)
      self.btn5.setText("FAQS")
      # Add connect
      self.btn6.setText("CONTACT")
      self.btn6.clicked.connect(self.button6)

      self.l1.setAlignment(Qt.AlignCenter)
      self.l2.setAlignment(Qt.AlignCenter)

      self.vbox = QVBoxLayout()
      self.vbox.addWidget(self.l1)
      self.vbox.addWidget(self.l2)
      self.vbox.addStretch()
      self.vbox.addWidget(self.btn1)
      self.vbox.addWidget(self.btn2)
      self.vbox.addWidget(self.btn3)
      self.vbox.addWidget(self.btn4)
      self.vbox.addWidget(self.btn5)
      self.vbox.addWidget(self.btn6)

      self.setLayout(self.vbox)

   def button2(self, s):
      dlg = InputDialog2()

   def button4(self,s):
      dlg = InputDialog4()

   def button6(self, s):
      dlg = InputDialog6()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
