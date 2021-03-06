from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QInputDialog, QApplication
from PyQt5.QtCore import Qt
from interfaces.grades_needed import InputDialog2
from interfaces.max_cgpa import InputDialog3
from interfaces.min_cgpa import InputDialog4
from interfaces.gpa_calc import InputDialog5
from interfaces.fgpa_calc import InputDialog6
from interfaces.faqs import InputDialog7
from interfaces.contact import InputDialog8
import sys

class window(QWidget):
   def __init__(self, parent = None):
      super().__init__()
      #super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("PyQt5")

      self.l1 = QLabel()
      self.l2 = QLabel()
      self.l3 = QLabel()
      self.btn1 = QPushButton()
      self.btn2 = QPushButton()
      self.btn3 = QPushButton()
      self.btn4 = QPushButton()
      self.btn5 = QPushButton()
      self.btn6 = QPushButton()
      self.btn7 = QPushButton()
      self.btn8 = QPushButton()

      self.l1.setText("Hey, Welcome To Daquiver's GPA Self Care")
      self.l2.setText("Below are the features we support")
      self.l3.setText("If this is your first time, go through the FAQS before you begin")
      self.btn1.setText("LEVEL PREDICTOR(NOT IMPLEMENTED")   
      # Add connect
      self.btn2.setText("GRADES YOU NEED IN ORDER TO REACH A SPECIFIC CGPA")
      self.btn2.clicked.connect(self.button2)
      self.btn3.setText("HIGHEST CGPA YOU CAN ATTAIN IN A SEM")
      self.btn3.clicked.connect(self.button3)
      self.btn4.setText("LOWEST CGPA YOU CAN ATTAIN IN A SEM")
      self.btn4.clicked.connect(self.button4)
      self.btn5.setText("GPA AND CGPA CALCULATOR")
      self.btn5.clicked.connect(self.button5)
      self.btn6.setText("FGPA CALCULATOR")
      self.btn6.clicked.connect(self.button6)
      self.btn7.setText("FAQS")
      self.btn7.clicked.connect(self.button7)
      self.btn8.setText("CONTACT")
      self.btn8.clicked.connect(self.button8)

      self.l1.setAlignment(Qt.AlignCenter)
      self.l2.setAlignment(Qt.AlignCenter)
      self.l3.setAlignment(Qt.AlignCenter)

      self.vbox = QVBoxLayout()
      self.vbox.addWidget(self.l1)
      self.vbox.addWidget(self.l2)
      self.vbox.addWidget(self.l3)
      self.vbox.addStretch()
      self.vbox.addWidget(self.btn1)
      self.vbox.addWidget(self.btn2)
      self.vbox.addWidget(self.btn3)
      self.vbox.addWidget(self.btn4)
      self.vbox.addWidget(self.btn5)
      self.vbox.addWidget(self.btn6)
      self.vbox.addWidget(self.btn7)
      self.vbox.addWidget(self.btn8)

      self.setLayout(self.vbox)

   def button2(self, s):
      """ A function to connect btn2 with it's interface. """
      dlg = InputDialog2()

   def button3(self, s):
      """ A function to connect btn3 with it's interface. """
      dlg = InputDialog3()

   def button4(self, s):
      """ A function to connect btn4 with it's interface. """
      dlg = InputDialog4()

   def button5(self,s):
      """ A function to connect btn5 with it's interface. """
      dlg = InputDialog5()

   def button6(self, s):
      """ A function to connect btn6 with it's interface. """
      dlg = InputDialog6()

   def button7(self, s):
      """ A function to connect btn7 with it's interface. """
      self.dlg = InputDialog7()           # When the method is left, the window will be destroyed. So I stored it by adding self.
      self.dlg.show()

   def button8(self, s):
      """ A function to connect btn8 with it's interface. """
      dlg = InputDialog8()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
