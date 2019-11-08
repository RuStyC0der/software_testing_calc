from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

import calc_model


class triangle(QMainWindow):
    def __init__(self):        
        super(triangle, self).__init__()
        self.ui = uic.loadUi("calc.ui", self)
        self._triangle_button_group =QButtonGroup()
        self._triangle_button_group.addButton(self.ui.radioButton)
        self._triangle_button_group.addButton(self.ui.radioButton_2)
        self._triangle_button_group.addButton(self.ui.radioButton_3)
        self._triangle_button_group.addButton(self.ui.radioButton_4)
        self._triangle_button_group.addButton(self.ui.radioButton_5)
        self._triangle_button_group.addButton(self.ui.radioButton_6)

        self.model = calc_model.Area_calc()

        self.setFixedSize(self.size())
        self.ui.stackedWidget.setCurrentIndex(1)
        self.setWindowIcon(QtGui.QIcon('./media/window_icon.png'))

        self._triangle_button_group.buttonClicked.connect(self.triangle_swich_menus)
        self.ui.pushButton.clicked.connect(self.but)

    def but(self):
        if self.typeR == "1":
            a = int(self.ui.lineEdit.text())
            b = int(self.ui.lineEdit_2.text())
            c = int(self.ui.lineEdit_3.text())
            res = self.model.triangle.geron(a,b,c)
        elif self.typeR == "2":
            a = int(self.ui.lineEdit_4.text())
            b = int(self.ui.lineEdit_5.text())
            c = int(self.ui.lineEdit_6.text())
            res = self.model.triangle.two_side_one_angle(a,b,c)
        elif self.typeR == "3":
            a = int(self.ui.lineEdit_7.text())
            b = int(self.ui.lineEdit_8.text())
            res = self.model.triangle.side_height(a,b)
        elif self.typeR == "4":
            a = int(self.ui.lineEdit_9.text())
            b = int(self.ui.lineEdit_10.text())
            c = int(self.ui.lineEdit_11.text())
            d = int(self.ui.lineEdit_12.text())
            res = self.model.triangle.thre_side_described_circle(a,b,c,d)
        elif self.typeR == "5":
            a = int(self.ui.lineEdit_13.text())
            b = int(self.ui.lineEdit_14.text())
            c = int(self.ui.lineEdit_15.text())
            d = int(self.ui.lineEdit_16.text())
            res = self.model.triangle.tree_side_inscribed_circle(a,b,c,d)
        elif self.typeR == "6":
            a = int(self.ui.lineEdit_17.text())
            b = int(self.ui.lineEdit_18.text())
            c = int(self.ui.lineEdit_19.text())    
            res = self.model.triangle.one_side_two_angle(a,b,c)

        self.ui.label_3.setText(str(res))
        print(res)

    def triangle_swich_menus(self, button):
        matchicg_dict = {"1":1, "2":0, "3":2, "4":3, "5":4, "6":5}
        self.ui.stackedWidget.setCurrentIndex(matchicg_dict[button.text()[0]])


if __name__ == '__main__':
    app = QApplication([])

    w = triangle()
    w.show()

    app.exec()