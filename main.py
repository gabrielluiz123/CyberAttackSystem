# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 120, 47, 13))
        self.label.setObjectName("label")
        self.inputIP = QtWidgets.QLineEdit(self.centralwidget)
        self.inputIP.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.inputIP.setObjectName("inputIP")
        self.ipBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ipBtn.setGeometry(QtCore.QRect(180, 170, 75, 23))
        self.ipBtn.setObjectName("ipBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 181, 20))
        self.label_2.setObjectName("label_2")
        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(100, 220, 221, 20))
        self.ipLabel.setText("")
        self.ipLabel.setObjectName("ipLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cyber Attack"))
        self.label.setText(_translate("MainWindow", "IP Alvo:"))
        self.ipBtn.setText(_translate("MainWindow", "Inserir"))
        self.label_2.setText(_translate("MainWindow", "Ambiente de ataque cibernético"))
