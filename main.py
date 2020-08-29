'''
---------------------------------------------------------------------
Copyright © 2020, Ailson Software Development

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

Autor: Ailson Araujo
Versão: 1.0
Data: 11/07/2020
---------------------------------------------------------------------
'''

import sys
import os
import time
#import _thread
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QPropertyAnimation
from interface import Ui_central
import UI_resource_rc
import socket

class LoopRequest(QThread):

    signal = pyqtSignal(int)

    def __init__(self, segundos):
        super(LoopRequest, self).__init__()
        self.segundos = segundos
        #self.central = Central()

    def run(self):

        contador = 0
        while (contador < 100):
            contador = contador +1
            #_thread.start_new_thread(self.comand, ("fire",))
            #self.central.comand("temp")
            cmd = "temp"
            #print(contador)
            time.sleep(self.segundos)
            self.signal.emit(contador)

class Central(QtWidgets.QMainWindow, Ui_central):

    def __init__(self, *args, obj=None, **kwargs):
        super(Central, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.btn_monitor.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.btn_grafico.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.btn_monitor.clicked.connect(lambda:self.marcador(self.btn_monitor))
        self.btn_grafico.clicked.connect(lambda:self.marcador(self.btn_grafico))

        self.btn_menu.clicked.connect(lambda: self.toggleMenu(190, True))
        self.request()

        # self.bt_on.setDisabled(True)
        # self.bt_off.setDisabled(True)
        #self.bt_conn.setVisible(False)
        # self.bt_conn.clicked.connect(lambda:self.conn(True))
        # self.bt_on.clicked.connect(lambda:self.comand('on'))
        # self.bt_off.clicked.connect(self.request)
        #self.bt_off.clicked.connect(lambda:self.comand('fire'))
        #self.bt_on.clicked.connect(self.on)
        #self.bt_off.clicked.connect(self.off)

    def loop(self, x):
        ProgressBar().set_value_temp(x, self.labelTemperatura, self.ProgressTemperatura)
        ProgressBar().set_value_humd(x, self.labelHumidade, self.ProgressHumidade)

    def marcador(self, button):
        btn = [self.btn_monitor, self.btn_grafico]
        btn.remove(button)
        for b in btn:
            b.setChecked(False)
    
            ## ==> SET VALUES TO DEF progressBarValue
        def setValue(self, slider, labelPercentage, progressBarName, color):

            # GET SLIDER VALUE
            value = slider.value()

            # CONVERT VALUE TO INT
            sliderValue = int(value)

            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

            # CALL DEF progressBarValue
            self.progressBarValue(sliderValue, progressBarName, color)

    def setValue(self, slider, labelPercentage, progressBarName, color):

            # GET SLIDER VALUE
            value = slider

            # CONVERT VALUE TO INT
            sliderValue = int(value)

            # HTML TEXT PERCENTAGE
            htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
            labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

            # CALL DEF progressBarValue
            self.progressBarValue(sliderValue, progressBarName, color)

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ProgressTemperatura.setStyleSheet(newStylesheet)

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.frame_menu.width()
            maxExtend = maxWidth
            standard = 60

            # SET MAX WIDTH
            if width == standard:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def conn(self, status):

        try:
            HOST = self.lineEditHost.text()
            PORT = int(self.lineEditPort.text())
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            self.terminal.insertPlainText("---->Falha ao tentar se conectar ao servidor!<----\n\n")
            self.bt_on.setDisabled(True)
            self.bt_off.setDisabled(True)
            return
        else:
            if client.connect_ex((HOST, PORT)) == 0:
                if status:
                    self.bt_on.setDisabled(False)
                    self.bt_off.setDisabled(False)
                    self.terminal.insertPlainText("---->Servidor Conectado!<----\n\n")
                else:
                    return client
            
            else:
                self.terminal.insertPlainText("---->Falha ao tentar se conectar ao servidor!<----\n\n")
                self.terminal.insertPlainText("Tentando Reconecta-se...\n")
                self.bt_on.setDisabled(True)
                self.bt_off.setDisabled(True)
                self.reconn(client, HOST, PORT)
                
    def reconn(self, client, HOST, PORT):

        
        contador = 0
        while(client.connect_ex((HOST, PORT)) != 0):
            contador = contador + 1
            print (contador)
            if contador == 10:
                self.terminal.insertPlainText("\n---->Impossivel conecta-se ao Servidor!<----\n\n")
                break

        else:
            self.terminal.insertPlainText("\n---->Servidor Conectado!<----\n\n")
            self.bt_on.setDisabled(False)
            self.bt_off.setDisabled(False)

    def thread_request(self):
        _thread.start_new_thread(self.request, (1,))
    
    def request(self):

        self.loop_request = LoopRequest(0.1)
        self.loop_request.start()
        self.loop_request.signal.connect(self.loop)
        # contador = 0
        # while (contador < 30):
        #     contador = contador +1
        #     #_thread.start_new_thread(self.comand, ("fire",))
        #     self.comand("temp")
        #     time.sleep(1)

    def comand(self, cmd):

        client = self.conn(False)
        
        if client != None:
            msg = cmd +'\n'
            client.send(msg.encode())
            msg_server = client.recv(2048)
            self.terminal.appendPlainText(msg_server.decode('utf-8'))
            self.terminal.ensureCursorVisible()

class ProgressBar():

    def set_value_temp(self, value, label, widget):

        if value <= 20:
            color = "rgba(85, 170, 255, 255)"
        if value > 20 and value <= 40:
            color = "rgba(30, 255, 45, 255)"
        if value > 40 and value <= 60:
            color = "rgba(240, 240, 35, 255)"
        if value > 60 and value <= 80:
            color = "rgba(255, 125, 30, 255)"
        if value > 80 and value <= 200:
            color = "rgba(240, 30, 30, 255)"

        value = int(value)
        htmlText = """<p align="center"><span style=" font-size:50pt; color:{COLOR}">{VALUE}</span>
                      <span style=" font-size:55pt; vertical-align:super; color:{COLOR}">°</span></p>"""

        label.setText(htmlText.replace("{VALUE}", str(value)).replace("{COLOR}", color))

        # BASE STYLESHEET PROGRESSBAR
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.003)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1"
            stop_2 = "1"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

    def set_value_humd(self, value, label, widget):

        if value <= 20:
            #color = "rgba(85, 170, 255, 255)"
            color = "rgba(240, 30, 30, 255)"
        if value > 20 and value <= 40:
            #color = "rgba(30, 255, 45, 255)"
            color = "rgba(255, 125, 30, 255)"
        if value > 40 and value <= 60:
            color = "rgba(240, 240, 35, 255)"
        if value > 60 and value <= 80:
            #color = "rgba(255, 125, 30, 255)"
            color = "rgba(30, 255, 45, 255)"
        if value > 80 and value <= 200:
            #color = "rgba(240, 30, 30, 255)"
            color = "rgba(85, 170, 255, 255)"

        value = int(value)
        htmlText = """<p align="center"><span style=" font-size:50pt; color:{COLOR}">{VALUE}</span>
                      <span style=" font-size:40pt; vertical-align:super; color:{COLOR}">%</span></p>"""

        label.setText(htmlText.replace("{VALUE}", str(value)).replace("{COLOR}", color))

        # BASE STYLESHEET PROGRESSBAR
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.003)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1"
            stop_2 = "1"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)

    # Configura as cores do tema escuro
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(52, 52, 52))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(42, 42, 42))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(31, 31, 31))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(185, 185, 185))
    palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(185, 185, 185))
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(185, 185, 185))
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(31, 31, 31))
    palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(185, 185, 185))
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.green)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(186, 87, 7).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

    # aplica as confiurações da paletta de cores
    #app.setPalette(palette)

    # inicialização da interface principal
    window = Central()
    window.show()
    
    # encerra a aplicação
    sys.exit(app.exec_())

