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
        central.resize(742, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        central.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(central)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setMinimumSize(QtCore.QSize(0, 25))
        self.label_version.setMaximumSize(QtCore.QSize(85, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"color: rgb(98, 103, 111);\n"
"padding-left: 8px;")
        self.label_version.setObjectName("label_version")
        self.gridLayout.addWidget(self.label_version, 3, 3, 1, 1)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"border: none;\n"
"color: rgb(210, 210, 210);\n"
"padding-top:3px;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.label_page = QtWidgets.QLabel(self.centralwidget)
        self.label_page.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setItalic(False)
        self.label_page.setFont(font)
        self.label_page.setStyleSheet("background-color: rgb(52, 59, 72);\n"
"border: none;\n"
"color: rgb(210, 210, 210);\n"
"padding-bottom: 5px;")
        self.label_page.setText("")
        self.label_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page.setObjectName("label_page")
        self.verticalLayout_2.addWidget(self.label_page)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 4)
        self.label_register = QtWidgets.QLabel(self.centralwidget)
        self.label_register.setMinimumSize(QtCore.QSize(0, 25))
        self.label_register.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_register.setFont(font)
        self.label_register.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"color: rgb(98, 103, 111);\n"
"padding-left: 8px;")
        self.label_register.setObjectName("label_register")
        self.gridLayout.addWidget(self.label_register, 3, 1, 1, 2)
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
        self.btn_setting = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_setting.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btn_setting.setFont(font)
        self.btn_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_setting.setStyleSheet("QPushButton {    \n"
"    background-image: url(:/icons/icons/cil-settings.png);\n"
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
        self.btn_setting.setCheckable(True)
        self.btn_setting.setObjectName("btn_setting")
        self.verticalLayout.addWidget(self.btn_setting)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame_menu, 1, 0, 3, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_monitor = QtWidgets.QWidget()
        self.page_monitor.setStyleSheet("")
        self.page_monitor.setObjectName("page_monitor")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_monitor)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 2, 0, 1, 1)
        self.circularProgressBar_MainTemp = QtWidgets.QFrame(self.page_monitor)
        self.circularProgressBar_MainTemp.setMinimumSize(QtCore.QSize(230, 232))
        self.circularProgressBar_MainTemp.setStyleSheet("background-color: none;")
        self.circularProgressBar_MainTemp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_MainTemp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_MainTemp.setObjectName("circularProgressBar_MainTemp")
        self.ProgressTemperatura = QtWidgets.QFrame(self.circularProgressBar_MainTemp)
        self.ProgressTemperatura.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.ProgressTemperatura.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}")
        self.ProgressTemperatura.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressTemperatura.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressTemperatura.setObjectName("ProgressTemperatura")
        self.circularBg_Temp = QtWidgets.QFrame(self.circularProgressBar_MainTemp)
        self.circularBg_Temp.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_Temp.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_Temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_Temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_Temp.setObjectName("circularBg_Temp")
        self.circularContainer_Temp = QtWidgets.QFrame(self.circularProgressBar_MainTemp)
        self.circularContainer_Temp.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_Temp.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_Temp.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_Temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_Temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_Temp.setObjectName("circularContainer_Temp")
        self.layoutWidget_7 = QtWidgets.QWidget(self.circularContainer_Temp)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 40, 171, 134))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.infoLayout_Temp = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.infoLayout_Temp.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_Temp.setObjectName("infoLayout_Temp")
        self.label_aapTemp = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_aapTemp.setFont(font)
        self.label_aapTemp.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.label_aapTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aapTemp.setObjectName("label_aapTemp")
        self.infoLayout_Temp.addWidget(self.label_aapTemp, 0, 0, 1, 1)
        self.labelTemperatura = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelTemperatura.setFont(font)
        self.labelTemperatura.setStyleSheet("color: rgb(115, 185, 255); \n"
"padding: 0px; \n"
"background-color: none;")
        self.labelTemperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemperatura.setIndent(-1)
        self.labelTemperatura.setObjectName("labelTemperatura")
        self.infoLayout_Temp.addWidget(self.labelTemperatura, 1, 0, 1, 1)
        self.label_IconTemp = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_IconTemp.setFont(font)
        self.label_IconTemp.setStyleSheet("color: rgb(148, 148, 216); \n"
"background-color: none;\n"
"background-image: url(:/icons/icons/temperatura.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_IconTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IconTemp.setObjectName("label_IconTemp")
        self.infoLayout_Temp.addWidget(self.label_IconTemp, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.circularProgressBar_MainTemp, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 2, 2, 1, 1)
        self.circularProgressBar_MainHumd = QtWidgets.QFrame(self.page_monitor)
        self.circularProgressBar_MainHumd.setMinimumSize(QtCore.QSize(230, 232))
        self.circularProgressBar_MainHumd.setStyleSheet("background-color: none;")
        self.circularProgressBar_MainHumd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBar_MainHumd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBar_MainHumd.setObjectName("circularProgressBar_MainHumd")
        self.ProgressHumidade = QtWidgets.QFrame(self.circularProgressBar_MainHumd)
        self.ProgressHumidade.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.ProgressHumidade.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.600 rgba(85, 255, 127, 255), stop:0.595 rgba(255, 255, 255, 0));\n"
