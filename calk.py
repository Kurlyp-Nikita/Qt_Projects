# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Калькулятор_Qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from math import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 430)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(0, 0, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(0, 0, 0);")
        self.result.setObjectName("result")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(0, 290, 150, 82))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_0.setObjectName("Button_0")
        self.equally = QtWidgets.QPushButton(self.centralwidget)
        self.equally.setGeometry(QtCore.QRect(150, 290, 81, 82))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.equally.setFont(font)
        self.equally.setStyleSheet("background-color: rgb(255, 88, 38);\n"
"")
        self.equally.setObjectName("equally")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(0, 210, 100, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        self.Button_1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(100, 210, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(200, 210, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_3.setFont(font)
        self.Button_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_3.setObjectName("Button_3")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(0, 130, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(100, 130, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(200, 130, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_6.setObjectName("Button_6")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(0, 50, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(100, 50, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(200, 50, 100, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Button_9.setObjectName("Button_9")
        self.Button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_plus.setGeometry(QtCore.QRect(300, 50, 50, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button_plus.setFont(font)
        self.Button_plus.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Button_plus.setObjectName("Button_plus")
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(300, 130, 50, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button_minus.setFont(font)
        self.Button_minus.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Button_minus.setObjectName("Button_minus")
        self.Button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.Button_multiply.setGeometry(QtCore.QRect(300, 210, 50, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button_multiply.setFont(font)
        self.Button_multiply.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Button_multiply.setObjectName("Button_multiply")
        self.Button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.Button_divide.setGeometry(QtCore.QRect(300, 290, 50, 82))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button_divide.setFont(font)
        self.Button_divide.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Button_divide.setObjectName("Button_divide")
        self.Button_degree = QtWidgets.QPushButton(self.centralwidget)
        self.Button_degree.setGeometry(QtCore.QRect(230, 290, 71, 82))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Button_degree.setFont(font)
        self.Button_degree.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Button_degree.setObjectName("Button_degree")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.result.setText(_translate("MainWindow", "0"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.equally.setText(_translate("MainWindow", "="))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_multiply.setText(_translate("MainWindow", "*"))
        self.Button_divide.setText(_translate("MainWindow", "/"))
        self.Button_degree.setText(_translate("MainWindow", "^"))

    def add_function(self):
        self.Button_0.clicked.connect(lambda: self.write_number(self.Button_0.text()))
        self.Button_1.clicked.connect(lambda: self.write_number(self.Button_1.text()))
        self.Button_2.clicked.connect(lambda: self.write_number(self.Button_2.text()))
        self.Button_3.clicked.connect(lambda: self.write_number(self.Button_3.text()))
        self.Button_4.clicked.connect(lambda: self.write_number(self.Button_4.text()))
        self.Button_5.clicked.connect(lambda: self.write_number(self.Button_5.text()))
        self.Button_6.clicked.connect(lambda: self.write_number(self.Button_6.text()))
        self.Button_7.clicked.connect(lambda: self.write_number(self.Button_7.text()))
        self.Button_8.clicked.connect(lambda: self.write_number(self.Button_8.text()))
        self.Button_9.clicked.connect(lambda: self.write_number(self.Button_9.text()))
        self.Button_plus.clicked.connect(lambda: self.write_number(self.Button_plus.text()))
        self.Button_minus.clicked.connect(lambda: self.write_number(self.Button_minus.text()))
        self.Button_multiply.clicked.connect(lambda: self.write_number(self.Button_multiply.text()))
        self.Button_divide.clicked.connect(lambda: self.write_number(self.Button_divide.text()))

        self.equally.clicked.connect(self.results)
        self.Button_degree.clicked.connect(self.result)


    def write_number(self, number):
        if self.result.text() == "0":
            self.result.setText(number)
        else:
            self.result.setText(self.result.text() + number)

    def results(self):
        res = eval(self.result.text())
        self.result.setText(str(res))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())