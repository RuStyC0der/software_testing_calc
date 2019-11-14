from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

from PyQt5.QtGui import QRegExpValidator, QPixmap
from PyQt5.QtCore import QRegExp

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

        self._triangle_button_group.buttonClicked.connect(self.triangle_swich_menus)
        self.ui.pushButton_2.clicked.connect(self.calculate_triangle)

        self.validator = QRegExpValidator(QRegExp(r"\d+[\.,]?\d*"))

        #  validate for all line. I do not write this code manually :)
        self.ui.lineEdit_50.setValidator(self.validator)
        self.ui.lineEdit.setValidator(self.validator)
        self.ui.lineEdit_45.setValidator(self.validator)
        self.ui.lineEdit_5.setValidator(self.validator)
        self.ui.lineEdit_46.setValidator(self.validator)
        self.ui.lineEdit_77.setValidator(self.validator)
        self.ui.lineEdit_29.setValidator(self.validator)
        self.ui.lineEdit_39.setValidator(self.validator)
        self.ui.lineEdit_83.setValidator(self.validator)
        self.ui.lineEdit_51.setValidator(self.validator)
        self.ui.lineEdit_71.setValidator(self.validator)
        self.ui.lineEdit_56.setValidator(self.validator)
        self.ui.lineEdit_12.setValidator(self.validator)
        self.ui.lineEdit_52.setValidator(self.validator)
        self.ui.lineEdit_28.setValidator(self.validator)
        self.ui.lineEdit_90.setValidator(self.validator)
        self.ui.lineEdit_30.setValidator(self.validator)
        self.ui.lineEdit_9.setValidator(self.validator)
        self.ui.lineEdit_85.setValidator(self.validator)
        self.ui.lineEdit_32.setValidator(self.validator)
        self.ui.lineEdit_24.setValidator(self.validator)
        self.ui.lineEdit_26.setValidator(self.validator)
        self.ui.lineEdit_11.setValidator(self.validator)
        self.ui.lineEdit_25.setValidator(self.validator)
        self.ui.lineEdit_36.setValidator(self.validator)
        self.ui.lineEdit_64.setValidator(self.validator)
        self.ui.lineEdit_280.setValidator(self.validator)
        self.ui.lineEdit_35.setValidator(self.validator)
        self.ui.lineEdit_273.setValidator(self.validator)
        self.ui.lineEdit_274.setValidator(self.validator)
        self.ui.lineEdit_13.setValidator(self.validator)
        self.ui.lineEdit_34.setValidator(self.validator)
        self.ui.lineEdit_14.setValidator(self.validator)
        self.ui.lineEdit_23.setValidator(self.validator)
        self.ui.lineEdit_31.setValidator(self.validator)
        self.ui.lineEdit_270.setValidator(self.validator)
        self.ui.lineEdit_271.setValidator(self.validator)
        self.ui.lineEdit_7.setValidator(self.validator)
        self.ui.lineEdit_277.setValidator(self.validator)
        self.ui.lineEdit_37.setValidator(self.validator)
        self.ui.lineEdit_27.setValidator(self.validator)
        self.ui.lineEdit_10.setValidator(self.validator)
        self.ui.lineEdit_63.setValidator(self.validator)
        self.ui.lineEdit_60.setValidator(self.validator)
        self.ui.lineEdit_79.setValidator(self.validator)
        self.ui.lineEdit_279.setValidator(self.validator)
        self.ui.lineEdit_84.setValidator(self.validator)
        self.ui.lineEdit_38.setValidator(self.validator)
        self.ui.lineEdit_3.setValidator(self.validator)
        self.ui.lineEdit_49.setValidator(self.validator)
        self.ui.lineEdit_62.setValidator(self.validator)
        self.ui.lineEdit_6.setValidator(self.validator)
        self.ui.lineEdit_4.setValidator(self.validator)
        self.ui.lineEdit_59.setValidator(self.validator)
        self.ui.lineEdit_8.setValidator(self.validator)
        self.ui.lineEdit_67.setValidator(self.validator)
        self.ui.lineEdit_2.setValidator(self.validator)
        self.ui.lineEdit_74.setValidator(self.validator)
        self.ui.lineEdit_70.setValidator(self.validator)
        self.ui.lineEdit_276.setValidator(self.validator)
        self.ui.lineEdit_22.setValidator(self.validator)
        self.ui.lineEdit_33.setValidator(self.validator)
        self.ui.lineEdit_91.setValidator(self.validator)
        self.ui.lineEdit_272.setValidator(self.validator)
        self.ui.lineEdit_57.setValidator(self.validator)


        self.model = calc_model.Area_calc()
        self.setWindowIcon(QtGui.QIcon('./media/window_icon.png'))

        self.setFixedSize(self.size())
        self.ui.stackedWidget.setCurrentIndex(1)
        self.typeR = "1"
        self.ui.lineEdit_26.setReadOnly(True)

        # pixmap = QPixmap('./media/phigures/circle/довжина.jpg')
        # self.ui.label_3.setPixmap(pixmap)


    def calculate_triangle(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit.text().replace(",", "."))
                b = float(self.ui.lineEdit_2.text().replace(",", "."))
                c = float(self.ui.lineEdit_3.text().replace(",", "."))
                res = self.model.triangle.geron(a,b,c)
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_4.text().replace(",", "."))
                b = float(self.ui.lineEdit_5.text().replace(",", "."))
                c = float(self.ui.lineEdit_6.text().replace(",", "."))
                res = self.model.triangle.two_side_one_angle(a,b,c)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_7.text().replace(",", "."))
                b = float(self.ui.lineEdit_8.text().replace(",", "."))
                res = self.model.triangle.side_height(a,b)
            elif self.typeR == "4":
                a = float(self.ui.lineEdit_9.text().replace(",", "."))
                b = float(self.ui.lineEdit_10.text().replace(",", "."))
                c = float(self.ui.lineEdit_11.text().replace(",", "."))
                d = float(self.ui.lineEdit_12.text().replace(",", "."))
                res = self.model.triangle.thre_side_described_circle(a,b,c,d)
            elif self.typeR == "5":
                a = float(self.ui.lineEdit_13.text().replace(",", "."))
                b = float(self.ui.lineEdit_14.text().replace(",", "."))
                c = float(self.ui.lineEdit_15.text().replace(",", "."))
                d = float(self.ui.lineEdit_16.text().replace(",", "."))
                res = self.model.triangle.tree_side_inscribed_circle(a,b,c,d)
            elif self.typeR == "6":
                a = float(self.ui.lineEdit_17.text().replace(",", "."))
                b = float(self.ui.lineEdit_18.text().replace(",", "."))
                c = float(self.ui.lineEdit_19.text().replace(",", "."))
                res = self.model.triangle.one_side_two_angle(a,b,c)
        except ValueError:
            print("error")
            return

        self.ui.lineEdit_26.setText(str(res))
        print(res)

    def triangle_swich_menus(self, button):
        matchicg_dict = {"1":1, "2":0, "3":2, "4":3, "5":4, "6":5}
        path_dict = {"1":"./media/phigures/triangle/Герон.jpg", "2":"./media/phigures/triangle/довжини двох сторін і кут між ними.png", "3":"./media/phigures/triangle/довжина сторони  і опущена висота.png", "4":"./media/phigures/triangle/довжина трьох сторін  і радіус вписаного кола.png", "5":"./media/phigures/triangle/довжина трьох сторін  і радіус описаного кола.png", "6":"./media/phigures/triangle/довжина одного боку  і двох кутыв.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_3.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])

    w = triangle()
    w.show()

    app.exec()
