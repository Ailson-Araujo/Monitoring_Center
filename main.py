########################################################################
## Copyright © 2020 Ailson Araujo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## Versão: 1.0.0
## Iniciado: 29/08/2020
## Finalizado:
##
## Este projeto pode ser usado livremente, desde que mantenham
## os respectivos créditos nos scripts Python.
## Projeto feito com Qt Designer, PyQt5 e Matplotlib
## PROGRESSEBAR DESIGNER BY: WANDERSON M.PIMENTA
########################################################################


import sys
import os
import socket
import UI_resource_rc
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtWidgets import QMessageBox, QColorDialog
from PyQt5.QtCore import QPropertyAnimation, QThreadPool, QSettings
from PyQt5.QtGui import QColor
from Interface.ui_main import Ui_central
from modulos import c_progressbar
from modulos import c_thread
from c_mplwidget import MplWidget
import random

class Central(QtWidgets.QMainWindow, Ui_central):

    def __init__(self, *args, obj=None, **kwargs):
        super(Central, self).__init__(*args, **kwargs)
        self.setupUi(self)
        #registro do Windows
        self.setting = QSettings('Ailson Software Development', 'Monitoring Center')

        #Inicialização
        self.validation_register()
        self.charge_setting()
        self.charge_position()
        self.disable_button(0,1,1)
        self.btn_monitor.setChecked(True)
        self.label_title.setText("Monitor")
        self.msg_status(0, 'Inicializando', 'blue')
        c_progressbar.SetValueProgressBar(0, 0, self.labelTemperatura, self.ProgressTemperatura)
        c_progressbar.SetValueProgressBar(1, 0, self.labelHumidade, self.ProgressHumidade)
        self.init_gauge()
        self.init_plot()
        self._plot_ref = None
        self.xdata = list(range(10))
        self.ytemp = [0 for i in range(10)]
        self.yhumd = [0 for i in range(10)]
        

        # Paginas
        self.btn_monitor.clicked.connect(lambda:self.select_page(self.btn_monitor))
        self.btn_grafico.clicked.connect(lambda:self.select_page(self.btn_grafico))
        self.btn_setting.clicked.connect(lambda:self.select_page(self.btn_setting))

        # Ações
        self.btn_menu.clicked.connect(lambda: self.Menu(190, True))
        self.btn_connect.clicked.connect(self.validation)
        self.btn_run.clicked.connect(self.play_stop)
        self.btn_save_config.clicked.connect(self.save_setting)
        self.btn_color_temp.clicked.connect(lambda: self.dialog_color(0))
        self.btn_color_humd.clicked.connect(lambda: self.dialog_color(1))


    # Desabilita Botões
    def disable_button(self, conn, save, run):
        '''
        True ou 1: Desabilita
        False ou 0: Habilita
        '''
        self.btn_connect.setDisabled(conn)
        self.btn_save.setDisabled(save)
        self.btn_run.setDisabled(run)

        if not conn:
            self.btn_run.setChecked(False)

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

    # Define os valores dos sensores no gauge
    def set_gauge(self, value_temp, value_humd):
        c_progressbar.SetValueProgressBar(0, value_temp, self.labelTemperatura, self.ProgressTemperatura)
        c_progressbar.SetValueProgressBar(1, value_humd, self.labelHumidade, self.ProgressHumidade)

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
            self.label_title.setText("Monitor")
        if button == self.btn_grafico:
            self.stackedWidget.setCurrentIndex(1)
            self.label_title.setText("Gráfico")
        if button == self.btn_setting:
            self.stackedWidget.setCurrentIndex(2)
            self.label_title.setText("Configurações")

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
        global ip, porta
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
                # Testa se é um IP válido
                socket.inet_pton(socket.AF_INET, ip)
            except socket.error: 
                self.msg_status(0, 'IP Inválido!', 'red')
                self.msg_status(3, 'Desconectado', 'red')
                self.lineEdit_IP.setFocus()
            else:
                try:
                    # Testa se é um numero inteiro
                    porta = int(porta)
                except ValueError:
                    self.msg_status(0, 'Porta Inválida!', 'red')
                    self.msg_status(3, 'Desconectado', 'red')
                    self.lineEdit_Porta.setFocus()
                else:
                    # Testa se esta entre os valores de portas válidas
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

        # Realiza a conexão com o servidor em um processamento paralelo
        self.connect_server = c_thread.ConnectServer(host, porta)
        self.connect_server.msg.connect(self.msg_status)
        self.connect_server.button.connect(self.disable_button)
        self.connect_server.start()

    # Inicia a solicitação ao servidor
    def play_stop(self):
        
        if self.btn_run.isChecked():
            c_thread.play = True
            self.loop_request = c_thread.LoopRequest(self.setting.value('request'))
            self.loop_request.msg.connect(self.msg_status)
            self.loop_request.button.connect(self.disable_button)
            self.loop_request.error.connect(self.reconn) # Chama reconn se houver erro de conexão
            self.loop_request.gauge.connect(self.set_gauge)
            self.loop_request.plot.connect(self.update_plot)
            self.loop_request.start()

        # Interrompe a solicitação ao servidor
        else:          
            c_thread.play = False

    # Tenta a reconexão com o servidor     
    def reconn(self):

        # Define o status de reconexão na label status
        c_thread.label_loading = True
        self.loading = c_thread.Loading('°', 3, 0.3)
        self.loading.msg.connect(self.msg_status)
        self.loading.button.connect(self.disable_button)
        self.loading.start()

        # Inicia a tentativa de reconexão
        self.reconn_server = c_thread.ReConn(ip, porta, 3, self.setting.value('reconn'))
        self.reconn_server.msg.connect(self.msg_status)
        self.reconn_server.re_conn.connect(self.play_stop)  # Chama play_stop se reconexão estabelecida
        self.reconn_server.start()

    # Inicialização do efeito
    def init_gauge(self):
        self.boot = c_thread.BootEffect(0.005)
        self.boot.value_gauge.connect(self.set_gauge)
        self.boot.msg.connect(self.msg_status)
        self.boot.start()

    # Inicilaiza o gráfico
    def init_plot(self):

        self.MplWidget.axes.tick_params(labelcolor = '#f0f0f0')
        self.MplWidget.axes.set_facecolor('#282c34')
        self.MplWidget.axes.tick_params(color = '#282c34')
        #self.MplWidget.axes.tick_params(labelbottom = False)
        self.MplWidget.axes.spines['top'].set_color('#1b1d23')
        self.MplWidget.axes.spines['right'].set_color('#1b1d23')
        self.MplWidget.axes.spines['bottom'].set_color('#1b1d23')
        self.MplWidget.axes.spines['left'].set_color('#1b1d23')

        # self.MplWidget.axes.set_xlabel('Horario da Leitura', fontfamily='Segoe UI', fontsize=11, color='#f0f0f0', fontweight='bold')
        # self.MplWidget.axes.set_ylabel('Temperatura / Humidade',fontfamily='Segoe UI', fontsize=11, color='#f0f0f0', fontweight='bold')
        # self.MplWidget.axes.grid(color = '#505050', linestyle='--')
        
    # Atualiza o gráfico
    def update_plot(self, temp, humd, date_hora):
        
        self.ytemp = self.ytemp[1:] + [temp]
        self.yhumd = self.yhumd[1:] + [humd]
        self.xdata = self.xdata[1:] + [date_hora]

        self.MplWidget.axes.cla()
        for label in self.MplWidget.axes.get_xticklabels():
            label.set_rotation(30)
            label.set_horizontalalignment('right')

        self.MplWidget.axes.plot(self.xdata, self.ytemp,
                                 color = self.setting.value('color_temp'),
                                 marker = 'o',
                                 label = 'Temperatura')

        self.MplWidget.axes.plot(self.xdata, self.yhumd,
                                 color = self.setting.value('color_humd'),
                                 marker = 'o',
                                 label = 'Humidade')

        self.MplWidget.axes.set_xlabel('Horario da Leitura', fontfamily='Segoe UI', fontsize=11, color='#f0f0f0', fontweight='bold')
        self.MplWidget.axes.set_ylabel('Temperatura / Humidade',fontfamily='Segoe UI', fontsize=11, color='#f0f0f0', fontweight='bold')
        self.MplWidget.axes.grid(color = '#505050', linestyle='--')
        
        legend = self.MplWidget.axes.legend(loc='upper left', ncol=1, frameon=True, framealpha= 0.1)

        # Subistitui as cores do texto da legenda
        for text in legend.get_texts():
            text.set_color('#f0f0f0')

        self.MplWidget.canvas.draw()

    # salva informações quando aplicação é finalizada
    def closeEvent(self, event):

        # salva a posição e o tamanho do app ao ser finalizado
        self.setting.setValue('size', self.size())
        self.setting.setValue('position', self.pos())
        self.setting.setValue('max', self.isMaximized())

    # carrega as configurações de localização e tamanho do app
    def charge_position(self):

        try:
            # caso a janela tenha sido maxmizada
            if self.setting.value('max') == 'true':
                self.resize(self.setting.value('size'))
                self.move(self.setting.value('position'))
                self.showMaximized()

            # janela não foi maxmizada
            else:
                self.resize(self.setting.value('size'))
                self.move(self.setting.value('position'))
        except:
            pass

    # Valida os dados do registro caso não existam
    def validation_register(self):       

        # valores padrões
        if self.setting.value('request') == None:
            self.setting.setValue('request', 3)

        if self.setting.value('reconn') == None:
            self.setting.setValue('reconn', 3)

        if self.setting.value('color_temp') == None:
            self.setting.setValue('color_temp', '#52BC56')

        if self.setting.value('color_humd') == None:
            self.setting.setValue('color_humd', '#73B9FF')

    # Carrega os dados da pagina configurações
    def charge_setting(self):

        self.spinBox_request.setValue(self.setting.value('request'))
        self.spinBox_reconn.setValue(self.setting.value('reconn'))

        # Dicionario
        dic_color = {'BTN': [self.btn_color_temp,
                             self.btn_color_humd],

                     'COLOR': ['color_temp',
                               'color_humd']}
        
        for index in range(2):
            dic_color['BTN'][index].setStyleSheet("QPushButton {\n"
                                                  "    border: 2px solid rgb(52, 59, 72);\n"
                                                  "    border-radius: 5px;    \n"
                                                  "    background-color: %s;\n"
                                                  "    color: rgb(210, 210, 210);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    border: 2px solid rgb(61, 70, 86);\n"
                                                  "}\n"
                                                  "QPushButton:pressed {\n"
                                                  "    border: 2px solid rgb(43, 50, 61);\n"
                                                  "}" %self.setting.value(dic_color['COLOR'][index]))

    # Salva os dados de Configurações
    def save_setting(self):

        self.setting.setValue('request', (self.spinBox_request.value()))
        self.setting.setValue('reconn', (self.spinBox_reconn.value()))

    # abre a caixa de dialogo para escolha das cores
    def dialog_color(self, button):
        
        # dicionario com as variaveis dos frames
        # a variavel button recebe um inteiro que fará referência ao botão clicado
        dic_color = {'BTN': [self.btn_color_temp,
                             self.btn_color_humd],

                     'COLOR': ['color_temp',
                               'color_humd'],

                     'TITLE': ['Selecionar cor da Temperatura',
                               'Selecionar cor da Humidade']}
        
        #recebe a cor selecionada
        selected_color = QColorDialog.getColor(initial = QtGui.QColor(self.setting.value(dic_color['COLOR'][button])), 
                                               title = dic_color['TITLE'][button])

        if selected_color.isValid():
            dic_color['BTN'][button].setStyleSheet("QPushButton {\n"
                                                   "    border: 2px solid rgb(52, 59, 72);\n"
                                                   "    border-radius: 5px;    \n"
                                                   "    background-color: %s;\n"
                                                   "    color: rgb(210, 210, 210);\n"
                                                   "}\n"
                                                   "QPushButton:hover {\n"
                                                   "    border: 2px solid rgb(61, 70, 86);\n"
                                                   "}\n"
                                                   "QPushButton:pressed {\n"
                                                   "    border: 2px solid rgb(43, 50, 61);\n"
                                                   "}" %selected_color.name())

            # Salva a cor no registro
            self.setting.setValue(dic_color['COLOR'][button], selected_color.name())

if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)

    # inicialização da interface principal
    window = Central()
    window.show()

    # encerra a aplicação
    sys.exit(app.exec_())

# Variaveis Globais
ip = ''
porta = ''