"}")
        self.ProgressHumidade.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ProgressHumidade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressHumidade.setObjectName("ProgressHumidade")
        self.circularBg_Humd = QtWidgets.QFrame(self.circularProgressBar_MainHumd)
        self.circularBg_Humd.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg_Humd.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg_Humd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg_Humd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg_Humd.setObjectName("circularBg_Humd")
        self.circularContainer_Humd = QtWidgets.QFrame(self.circularProgressBar_MainHumd)
        self.circularContainer_Humd.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_Humd.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_Humd.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(58, 58, 102);\n"
"}")
        self.circularContainer_Humd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_Humd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_Humd.setObjectName("circularContainer_Humd")
        self.layoutWidget_6 = QtWidgets.QWidget(self.circularContainer_Humd)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 40, 171, 134))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.infoLayout_Humd = QtWidgets.QGridLayout(self.layoutWidget_6)
        self.infoLayout_Humd.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_Humd.setObjectName("infoLayout_Humd")
        self.labelappHumd = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.labelappHumd.setFont(font)
        self.labelappHumd.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelappHumd.setAlignment(QtCore.Qt.AlignCenter)
        self.labelappHumd.setObjectName("labelappHumd")
        self.infoLayout_Humd.addWidget(self.labelappHumd, 0, 0, 1, 1)
        self.labelHumidade = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(30)
        self.labelHumidade.setFont(font)
        self.labelHumidade.setStyleSheet("color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelHumidade.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHumidade.setIndent(-1)
        self.labelHumidade.setObjectName("labelHumidade")
        self.infoLayout_Humd.addWidget(self.labelHumidade, 1, 0, 1, 1)
        self.label_IconHumd = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_IconHumd.setFont(font)
        self.label_IconHumd.setStyleSheet("color: rgb(148, 148, 216);\n"
"background-color: none;\n"
"background-image: url(:/icons/icons/humidade.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.label_IconHumd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_IconHumd.setObjectName("label_IconHumd")
        self.infoLayout_Humd.addWidget(self.label_IconHumd, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.circularProgressBar_MainHumd, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 2, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 3, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_conection = QtWidgets.QFrame(self.page_monitor)
        self.frame_conection.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_conection.setMaximumSize(QtCore.QSize(335, 107))
        self.frame_conection.setStyleSheet("background-color: rgba(33, 37, 43, 180);\n"
"border-radius: 8px;    \n"
"")
        self.frame_conection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_conection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conection.setObjectName("frame_conection")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_conection)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelBoxBlenderInstalation = QtWidgets.QLabel(self.frame_conection)
        self.labelBoxBlenderInstalation.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet("color: rgb(210, 210, 210);\n"
"background-color: transparent;")
        self.labelBoxBlenderInstalation.setObjectName("labelBoxBlenderInstalation")
        self.gridLayout_2.addWidget(self.labelBoxBlenderInstalation, 0, 0, 1, 2)
        self.btn_connect = QtWidgets.QPushButton(self.frame_conection)
        self.btn_connect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_connect.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"    color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled{\n"
"    color: rgb(40, 44, 52);\n"
"}")
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout_2.addWidget(self.btn_connect, 1, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.frame_conection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;    \n"
"    background-color: rgb(52, 59, 72);\n"
"    color: rgb(210, 210, 210);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QPushButton:disabled{\n"
"    color: rgb(40, 44, 52);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_2.addWidget(self.btn_save, 2, 1, 1, 1)
        self.lineEdit_Porta = QtWidgets.QLineEdit(self.frame_conection)
        self.lineEdit_Porta.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Porta.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_Porta.setText("")
        self.lineEdit_Porta.setObjectName("lineEdit_Porta")
        self.gridLayout_2.addWidget(self.lineEdit_Porta, 2, 0, 1, 1)
        self.lineEdit_IP = QtWidgets.QLineEdit(self.frame_conection)
        self.lineEdit_IP.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_IP.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_IP.setText("")
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.gridLayout_2.addWidget(self.lineEdit_IP, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_conection)
        self.frame_status = QtWidgets.QFrame(self.page_monitor)
        self.frame_status.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_status.setMaximumSize(QtCore.QSize(16777215, 107))
        self.frame_status.setStyleSheet("background-color: rgba(33, 37, 43, 180);\n"
"border-radius: 8px;    \n"
"")
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_status)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelBoxBlenderInstalation_2 = QtWidgets.QLabel(self.frame_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBoxBlenderInstalation_2.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation_2.setSizePolicy(sizePolicy)
        self.labelBoxBlenderInstalation_2.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet("color: rgb(210, 210, 210);\n"
"background-color: transparent;")
        self.labelBoxBlenderInstalation_2.setObjectName("labelBoxBlenderInstalation_2")
        self.gridLayout_5.addWidget(self.labelBoxBlenderInstalation_2, 0, 1, 1, 1)
        self.label_status = QtWidgets.QLabel(self.frame_status)
        self.label_status.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color: rgb(115, 185, 255);\n"
"background-color: transparent;")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.gridLayout_5.addWidget(self.label_status, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem6, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_status)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_run = QtWidgets.QPushButton(self.page_monitor)
        self.btn_run.setEnabled(True)
        self.btn_run.setMinimumSize(QtCore.QSize(60, 50))
        self.btn_run.setMaximumSize(QtCore.QSize(60, 50))
        self.btn_run.setStyleSheet("QPushButton{\n"
"    background-image: url(:/icons/icons/cil-media-play.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border-radius: 8px;    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(52, 58, 68);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:checked {\n"
"    background-image: url(:/icons/icons/cil-media-pause.png);\n"
"}\n"
"QPushButton:disabled{\n"
"    background-image: url(:/icons/icons/cil-media-play-dark.png);\n"
"}")
        self.btn_run.setText("")
        self.btn_run.setCheckable(True)
        self.btn_run.setObjectName("btn_run")
        self.gridLayout_4.addWidget(self.btn_run, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 1, 0, 1, 5)
        self.stackedWidget.addWidget(self.page_monitor)
        self.page_grafico = QtWidgets.QWidget()
        self.page_grafico.setStyleSheet("")
        self.page_grafico.setObjectName("page_grafico")
        self.stackedWidget.addWidget(self.page_grafico)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.stackedWidget.addWidget(self.page_setting)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 2, 3)
        central.setCentralWidget(self.centralwidget)

        self.retranslateUi(central)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(central)

    def retranslateUi(self, central):
        _translate = QtCore.QCoreApplication.translate
        central.setWindowTitle(_translate("central", "Central de Monitoramento"))
        self.label_version.setText(_translate("central", "Version 1.0.0"))
        self.label_title.setText(_translate("central", "Central de Monitoramento"))
        self.label_register.setText(_translate("central", "<html><head/><body><p>Desenvolvido:<span style=\" font-weight:600;\"> Ailson Araujo</span></p></body></html>"))
        self.btn_monitor.setText(_translate("central", "Monitor"))
        self.btn_grafico.setText(_translate("central", "Gráfico"))
        self.btn_setting.setText(_translate("central", "Configurações"))
        self.label_aapTemp.setText(_translate("central", "<html><head/><body><p><span style=\" font-weight:600;\">TEMPERATURA</span></p></body></html>"))
        self.labelTemperatura.setText(_translate("central", "<p align=\"center\"><span style=\" font-size:50pt;\">0.0</span><span style=\" font-size:40pt; vertical-align:super;\">°</span></p>"))
        self.label_IconTemp.setText(_translate("central", "<html><head/><body><p><br/></p></body></html>"))
        self.labelappHumd.setText(_translate("central", "<html><head/><body><p><span style=\" font-weight:600;\">HUMIDADE</span></p></body></html>"))
        self.labelHumidade.setText(_translate("central", "<html><head/><body><p align=\"center\"><span style=\" font-size:50pt;\">0</span><span style=\" font-size:40pt; vertical-align:super;\">%</span></p></body></html>"))
        self.label_IconHumd.setText(_translate("central", "<html><head/><body><p><br/></p></body></html>"))
        self.labelBoxBlenderInstalation.setText(_translate("central", "CONEXÃO"))
        self.btn_connect.setText(_translate("central", "Conectar"))
        self.btn_save.setText(_translate("central", "Salvar Conexão"))
        self.lineEdit_Porta.setPlaceholderText(_translate("central", "Porta"))
        self.lineEdit_IP.setPlaceholderText(_translate("central", "Endereço IP"))
        self.labelBoxBlenderInstalation_2.setText(_translate("central", "STATUS"))
        self.label_status.setText(_translate("central", "Aguardando Conexão"))
import UI_resource_rc
