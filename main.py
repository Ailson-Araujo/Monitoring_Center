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
import time
import socket

from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QPropertyAnimation, QThreadPool
from ui_main import Ui_central
import UI_resource_rc

import c_progressbar
import c_thread



class Central(QtWidgets.QMainWindow, Ui_central):

    def __init__(self, *args, obj=None, **kwargs):
        super(Central, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.threadpool = QThreadPool()
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
        self.btn_connect.clicked.connect(self.validation)
        self.btn_run.clicked.connect(self.play_stop)
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
        '''Segundos: tempo de espera para definir a mensagem

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
            self.pause.signal.connect(lambda:self.msg_status(0, msg, color))
            self.pause.start()


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

    # Validação de IP e Porta
    def validation(self):

        ip = self.lineEdit_IP.text()
        porta = self.lineEdit_Porta.text()
        if ip == '' and porta == '':
            self.msg_status(0, 'Informe número IP e Porta!', 'red')
            self.msg_status(3, 'Desconectado', 'red')

        elif ip == '':
            self.msg_status(0, 'Informe número IP!', 'red')
            self.msg_status(3, 'Desconectado', 'red')

        elif ip != '' and porta != '':
            try:
                socket.inet_pton(socket.AF_INET, ip)
            except socket.error: 
                self.msg_status(0, 'IP Inválido!', 'red')
                self.msg_status(3, 'Desconectado', 'red')
                self.lineEdit_IP.setFocus()
            else:
                try:
                    porta = int(porta)
                except ValueError:
                    self.msg_status(0, 'Porta Inválida!', 'red')
                    self.msg_status(3, 'Desconectado', 'red')
                    self.lineEdit_Porta.setFocus()
                else:
                    if porta >= 0 and porta <= 65535:                        
                        self.conn(ip, porta)

                    else:
                        self.msg_status(0, 'Informe Porta de 0 a 65535', 'red')
                        self.msg_status(3, 'Desconectado', 'red')
                        self.lineEdit_Porta.setFocus()
        else:
            self.msg_status(0, 'Informe número da Porta!', 'red')
            self.msg_status(3, 'Desconectado', 'red')

    # Conecta ao servidor
    def conn(self, host, porta):

        self.connect_server = c_thread.ConnectServer(host, porta)
        self.connect_server.msg.connect(self.msg_status)
        self.connect_server.button.connect(self.disable_button)
        self.connect_server.start()

        # try:
        #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # except:
        #     self.msg_status(0, 'Falha ao estabelecer ligação!', 'red')
        #     self.msg_status(3, 'Desconectado', 'red')
        # else:
        #     if client.connect_ex((host, porta)) == 0:
        #         self.msg_status(0, 'Conectado', 'green')
        #         self.disable_button(1,0,0)
        #         msg = 'ailson' +'\n'
        #         client.send(msg.encode())
        #         msg_server = client.recv(2048).decode('utf-8')
        #         print (msg_server)
        #     else:
        #         self.msg_status(0, 'Falha ao tentar se conectar!', 'red')
        #         self.msg_status(3, 'Desconectado', 'red')

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

    def play_stop(self):
        
        if self.btn_run.isChecked():
            c_thread.play = True
            self.loop_request = c_thread.LoopRequest(2)
            self.loop_request.start()

        else:          
            c_thread.play = False
            
            
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


    def request(self):

        self.loop_request = c_thread.LoopRequest(0.1)
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

ACTIVATED = ''