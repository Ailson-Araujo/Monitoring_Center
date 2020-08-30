########################################################################
## MIT License
## Copyright © 2020, Ailson Software Development
##
## Autor: Ailson Araujo
## Versão: 1.0.0
## Data: 29/08/2020
##
## Este projeto pode ser usado livremente, desde que mantenham
## os respectivos créditos apenas nos scripts Python.
##
## PROGRESSEBAR DESIGNER BY: WANDERSON M.PIMENTA
########################################################################


import sys
import os
#import time
import socket

from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QPropertyAnimation
from ui_main import Ui_central
import UI_resource_rc

import c_progressbar
#from c_thread import Pause
import c_thread

# class LoopRequest(QThread):

#     signal = pyqtSignal(int)

#     def __init__(self, segundos):
#         super(LoopRequest, self).__init__()
#         self.segundos = segundos
#         #self.central = Central()

#     def run(self):

#         contador = 0
#         while (contador < 100):
#             contador = contador +1
#             #_thread.start_new_thread(self.comand, ("fire",))
#             #self.central.comand("temp")
#             cmd = "temp"
#             #print(contador)
#             time.sleep(self.segundos)
#             self.signal.emit(contador)

class Central(QtWidgets.QMainWindow, Ui_central):

    def __init__(self, *args, obj=None, **kwargs):
        super(Central, self).__init__(*args, **kwargs)
        self.setupUi(self)

        #Inicialização
        self.disable_button(0,1,1)
        self.btn_monitor.setChecked(True)
        self.label_page.setText("Monitor")
        c_progressbar.SetValueProgressBar(0, 0, self.labelTemperatura, self.ProgressTemperatura)
        c_progressbar.SetValueProgressBar(1, 0, self.labelHumidade, self.ProgressHumidade)

        # Paginas
        self.btn_monitor.clicked.connect(lambda:self.select_page(self.btn_monitor))
        self.btn_grafico.clicked.connect(lambda:self.select_page(self.btn_grafico))
        self.btn_setting.clicked.connect(lambda:self.select_page(self.btn_setting))

        # Ações
        self.btn_menu.clicked.connect(lambda: self.Menu(190, True))
        self.btn_connect.clicked.connect(self.conn)
        #self.request()

        # self.bt_on.setDisabled(True)
        # self.bt_off.setDisabled(True)
        #self.bt_conn.setVisible(False)
        # self.bt_conn.clicked.connect(lambda:self.conn(True))
        # self.bt_on.clicked.connect(lambda:self.comand('on'))
        # self.bt_off.clicked.connect(self.request)
        #self.bt_off.clicked.connect(lambda:self.comand('fire'))
        #self.bt_on.clicked.connect(self.on)
        #self.bt_off.clicked.connect(self.off)

    # Desabilita Botões
    def disable_button(self, conn, save, run):
        '''
        True ou 1: Desabilita
        False ou 0: Habilita
        '''
        self.btn_connect.setDisabled(conn)
        self.btn_save.setDisabled(save)
        self.btn_run.setDisabled(run)

    # Define mensagem na label Status
    def msg_status(self, segundos, msg, color):
        '''
        Segundos: tempo de espera para definir a mensagem
        "0" define imediatamente
        color: red, green ou blue'''

        if color == 'red': color = 'rgb(236, 52, 52)'
        if color == 'green': color = 'rgb(82, 188, 86)'
        if color == 'blue': color = 'rgb(115, 185, 255)'
        if segundos == 0:
            self.label_status.setStyleSheet('color: %s; background-color: transparent' %color)
            self.label_status.setText(msg)
        else:
            self.pause = c_thread.Pause(segundos)
            self.pause.start()
            self.pause.signal.connect(lambda:self.msg_status(0, 'Desconectado', 'red'))


    def loop(self, value):
        c_progressbar.SetValueProgressBar(0, value, self.labelTemperatura, self.ProgressTemperatura)
        c_progressbar.SetValueProgressBar(1, value, self.labelHumidade, self.ProgressHumidade)

    # Exibe a pagina selecionada do stackeWidget
    def select_page(self, button):

        # inverte o valor do button que estava checked
        btn = [self.btn_monitor, self.btn_grafico, self.btn_setting]
        btn.remove(button)
        for b in btn:
            b.setChecked(False)

        #Exibe a pagina
        if button == self.btn_monitor:
            self.stackedWidget.setCurrentIndex(0)
            self.label_page.setText("Monitor")
        if button == self.btn_grafico:
            self.stackedWidget.setCurrentIndex(1)
            self.label_page.setText("Gráfico")
        if button == self.btn_setting:
            self.stackedWidget.setCurrentIndex(2)
            self.label_page.setText("Configurações")

    # Alterna a largura do menu
    def Menu(self, maxWidth, enable):

        if enable:
            # obtem a largura
            width = self.frame_menu.width()
            width_standard = 60

            # Define a maxima largura
            if width == width_standard:
                widthExtended = maxWidth
            else:
                widthExtended = width_standard

            # Animação
            self.animation = QPropertyAnimation(self.frame_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # Conecta ao servidor
    def conn(self):

        if (self.lineEdit_IP.text() != '' and int(self.lineEdit_Porta.text()) != ''):
            self.disable_button(1,0,0)

        else:
            self.msg_status(0, 'Insira os dados!', 'red')
            self.msg_status(3, 'Desconectado', 'red')

        # try:
        #     HOST = self.lineEditHost.text()
        #     PORT = int(self.lineEditPort.text())
        #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # except:
        #     self.terminal.insertPlainText("---->Falha ao tentar se conectar ao servidor!<----\n\n")
        #     self.bt_on.setDisabled(True)
        #     self.bt_off.setDisabled(True)
        #     return
        # else:
        #     if client.connect_ex((HOST, PORT)) == 0:
        #         if status:
        #             self.bt_on.setDisabled(False)
        #             self.bt_off.setDisabled(False)
        #             self.terminal.insertPlainText("---->Servidor Conectado!<----\n\n")
        #         else:
        #             return client

        #     else:
        #         self.terminal.insertPlainText("---->Falha ao tentar se conectar ao servidor!<----\n\n")
        #         self.terminal.insertPlainText("Tentando Reconecta-se...\n")
        #         self.bt_on.setDisabled(True)
        #         self.bt_off.setDisabled(True)
        #         self.reconn(client, HOST, PORT)

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

    def comand(self, cmd):

        client = self.conn(False)

        if client != None:
            msg = cmd +'\n'
            client.send(msg.encode())
            msg_server = client.recv(2048)
            self.terminal.appendPlainText(msg_server.decode('utf-8'))
            self.terminal.ensureCursorVisible()




if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)

    # inicialização da interface principal
    window = Central()
    window.show()

    # encerra a aplicação
    sys.exit(app.exec_())

