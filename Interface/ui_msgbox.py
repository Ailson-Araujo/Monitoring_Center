# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_MsgBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MsgDialog(object):
    def setupUi(self, MsgDialog):
        MsgDialog.setObjectName("MsgDialog")
        MsgDialog.resize(333, 142)
        MsgDialog.setMinimumSize(QtCore.QSize(333, 142))
        MsgDialog.setMaximumSize(QtCore.QSize(333, 142))
        MsgDialog.setStyleSheet("QDialog{\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton {\n"
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
        self.gridLayout = QtWidgets.QGridLayout(MsgDialog)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(MsgDialog)
        self.frame.setStyleSheet("background-color: rgba(33, 37, 43, 180);\n"
"border-radius: 8px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(5, 1, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(210, 210, 210);\n"
"background-color: transparent;")
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(self.frame)
        self.btn_ok.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_ok.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout_2.addWidget(self.btn_ok, 2, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.frame)
        self.btn_cancel.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_cancel.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 2, 2, 1, 1)
        self.label_msg = QtWidgets.QLabel(self.frame)
        self.label_msg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_msg.setFont(font)
        self.label_msg.setStyleSheet("background-color: transparent;\n"
"border-radius: 8px;    \n"
"color: rgb(210, 210, 210);\n"
"")
        self.label_msg.setLineWidth(1)
        self.label_msg.setText("")
        self.label_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_msg.setObjectName("label_msg")
        self.gridLayout_2.addWidget(self.label_msg, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(MsgDialog)
        QtCore.QMetaObject.connectSlotsByName(MsgDialog)

    def retranslateUi(self, MsgDialog):
        _translate = QtCore.QCoreApplication.translate
        MsgDialog.setWindowTitle(_translate("MsgDialog", "Aviso"))
        self.label_title.setText(_translate("MsgDialog", "AVISO"))
        self.btn_ok.setText(_translate("MsgDialog", "Ok"))
        self.btn_cancel.setText(_translate("MsgDialog", "Cancelar"))
