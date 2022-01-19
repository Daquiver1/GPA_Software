import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   win = QWidget()

   l1 = QLabel()
   l2 = QLabel()
   btn1 = QPushButton(win)
   btn2 = QPushButton(win)
   btn3 = QPushButton(win)
   btn4 = QPushButton(win)
   btn5 = QPushButton(win)


   l1.setText("Hey, Welcome To Daquiver's GPA Predictor")
   l2.setText("Below are the features we support")
   btn1.setText("LEVEL PREDICTOR")
   btn2.setText("GRADES YOU NEED IN ORDER TO ATTAIN A LEVEL")
   btn3.setText("GPA CALCULATOR")
   btn4.setText("FAQS")
   btn5.setText("CONTACT")

   l1.setAlignment(Qt.AlignCenter)
   l2.setAlignment(Qt.AlignCenter)

   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   vbox.addWidget(l2)
   vbox.addStretch()
   vbox.addWidget(btn1)
   vbox.addWidget(btn2)
   vbox.addWidget(btn3)
   vbox.addWidget(btn4)
   vbox.addWidget(btn5)

   win.setLayout(vbox)

   btn1.clicked.connect(showdialog)

   win.setWindowTitle("GPA 101")
   win.show()
   sys.exit(app.exec_())

def showdialog():
   dlg = QDialog()
   b1 = QPushButton("ok",dlg)
   b1.move(50,50)
   dlg.setWindowTitle("Dialog") 
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()

if __name__ == '__main__':
   window()