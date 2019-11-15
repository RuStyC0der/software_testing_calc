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

        self._quadrangle_button_group =QButtonGroup()
        self._quadrangle_button_group.addButton(self.ui.radioButton_7)
        self._quadrangle_button_group.addButton(self.ui.radioButton_8)

        self._square_button_group =QButtonGroup()
        self._square_button_group.addButton(self.ui.radioButton_21)
        self._square_button_group.addButton(self.ui.radioButton_22)

        self._rectangle_button_group =QButtonGroup()
        self._rectangle_button_group.addButton(self.ui.radioButton_9)

        self._paralelogram_button_group =QButtonGroup()
        self._paralelogram_button_group.addButton(self.ui.radioButton_11)
        self._paralelogram_button_group.addButton(self.ui.radioButton_12)
        self._paralelogram_button_group.addButton(self.ui.radioButton_23)      

        self._diamond_button_group =QButtonGroup()
        self._diamond_button_group.addButton(self.ui.radioButton_13)
        self._diamond_button_group.addButton(self.ui.radioButton_14)
        self._diamond_button_group.addButton(self.ui.radioButton_24)

        self._trapeze_button_group =QButtonGroup()
        self._trapeze_button_group.addButton(self.ui.radioButton_15)
        self._trapeze_button_group.addButton(self.ui.radioButton_16)
        self._trapeze_button_group.addButton(self.ui.radioButton_25)

        self._circle_button_group =QButtonGroup()
        self._circle_button_group.addButton(self.ui.radioButton_17)
        self._circle_button_group.addButton(self.ui.radioButton_18)
        self._circle_button_group.addButton(self.ui.radioButton_26)

        self._elipse_button_group =QButtonGroup()
        self._elipse_button_group.addButton(self.ui.radioButton_19)

        
       
        
        self._triangle_button_group.buttonClicked.connect(self.triangle_swich_menus)
        self.ui.pushButton_2.clicked.connect(self.calculate_triangle)

        self._quadrangle_button_group.buttonClicked.connect(self.quadrangle_swich_menus)
        self.ui.pushButton_4.clicked.connect(self.calculate_quadrangle)
      

        self._square_button_group.buttonClicked.connect(self.square_swich_menus)
        self.ui.pushButton_5.clicked.connect(self.calculate_square)
        
        self._rectangle_button_group.buttonClicked.connect(self.rectangle_swich_menus)
        self.ui.pushButton_6.clicked.connect(self.calculate_rectangle)
       
        self._paralelogram_button_group.buttonClicked.connect(self.paralelogram_swich_menus)
        self.ui.pushButton_7.clicked.connect(self.calculate_paralelogram)
       
        self._diamond_button_group.buttonClicked.connect(self.diamond_swich_menus)
        self.ui.pushButton_8.clicked.connect(self.calculate_diamond)
     
        self._trapeze_button_group.buttonClicked.connect(self.trapeze_swich_menus)
        self.ui.pushButton_9.clicked.connect(self.calculate_trapeze)
     
        self._circle_button_group.buttonClicked.connect(self.circle_swich_menus)
        self.ui.pushButton_10.clicked.connect(self.calculate_circle)

        self._elipse_button_group.buttonClicked.connect(self.elipse_swich_menus)
        self.ui.pushButton_11.clicked.connect(self.calculate_elipse)


     

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


        # I do not write this code manually :)
        self.ui.comboBox_12.addItem("cm", 1)
        self.ui.comboBox_12.addItem("m", 100)
        self.ui.comboBox_12.addItem("km", 100000)
      
        self.ui.comboBox_29.addItem("cm", 1)
        self.ui.comboBox_29.addItem("m", 100)
        self.ui.comboBox_29.addItem("km", 100000)
       
        self.ui.comboBox_30.addItem("cm", 1)
        self.ui.comboBox_30.addItem("m", 100)
        self.ui.comboBox_30.addItem("km", 100000)
        self.ui.comboBox.addItem("cm", 1)
        self.ui.comboBox.addItem("m", 100)
        self.ui.comboBox.addItem("km", 100000)
        self.ui.comboBox_39.addItem("cm", 1)
        self.ui.comboBox_39.addItem("m", 100)
        self.ui.comboBox_39.addItem("km", 100000)
        self.ui.comboBox_27.addItem("cm", 1)
        self.ui.comboBox_27.addItem("m", 100)
        self.ui.comboBox_27.addItem("km", 100000)
        self.ui.comboBox_10.addItem("cm", 1)
        self.ui.comboBox_10.addItem("m", 100)
        self.ui.comboBox_10.addItem("km", 100000)
        self.ui.comboBox_45.addItem("cm", 1)
        self.ui.comboBox_45.addItem("m", 100)
        self.ui.comboBox_45.addItem("km", 100000)
        self.ui.comboBox_31.addItem("cm", 1)
        self.ui.comboBox_31.addItem("m", 100)
        self.ui.comboBox_31.addItem("km", 100000)
        self.ui.comboBox_153.addItem("cm", 1)
        self.ui.comboBox_153.addItem("m", 100)
        self.ui.comboBox_153.addItem("km", 100000)
        self.ui.comboBox_18.addItem("cm", 1)
        self.ui.comboBox_18.addItem("m", 100)
        self.ui.comboBox_18.addItem("km", 100000)
        self.ui.comboBox_149.addItem("cm", 1)
        self.ui.comboBox_149.addItem("m", 100)
        self.ui.comboBox_149.addItem("km", 100000)
        self.ui.comboBox_38.addItem("cm", 1)
        self.ui.comboBox_38.addItem("m", 100)
        self.ui.comboBox_38.addItem("km", 100000)
        self.ui.comboBox_148.addItem("cm", 1)
        self.ui.comboBox_148.addItem("m", 100)
        self.ui.comboBox_148.addItem("km", 100000)
        self.ui.comboBox_151.addItem("cm", 1)
        self.ui.comboBox_151.addItem("m", 100)
        self.ui.comboBox_151.addItem("km", 100000)

        self.ui.comboBox_154.addItem("cm", 1)
        self.ui.comboBox_154.addItem("m", 100)
        self.ui.comboBox_154.addItem("km", 100000)

        
        self.ui.comboBox_33.addItem("cm", 1)
        self.ui.comboBox_33.addItem("m", 100)
        self.ui.comboBox_33.addItem("km", 100000)
        self.ui.comboBox_146.addItem("cm", 1)
        self.ui.comboBox_146.addItem("m", 100)
        self.ui.comboBox_146.addItem("km", 100000)
        self.ui.comboBox_6.addItem("cm", 1)
        self.ui.comboBox_6.addItem("m", 100)
        self.ui.comboBox_6.addItem("km", 100000)
        self.ui.comboBox_42.addItem("cm", 1)
        self.ui.comboBox_42.addItem("m", 100)
        self.ui.comboBox_42.addItem("km", 100000)
        self.ui.comboBox_152.addItem("cm", 1)
        self.ui.comboBox_152.addItem("m", 100)
        self.ui.comboBox_152.addItem("km", 100000)
        self.ui.comboBox_44.addItem("cm", 1)
        self.ui.comboBox_44.addItem("m", 100)
        self.ui.comboBox_44.addItem("km", 100000)
        self.ui.comboBox_46.addItem("cm", 1)
        self.ui.comboBox_46.addItem("m", 100)
        self.ui.comboBox_46.addItem("km", 100000)
        self.ui.comboBox_8.addItem("cm", 1)
        self.ui.comboBox_8.addItem("m", 100)
        self.ui.comboBox_8.addItem("km", 100000)
        self.ui.comboBox_28.addItem("cm", 1)
        self.ui.comboBox_28.addItem("m", 100)
        self.ui.comboBox_28.addItem("km", 100000)
        self.ui.comboBox_5.addItem("cm", 1)
        self.ui.comboBox_5.addItem("m", 100)
        self.ui.comboBox_5.addItem("km", 100000)
        self.ui.comboBox_35.addItem("cm", 1)
        self.ui.comboBox_35.addItem("m", 100)
        self.ui.comboBox_35.addItem("km", 100000)
        self.ui.comboBox_48.addItem("cm", 1)
        self.ui.comboBox_48.addItem("m", 100)
        self.ui.comboBox_48.addItem("km", 100000)
        self.ui.comboBox_9.addItem("cm", 1)
        self.ui.comboBox_9.addItem("m", 100)
        self.ui.comboBox_9.addItem("km", 100000)
        self.ui.comboBox_40.addItem("cm", 1)
        self.ui.comboBox_40.addItem("m", 100)
        self.ui.comboBox_40.addItem("km", 100000)
        self.ui.comboBox_147.addItem("cm", 1)
        self.ui.comboBox_147.addItem("m", 100)
        self.ui.comboBox_147.addItem("km", 100000)
        self.ui.comboBox_3.addItem("cm", 1)
        self.ui.comboBox_3.addItem("m", 100)
        self.ui.comboBox_3.addItem("km", 100000)
        self.ui.comboBox_2.addItem("cm", 1)
        self.ui.comboBox_2.addItem("m", 100)
        self.ui.comboBox_2.addItem("km", 100000)
        self.ui.comboBox_11.addItem("cm", 1)
        self.ui.comboBox_11.addItem("m", 100)
        self.ui.comboBox_11.addItem("km", 100000)
        self.ui.comboBox_4.addItem("cm", 1)
        self.ui.comboBox_4.addItem("m", 100)
        self.ui.comboBox_4.addItem("km", 100000)
        self.ui.comboBox_34.addItem("cm", 1)
        self.ui.comboBox_34.addItem("m", 100)
        self.ui.comboBox_34.addItem("km", 100000)
        self.ui.comboBox_15.addItem("cm", 1)
        self.ui.comboBox_15.addItem("m", 100)
        self.ui.comboBox_15.addItem("km", 100000)
        self.ui.comboBox_32.addItem("cm", 1)
        self.ui.comboBox_32.addItem("m", 100)
        self.ui.comboBox_32.addItem("km", 100000)
        self.ui.comboBox_17.addItem("cm", 1)
        self.ui.comboBox_17.addItem("m", 100)
        self.ui.comboBox_17.addItem("km", 100000)
        self.ui.comboBox_16.addItem("cm", 1)
        self.ui.comboBox_16.addItem("m", 100)
        self.ui.comboBox_16.addItem("km", 100000)
        self.ui.comboBox_150.addItem("cm", 1)
        self.ui.comboBox_150.addItem("m", 100)
        self.ui.comboBox_150.addItem("km", 100000)
        self.ui.comboBox_36.addItem("cm", 1)
        self.ui.comboBox_36.addItem("m", 100)
        self.ui.comboBox_36.addItem("km", 100000)
        self.ui.comboBox_49.addItem("cm", 1)
        self.ui.comboBox_49.addItem("m", 100)
        self.ui.comboBox_49.addItem("km", 100000)
        self.ui.comboBox_41.addItem("cm", 1)
        self.ui.comboBox_41.addItem("m", 100)
        self.ui.comboBox_41.addItem("km", 100000)
        self.ui.comboBox_14.addItem("cm", 1)
        self.ui.comboBox_14.addItem("m", 100)
        self.ui.comboBox_14.addItem("km", 100000)
        self.ui.comboBox_13.addItem("cm", 1)
        self.ui.comboBox_13.addItem("m", 100)
        self.ui.comboBox_13.addItem("km", 100000)
        self.ui.comboBox_37.addItem("cm", 1)
        self.ui.comboBox_37.addItem("m", 100)
        self.ui.comboBox_37.addItem("km", 100000)
        self.ui.comboBox_7.addItem("cm", 1)
        self.ui.comboBox_7.addItem("m", 100)
        self.ui.comboBox_7.addItem("km", 100000)



        self.model = calc_model.Area_calc()
        self.setWindowIcon(QtGui.QIcon('./media/window_icon.png'))
        self.movie = QtGui.QMovie("./media/firework.gif")
        self.ui.label_55.setMovie(self.movie)
        self.ui.label_28.setMovie(self.movie)
        self.ui.label_30.setMovie(self.movie)
        self.ui.label_49.setMovie(self.movie)
        self.ui.label_50.setMovie(self.movie)
        self.ui.label_51.setMovie(self.movie)
        self.ui.label_52.setMovie(self.movie)
        self.ui.label_53.setMovie(self.movie)
        self.ui.label_54.setMovie(self.movie)

        self.setFixedSize(self.size())
        self.ui.stackedWidget.setCurrentIndex(1)
        self.typeR = "1"
        self.ui.lineEdit_26.setReadOnly(True)

        # pixmap = QPixmap('./media/phigures/circle/довжина.jpg')
        # self.ui.label_3.setPixmap(pixmap)


    def calculate_triangle(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit.text().replace(",", ".")) * self.ui.comboBox.currentData()
                b = float(self.ui.lineEdit_2.text().replace(",", ".")) * self.ui.comboBox_2.currentData()
                c = float(self.ui.lineEdit_3.text().replace(",", ".")) * self.ui.comboBox_3.currentData()
                res = self.model.triangle.geron(a,b,c)
            elif self.typeR == "2":
                
                a = float(self.ui.lineEdit_23.text().replace(",", ".")) * self.ui.comboBox_4.currentData()
                print("sdsd")
                b = float(self.ui.lineEdit_22.text().replace(",", ".")) * self.ui.comboBox_5.currentData()
                c = float(self.ui.lineEdit_25.text().replace(",", ".")) 
                
                res = self.model.triangle.two_side_one_angle(a,b,c)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_5.text().replace(",", ".")) * self.ui.comboBox_6.currentData()
                b = float(self.ui.lineEdit_4.text().replace(",", ".")) * self.ui.comboBox_7.currentData()
                res = self.model.triangle.side_height(a,b)
            elif self.typeR == "4":
                a = float(self.ui.lineEdit_7.text().replace(",", ".")) * self.ui.comboBox_8.currentData()
                b = float(self.ui.lineEdit_6.text().replace(",", ".")) * self.ui.comboBox_9.currentData()
                c = float(self.ui.lineEdit_8.text().replace(",", ".")) * self.ui.comboBox_10.currentData()
                d = float(self.ui.lineEdit_24.text().replace(",", ".")) 
                res = self.model.triangle.thre_side_described_circle(a,b,c,d)
            elif self.typeR == "5":
                a = float(self.ui.lineEdit_10.text().replace(",", ".")) * self.ui.comboBox_11.currentData()
                b = float(self.ui.lineEdit_9.text().replace(",", ".")) * self.ui.comboBox_12.currentData()
                c = float(self.ui.lineEdit_11.text().replace(",", ".")) * self.ui.comboBox_13.currentData()
                d = float(self.ui.lineEdit_29.text().replace(",", ".")) 
                res = self.model.triangle.tree_side_inscribed_circle(a,b,c,d)
            elif self.typeR == "6":
                a = float(self.ui.lineEdit_13.text().replace(",", ".")) * self.ui.comboBox_14.currentData()
                b = float(self.ui.lineEdit_12.text().replace(",", ".")) 
                c = float(self.ui.lineEdit_14.text().replace(",", ".")) 
                res = self.model.triangle.one_side_two_angle(a,b,c)

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_26.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_quadrangle(self):
     
        try:
            if self.typeR == "2":
                
                a = float(self.ui.lineEdit_50.text().replace(",", ".")) * self.ui.comboBox_28.currentData()
                b = float(self.ui.lineEdit_49.text().replace(",", ".")) * self.ui.comboBox_27.currentData()
                c = float(self.ui.lineEdit_54.text().replace(",", ".")) * self.ui.comboBox_29.currentData()
                d = float(self.ui.lineEdit_55.text().replace(",", ".")) * self.ui.comboBox_30.currentData()
                f = float(self.ui.lineEdit_52.text().replace(",", "."))
                e = float(self.ui.lineEdit_51.text().replace(",", "."))
                res = self.model.quad.four_side_two_angle(a,b,c, d, e, f)
            elif self.typeR == "1":
                a = float(self.ui.lineEdit_46.text().replace(",", ".")) * self.ui.comboBox_18.currentData()
                b = float(self.ui.lineEdit_45.text().replace(",", ".")) * self.ui.comboBox_17.currentData()
                c = float(self.ui.lineEdit_53.text().replace(",", "."))             
                res = self.model.quad.two_diagonal_one_angle(a,b, c)
            

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_28.setText(str(res))
        self.movie.start()
        

    def calculate_square(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit_63.text().replace(",", ".")) * self.ui.comboBox_36.currentData()
              
                res = self.model.squad.one_side(a)
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_64.text().replace(",", ".")) * self.ui.comboBox_37.currentData()
              
                res = self.model.squad.one_diagonal(a)
            

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_30.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_rectangle(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit_60.text().replace(",", ".")) * self.ui.comboBox_34.currentData()
                b = float(self.ui.lineEdit_59.text().replace(",", ".")) * self.ui.comboBox_33.currentData()
               
                res = self.model.rectangle.two_side(a,b)
           

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_31.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_paralelogram(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit_67.text().replace(",", ".")) * self.ui.comboBox_38.currentData()
                b = float(self.ui.lineEdit_62.text().replace(",", ".")) * self.ui.comboBox_35.currentData()
                c = float(self.ui.lineEdit_65.text().replace(",", "."))
                res = self.model.parallelogram.two_side_one_angle(a, b, c)
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_91.text().replace(",", ".")) * self.ui.comboBox_49.currentData()
                b = float(self.ui.lineEdit_90.text().replace(",", ".")) * self.ui.comboBox_48.currentData()
            
                res = self.model.parallelogram.base_height(a, b)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_33.text().replace(",", ".")) * self.ui.comboBox_15.currentData()
                b = float(self.ui.lineEdit_32.text().replace(",", ".")) * self.ui.comboBox_16.currentData()
                c = float(self.ui.lineEdit_34.text().replace(",", ".")) 
                
                res = self.model.parallelogram.two_diagonal_one_angle(a, b, c)
            

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_35.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_diamond(self):
        try:
            if self.typeR == "1":               
                a = float(self.ui.lineEdit_71.text().replace(",", ".")) * self.ui.comboBox_40.currentData()
                b = float(self.ui.lineEdit_72.text().replace(",", "."))
                res = self.model.diamond.one_side_one_angle(a, b)
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_74.text().replace(",", ".")) * self.ui.comboBox_41.currentData()
                b = float(self.ui.lineEdit_75.text().replace(",", ".")) 
            
                res = self.model.diamond.one_side_height(a, b)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_79.text().replace(",", ".")) * self.ui.comboBox_42.currentData()
                b = float(self.ui.lineEdit_80.text().replace(",", ".")) * self.ui.comboBox_42.currentData()
                res = self.model.diamond.two_diagonal(a, b)           

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_36.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_trapeze(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit_274.text().replace(",", ".")) * self.ui.comboBox_148.currentData()
                b = float(self.ui.lineEdit_273.text().replace(",", ".")) * self.ui.comboBox_149.currentData()
                c = float(self.ui.lineEdit_273.text().replace(",", ".")) * self.ui.comboBox_154.currentData()
                res = self.model.trapeze.two_base_one_height(a, b, c) 
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_277.text().replace(",", ".")) * self.ui.comboBox_150.currentData()
                b = float(self.ui.lineEdit_276.text().replace(",", ".")) * self.ui.comboBox_151.currentData()
               
                res = self.model.trapeze.one_height_middle_line(a, b)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_280.text().replace(",", ".")) * self.ui.comboBox_153.currentData()
                b = float(self.ui.lineEdit_279.text().replace(",", ".")) * self.ui.comboBox_152.currentData()

                c = float(self.ui.lineEdit_281.text().replace(",", ".")) 
                res = self.model.trapeze.two_diagonal_one_angle(a, b, c)
           

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_37.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_circle(self):
        try:
            if self.typeR == "1":
                print(self.ui.lineEdit_84.text().replace(",", "."))
                a = float(self.ui.lineEdit_84.text().replace(",", ".")) * self.ui.comboBox_45.currentData()
             
                res = self.model.circle.one_radius(a)
            elif self.typeR == "2":
                a = float(self.ui.lineEdit_85.text().replace(",", ".")) * self.ui.comboBox_46.currentData()
            
                res = self.model.circle.one_diameter(a)
            elif self.typeR == "3":
                a = float(self.ui.lineEdit_83.text().replace(",", ".")) * self.ui.comboBox_44.currentData()
                res = self.model.circle.one_length(a)
            

        except ValueError as d:
            print("error", d)
            return

        self.ui.lineEdit_38.setText(str(res))
        self.movie.start()
        print(res)

    def calculate_elipse(self):
        try:
            if self.typeR == "1":
                a = float(self.ui.lineEdit_57.text().replace(",", ".")) * self.ui.comboBox_32.currentData()
                b = float(self.ui.lineEdit_56.text().replace(",", ".")) * self.ui.comboBox_31.currentData()
 
                res = self.model.ellipse.two_half_shaft(a, b)
            

        except ValueError:
            print("error")
            return

        self.ui.lineEdit_39.setText(str(res))
        self.movie.start()
        print(res)




    def triangle_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1":1, "2":0, "3":2, "4":3, "5":4, "6":5}
        path_dict = {"1":"./media/phigures/triangle/Герон.jpg",
                     "2":"./media/phigures/triangle/довжини двох сторін і кут між ними.png",
                     "3":"./media/phigures/triangle/довжина сторони  і опущена висота.png",
                     "4":"./media/phigures/triangle/довжина трьох сторін  і радіус вписаного кола.png",
                     "5":"./media/phigures/triangle/довжина трьох сторін  і радіус описаного кола.png",
                     "6":"./media/phigures/triangle/довжина одного боку  і двох кутыв.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_3.setPixmap(pixmap)

    def quadrangle_swich_menus(self, button):
        self.movie.stop()
        
        matchicg_dict = {"1":0, "2":1}
        path_dict = {"1":"./media/phigures/quadrangle/1.png",
                     "2":"./media/phigures/quadrangle/2.png"}
        self.typeR = button.text()[0]
        
        self.ui.stackedWidget_3.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_4.setPixmap(pixmap)

    def square_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1":0, "2":1}
        path_dict = {"1":"./media/phigures/square/Сторона.png",
                     "2":"./media/phigures/square/дыагональ.png"}                     
        self.typeR = button.text()[0]
        self.ui.stackedWidget_6.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_21.setPixmap(pixmap)

    def rectangle_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1":0}
        path_dict = {"1":"./media/phigures/rectangle/Сторона.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_5.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_22.setPixmap(pixmap)

    def paralelogram_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1":10, "2":1, "3":2}
        path_dict = {"1":"./media/phigures/paralelogram/дві сторони та кут між ними.png",
                     "2":"./media/phigures/paralelogram/одна сторона та висота.png",
                     "3":"./media/phigures/paralelogram/дыагоналы та кут.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_7.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_23.setPixmap(pixmap)

    def diamond_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1": 0, "2": 1, "3": 2}
        path_dict = {"1": "./media/phigures/diamond/сторона і кут.png",
                     "2": "./media/phigures/diamond/сторона івисота.png",
                     "3": "./media/phigures/diamond/діагональ.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_8.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_24.setPixmap(pixmap)

    def trapeze_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1": 0, "2": 1, "3": 2}
        path_dict = {"1": "./media/phigures/trapeze/основа і висота.jpg",
                     "2": "./media/phigures/trapeze/сер лін і висота.jpg",
                     "3": "./media/phigures/trapeze/діа кут.jpg"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_37.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_25.setPixmap(pixmap)

    def circle_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1": 2, "2": 1, "3": 0}
        path_dict = {"1": "./media/phigures/circle/радіус.jpg",
                     "2": "./media/phigures/circle/діаметр.jpg",
                     "3": "./media/phigures/circle/довжина.jpg"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_10.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_26.setPixmap(pixmap)

    def elipse_swich_menus(self, button):
        self.movie.stop()
        matchicg_dict = {"1": 0}
        path_dict = {"1": "./media/phigures/elips/ovals.png"}
        self.typeR = button.text()[0]
        self.ui.stackedWidget_4.setCurrentIndex(matchicg_dict[self.typeR])
        pixmap = QPixmap(path_dict[self.typeR])
        self.ui.label_27.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication([])

    w = triangle()
    w.show()

    app.exec()
