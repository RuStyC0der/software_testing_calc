from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5 import QtPrintSupport, QtWidgets
from PyQt5.QtGui import QTextDocument
import PyQt5.QtGui
from PyQt5.QtWidgets import *
import calc_model 

from PyQt5 import uic

class triangle(QMainWindow):
    def __init__(self):        
        super(triangle, self).__init__()
        self.ui =uic.loadUi("calc.ui", self)
        self.button_group =QButtonGroup()
        self.button_group.addButton(self.ui.radioButton)
        self.button_group.addButton(self.ui.radioButton_3)
        self.button_group.addButton(self.ui.radioButton_6)
        self.button_group.addButton(self.ui.radioButton_4)
        self.button_group.addButton(self.ui.radioButton_5)
        self.button_group.addButton(self.ui.radioButton_2)
        

        self.a = calc_model.Area_calc()
        

        self.button_group.buttonClicked.connect(self.radioB)
        self.ui.pushButton.clicked.connect(self.but)

    def but(self):
        
        

        if self.typeR == "1":
            a = int(self.ui.lineEdit.text())
            b = int(self.ui.lineEdit_2.text())
            c = int(self.ui.lineEdit_3.text())
            res = self.a.triangle.geron(a,b,c)
        elif self.typeR == "2":
            a = int(self.ui.lineEdit_4.text())
            b = int(self.ui.lineEdit_5.text())
            c = int(self.ui.lineEdit_6.text())
            res = self.a.triangle.two_side_one_angle(a,b,c)
        elif self.typeR == "3":
            a = int(self.ui.lineEdit_7.text())
            b = int(self.ui.lineEdit_8.text())
            res = self.a.triangle.side_height(a,b)
        elif self.typeR == "4":
            a = int(self.ui.lineEdit_9.text())
            b = int(self.ui.lineEdit_10.text())
            c = int(self.ui.lineEdit_11.text())
            d = int(self.ui.lineEdit_12.text())
            res = self.a.triangle.thre_side_described_circle(a,b,c,d)
        elif self.typeR == "5":
            a = int(self.ui.lineEdit_13.text())
            b = int(self.ui.lineEdit_14.text())
            c = int(self.ui.lineEdit_15.text())
            d = int(self.ui.lineEdit_16.text())
            res = self.a.triangle.tree_side_inscribed_circle(a,b,c,d)
        elif self.typeR == "6":
            a = int(self.ui.lineEdit_17.text())
            b = int(self.ui.lineEdit_18.text())
            c = int(self.ui.lineEdit_19.text())    
            res = self.a.triangle.one_side_two_angle(a,b,c)
            

        self.ui.label_3.setText(str(res))
        
        

        
        print(res)

    def radioB(self, button):
        
        self.typeR = button.text()[0]
        if self.typeR == "1":
            self.ui.stackedWidget.setCurrentIndex(1)
        elif self.typeR == "2":
            self.ui.stackedWidget.setCurrentIndex(2)
        elif self.typeR == "3":
            self.ui.stackedWidget.setCurrentIndex(3)
        elif self.typeR == "4":
            self.ui.stackedWidget.setCurrentIndex(4)
        elif self.typeR == "5":
            self.ui.stackedWidget.setCurrentIndex(5)
        elif self.typeR == "6":
            self.ui.stackedWidget.setCurrentIndex(6)
      

if __name__ == '__main__':
    app = QApplication([])

    w = triangle()
    w.show()

    app.exec()

#self.label.setText('Current: ' + button.text())
        
