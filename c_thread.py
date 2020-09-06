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
########################################################################
import time
import socket
from PyQt5.QtCore import QThread, pyqtSignal


class Pause(QThread):
    '''Emite um sinal apos o tempo declarado'''

    signal = pyqtSignal()

    def __init__(self, segundos):
        super(Pause, self).__init__()
        self.segundos = segundos

    def run(self):
        time.sleep(self.segundos)
        self.signal.emit()


class LoopRequest(QThread):

    signal = pyqtSignal(int)

    def __init__(self, segundos):
        super(LoopRequest, self).__init__()
        self.segundos = segundos

    def run(self):
        while True:
            print ('running')
            time.sleep(self.segundos)
            if play == False:
                break

        #contador = 0
        # while True:
        #     print ('running')
        #     time.sleep(self.segundos)
        #     if self.activated == False:
        #         break
            #contador = contador +1
            #_thread.start_new_thread(self.comand, ("fire",))
            #self.central.comand("temp")
            #cmd = "temp"
            #print(contador)
            #time.sleep(self.segundos)
            #self.signal.emit(contador)

class ConnectServer(QThread):
    '''Realiza a conexão com o servidor'''

    # Padões de sinais que serão emitidos
    conn = pyqtSignal(object)
    msg = pyqtSignal(int, str, str)
    button = pyqtSignal(bool, bool, bool)

    def __init__(self, host, porta):
        super(ConnectServer, self).__init__()
        self.host = host
        self.porta = porta

    def run(self):
        try: 
            self.msg.emit(0, 'Aguardando Conexão', 'blue')
            # Cria o socket
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            self.msg.emit(0, 'Falha ao estabelecer ligação!', 'red')
            self.msg.emit(3, 'Desconectado', 'red')
        else:
            # Executa a conexão
            if client.connect_ex((self.host, self.porta)) == 0:
                self.msg.emit(0, 'Conectado', 'green')
                self.button.emit(1,0,0)
                # msg = 'ailson' +'\n'
                # client.send(msg.encode())
                # msg_server = client.recv(2048).decode('utf-8')
                # print (msg_server)

            else:
                self.msg.emit(0, 'Falha ao tentar se conectar!', 'red')
                self.msg.emit(3, 'Desconectado', 'red')

# Variavel Global, para a execução do loop quando recebe False                
play = True