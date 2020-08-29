# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_central(object):
    def setupUi(self, central):
        central.setObjectName("central")
        central.resize(920, 604)
        self.centralwidget = QtWidgets.QWidget(central)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_menu.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"border: none;\n"
"color: rgb(210, 210, 210);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_monitor = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_monitor.sizePolicy().hasHeightForWidth())
        self.btn_monitor.setSizePolicy(sizePolicy)
        self.btn_monitor.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_monitor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btn_monitor.setFont(font)
        self.btn_monitor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_monitor.setStyleSheet("QPushButton {    \n"
"    background-image:  url(:/icons/icons/cil-monitor.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 19px solid rgb(27, 29, 35);\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 55px;\n"
"    color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-left: 19px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"    border-left: 19px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:checked {\n"
"    border-right: 5px solid rgb(85, 170, 255);\n"
"}")
        self.btn_monitor.setCheckable(True)
        self.btn_monitor.setObjectName("btn_monitor")
        self.verticalLayout.addWidget(self.btn_monitor)
        self.btn_grafico = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grafico.sizePolicy().hasHeightForWidth())
        self.btn_grafico.setSizePolicy(sizePolicy)
        self.btn_grafico.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_grafico.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btn_grafico.setFont(font)
        self.btn_grafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_grafico.setStyleSheet("QPushButton {    \n"
"    background-image: url(:/icons/icons/cil-chart-line.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 19px solid rgb(27, 29, 35);\n"
"    background-color: rgb(27, 29, 35);\n"
"    text-align: left;\n"
"    padding-left: 55px;\n"
"    color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-left: 19px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"    border-left: 19px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:checked {\n"
"    border-right: 5px solid rgb(85, 170, 255);\n"
"}")
        self.btn_grafico.setCheckable(True)
        self.btn_grafico.setObjectName("btn_grafico")
        self.verticalLayout.addWidget(self.btn_grafico)
        spacerItem = QtWidgets.QSpacerItem(20, 16777215, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame_menu, 1, 0, 3, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_menu = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_menu.setMaximumSize(QtCore.QSize(60, 50))
        self.btn_menu.setStyleSheet("QPushButton {\n"
"    background-image: url(:icons/icons/cil-menu.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"    border: 0px solid;\n"
"    background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_menu.setText("")
        self.btn_menu.setObjectName("btn_menu")
        self.gridLayout_3.addWidget(self.btn_menu, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"color: rgb(210, 210, 210);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 4)
        self.label_register = QtWidgets.QLabel(self.centralwidget)
        self.label_register.setMinimumSize(QtCore.QSize(0, 25))
        self.label_register.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_register.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"color: rgb(98, 103, 111);\n"
"padding-left: 8px;")
        self.label_register.setObjectName("label_register")
        self.gridLayout.addWidget(self.label_register, 3, 1, 1, 2)
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setMinimumSize(QtCore.QSize(0, 25))
        self.label_version.setMaximumSize(QtCore.QSize(85, 25))
        self.label_version.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"color: rgb(98, 103, 111);\n"
"padding-left: 8px;")
        self.label_version.setObjectName("label_version")
        self.gridLayout.addWidget(self.label_version, 3, 3, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_monitor = QtWidgets.QWidget()
        self.page_monitor.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.page_monitor.setObjectName("page_monitor")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_monitor)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 1)
        self.circularProgressBar_Main = QtWidgets.QFrame(self.page_monitor)
        self.circularProgressBar_Main.setMinimumSize(QtCore.QSize(230, 232))
        self.circularProgressBar_Main.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main.setObjectName("circularProgressBar_Main")
        self.ProgressTemperatura = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.ProgressTemperatura.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.ProgressTemperatura.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.ProgressTemperatura.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressTemperatura.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressTemperatura.setObjectName("ProgressTemperatura")
        self.circularBg_5 = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularBg_5.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_5.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_5.setObjectName("circularBg_5")
        self.circularContainer_5 = QtWidgets.QFrame(self.circularProgressBar_Main)
        self.circularContainer_5.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_5.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_5.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_5.setObjectName("circularContainer_5")
        self.layoutWidget_7 = QtWidgets.QWidget(self.circularContainer_5)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 40, 171, 134))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.infoLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.infoLayout_7.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_7.setObjectName("infoLayout_7")
        self.labelAplicationName_7 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName_7.setFont(font)
        self.labelAplicationName_7.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_7.setObjectName("labelAplicationName_7")
        self.infoLayout_7.addWidget(self.labelAplicationName_7, 0, 0, 1, 1)
        self.labelTemperatura = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelTemperatura.setFont(font)
        self.labelTemperatura.setStyleSheet("color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelTemperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemperatura.setIndent(-1)
        self.labelTemperatura.setObjectName("labelTemperatura")
        self.infoLayout_7.addWidget(self.labelTemperatura, 1, 0, 1, 1)
        self.labelCredits_7 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits_7.setFont(font)
        self.labelCredits_7.setStyleSheet("color: rgb(148, 148, 216); \n"
"background-color: none;\n"
"background-image: url(:/icons/icons/temperatura.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.labelCredits_7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_7.setObjectName("labelCredits_7")
        self.infoLayout_7.addWidget(self.labelCredits_7, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.circularProgressBar_Main, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 2, 1, 1)
        self.circularProgressBar_Main_2 = QtWidgets.QFrame(self.page_monitor)
        self.circularProgressBar_Main_2.setMinimumSize(QtCore.QSize(230, 232))
        self.circularProgressBar_Main_2.setStyleSheet("background-color: none;")
        self.circularProgressBar_Main_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_Main_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_Main_2.setObjectName("circularProgressBar_Main_2")
        self.ProgressHumidade = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.ProgressHumidade.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.ProgressHumidade.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 255, 127, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
        self.ProgressHumidade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressHumidade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressHumidade.setObjectName("ProgressHumidade")
        self.circularBg_4 = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.circularBg_4.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_4.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_4.setObjectName("circularBg_4")
        self.circularContainer_4 = QtWidgets.QFrame(self.circularProgressBar_Main_2)
        self.circularContainer_4.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_4.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_4.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_4.setObjectName("circularContainer_4")
        self.layoutWidget_6 = QtWidgets.QWidget(self.circularContainer_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 40, 171, 134))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.infoLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.infoLayout_6.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_6.setObjectName("infoLayout_6")
        self.labelAplicationName_6 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName_6.setFont(font)
        self.labelAplicationName_6.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_6.setObjectName("labelAplicationName_6")
        self.infoLayout_6.addWidget(self.labelAplicationName_6, 0, 0, 1, 1)
        self.labelHumidade = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelHumidade.setFont(font)
        self.labelHumidade.setStyleSheet("color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelHumidade.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHumidade.setIndent(-1)
        self.labelHumidade.setObjectName("labelHumidade")
        self.infoLayout_6.addWidget(self.labelHumidade, 1, 0, 1, 1)
        self.labelCredits_6 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.labelCredits_6.setFont(font)
        self.labelCredits_6.setStyleSheet("color: rgb(148, 148, 216);\n"
"background-color: none;\n"
"background-image: url(:/icons/icons/humidade.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.labelCredits_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_6.setObjectName("labelCredits_6")
        self.infoLayout_6.addWidget(self.labelCredits_6, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.circularProgressBar_Main_2, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 2, 3, 1, 1)
        self.stackedWidget.addWidget(self.page_monitor)
        self.page_grafico = QtWidgets.QWidget()
        self.page_grafico.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.page_grafico.setObjectName("page_grafico")
        self.stackedWidget.addWidget(self.page_grafico)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 2, 3)
        central.setCentralWidget(self.centralwidget)

        self.retranslateUi(central)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(central)

    def retranslateUi(self, central):
        _translate = QtCore.QCoreApplication.translate
        central.setWindowTitle(_translate("central", "MainWindow"))
        self.btn_monitor.setText(_translate("central", "Monitor"))
        self.btn_grafico.setText(_translate("central", "Gráfico"))
        self.label.setText(_translate("central", "Central de Monitoramento"))
        self.label_register.setText(_translate("central", "Registered by: Ailson Araujo"))
        self.label_version.setText(_translate("central", "Version 1.0.0"))
        self.labelAplicationName_7.setText(_translate("central", "<html><head/><body><p><span style=\" font-weight:600;\">TEMPERATURA</span></p></body></html>"))
        self.labelTemperatura.setText(_translate("central", "<p align=\"center\"><span style=\" font-size:50pt;\">0.0</span><span style=\" font-size:40pt; vertical-align:super;\">°</span></p>"))
        self.labelCredits_7.setText(_translate("central", "<html><head/><body><p><br/></p></body></html>"))
        self.labelAplicationName_6.setText(_translate("central", "<html><head/><body><p><span style=\" font-weight:600;\">HUMIDADE</span></p></body></html>"))
        self.labelHumidade.setText(_translate("central", "<html><head/><body><p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelCredits_6.setText(_translate("central", "<html><head/><body><p><br/></p></body></html>"))
import UI_resource_rc
