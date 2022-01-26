import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QApplication
sys.path.insert(0, "C:\\Users\\Anita Agyepong\\Documents\\Daquiver's Quivers\\Python\\GPA_Software\\gui\\logics")
from logic7 import * 

class InputDialog7(QWidget):
   def __init__(self, parent = None):
      super().__init__()
      self.resize(200,50)

      self.btn1 = QPushButton()
      self.btn2 = QPushButton()
      self.btn3 = QPushButton()
      self.btn4 = QPushButton()
      self.btn5 = QPushButton()
      self.btn6 = QPushButton()
      self.btn7 = QPushButton()

      self.btn1.setText("What is GPA?")
      self.btn1.clicked.connect(self.button1)
      self.btn2.setText("What is CGPA?")
      self.btn2.clicked.connect(self.button2)
      self.btn3.setText("What is FGPA?")
      self.btn3.clicked.connect(self.button3)
      self.btn4.setText("What are credit hours?")
      self.btn4.clicked.connect(self.button4)
      self.btn5.setText("What are resits?")
      self.btn5.clicked.connect(self.button5)
      self.btn6.setText("What are levels?")
      self.btn6.clicked.connect(self.button6)
      self.btn7.setText("What is a good GPA?")
      self.btn7.clicked.connect(self.button7)

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
      """ A function to display GPA info. """
      gpa_info = gpa()
      QMessageBox.about(self, "Title", gpa_info)

   def button2(self, s):
      """ A function to display CGPA info. """
      cgpa_info = cgpa()
      QMessageBox.about(self, "Title", cgpa_info) 

   def button3(self, s):
      """ A function to display FGPA info. """
      fgpa_info = fgpa()
      QMessageBox.about(self, "Title", fgpa_info) 

   def button4(self,s):
      """ A function to display credit hours info. """
      chours_info = credit_hours()
      QMessageBox.about(self, "Title", chours_info) 

   def button5(self, s):
      """ A function to display resits info. """
      resit_info = resits()
      QMessageBox.about(self, "Title", resit_info)

   def button6(self, s):
      """ A function to display degree classification info. """
      levels_info = levels()
      QMessageBox.about(self, "Ttile", levels_info)

   def button7(self, s):
      """ A function to display what a good gpa is. """
      good_gpa_info = good_gpa()
      QMessageBox.about(self, "Title", good_gpa_info)

if __name__ == '__main__':
   import sys
   app = QApplication(sys.argv)
   ex = InputDialog7()
   ex.show()
   sys.exit(app.exec_())
