import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gpa_calc import InputDialog

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

      self.l1.setText("Hey, Welcome To Daquiver's GPA Predictor")
      self.l2.setText("Below are the features we support")
      self.btn1.setText("LEVEL PREDICTOR")
      self.btn2.setText("GRADES YOU NEED IN ORDER TO ATTAIN A LEVEL")
      self.btn3.setText("GPA CALCULATOR")
      self.btn3.clicked.connect(self.button23)
      self.btn4.setText("FAQS")
      self.btn5.setText("CONTACT")

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

      self.setLayout(self.vbox)

   def button23(self,s):
      dlg = InputDialog()

def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()


# def main(self):
#    yaw = InputDialog.random(self)
#    print(yaw)
   # app = QApplication(sys.argv)
   # win = QWidget()

   # l1 = QLabel()
   # l2 = QLabel()
   # btn1 = QPushButton(win)
   # btn2 = QPushButton(win)
   # btn3 = QPushButton(win)
   # btn4 = QPushButton(win)
   # btn5 = QPushButton(win)


   # l1.setText("Hey, Welcome To Daquiver's GPA Predictor")
   # l2.setText("Below are the features we support")
   # btn1.setText("LEVEL PREDICTOR")
   # btn2.setText("GRADES YOU NEED IN ORDER TO ATTAIN A LEVEL")
   # btn3.setText("GPA CALCULATOR")
   # btn3.clicked.connect(InputDialog)
   # btn4.setText("FAQS")
   # btn5.setText("CONTACT")

   # l1.setAlignment(Qt.AlignCenter)
   # l2.setAlignment(Qt.AlignCenter)

   # vbox = QVBoxLayout()
   # vbox.addWidget(l1)
   # vbox.addWidget(l2)
   # vbox.addStretch()
   # vbox.addWidget(btn1)
   # vbox.addWidget(btn2)
   # vbox.addWidget(btn3)
   # vbox.addWidget(btn4)
   # vbox.addWidget(btn5)

   # win.setLayout(vbox)


   # win.setWindowTitle("GPA 101")
   # win.show()
   # sys.exit(app.exec_())

# if __name__ == '__main__':
#    main()