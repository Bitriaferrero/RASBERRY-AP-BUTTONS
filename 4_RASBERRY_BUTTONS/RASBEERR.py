# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LED.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #self.pushButton_11.clicked.connect(self.Play_button_11_clicked)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("awus036neh-llave-de-wifi-usb-alfa-network-320-mw-y-5-dbi-antena.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("wifiap2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(160, 160))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 10, 301, 161))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("router-icon-transparent-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QtCore.QSize(160, 160))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 180, 311, 71))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("wifi5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 260, 311, 71))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 180, 301, 151))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ssh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 340, 311, 121))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(130, 120))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(False)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(330, 340, 301, 121))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 81 11pt \"Open Sans ExtraBold\";")
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QtCore.QSize(130, 120))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_11.clicked.connect(self.Play_button_11_clicked)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WIFI-HACK "))
        self.pushButton.setText(_translate("MainWindow", " WIFI AP"))
        self.pushButton_6.setText(_translate("MainWindow", "ROUTING WIFI"))
        self.pushButton_8.setText(_translate("MainWindow", "CONNECT &WIFI 1"))
        self.pushButton_10.setText(_translate("MainWindow", "CONNECT W&IFI 2"))
        self.pushButton_11.setText(_translate("MainWindow", "  S&ERVER SSH"))
        self.pushButton_12.setText(_translate("MainWindow", "ALPHA1 MACCHANGER"))
        self.pushButton_13.setText(_translate("MainWindow", "ALPHA2 MACCHANGER"))


# Eventos de botones 
    def Play_button_11_clicked(self):
        os.system("xterm -e 'bash -c \"sudo sh /etc/init.d/ssh start; exec bash\"'")
 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
