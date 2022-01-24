import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self, parent = None):
      super().__init__()
      #super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("PyQt5")

      self.btn1 = QPushButton()
      self.btn2 = QPushButton()
      self.btn3 = QPushButton()
      self.btn4 = QPushButton()
      self.btn5 = QPushButton()
      self.btn6 = QPushButton()
      self.btn7 = QPushButton()

      self.btn1.setText("What is GPA?")
      # Add connect
      self.btn2.setText("What is CGPA?")
      # Add connect
      self.btn3.setText("What is FGPA?")
      # Add connect
      self.btn4.setText("What are credit hours?")
      # Add connect
      self.btn5.setText("What are resits?")
      # Add connect
      self.btn6.setText("What are levels?")
      # Add connect
      self.btn7.setText("What is a good GPA?")
      # Add connect

      self.vbox = QVBoxLayout()
      self.vbox.addWidget(self.btn1)
      self.vbox.addWidget(self.btn2)
      self.vbox.addWidget(self.btn3)
      self.vbox.addWidget(self.btn4)
      self.vbox.addWidget(self.btn5)
      self.vbox.addWidget(self.btn6)
      self.vbox.addWidget(self.btn7)

      self.setLayout(self.vbox)

   def button1(self,s):
      pass

   def button2(self, s):
      pass 

   def button3(self, s):
      pass 

   def button4(self,s):
      pass 

   def button5(self, s):
      pass

   def button6(self, s):
      pass

   def button7(self, s):
      pass

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
