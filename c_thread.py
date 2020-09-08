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

# Pausa paralela
class Pause(QThread):
    '''Emite um sinal apos o tempo declarado'''

    signal = pyqtSignal()

    def __init__(self, segundos):
        super(Pause, self).__init__()
        self.segundos = segundos

    def run(self):
        time.sleep(self.segundos)
        self.signal.emit()

# Loop de requisição ao servidor
class LoopRequest(QThread):
    '''interval: intervalo de tempo em segundos para as solicitações'''
    
    error = pyqtSignal()                    # retorna sinal de erro
    msg = pyqtSignal(int, str, str)         # retorna sinal com parametros para mensagem de status
    button = pyqtSignal(bool, bool, bool)   # retorna sinal com parametros para habilitar e desabilitar buttons 


    def __init__(self, interval):
        super(LoopRequest, self).__init__()
        self.interval = interval

    def run(self):

        while True:
            global play
            global reconn
            msg = 'ailson' +'\n'

            try:
                # Evia dados ao servidor
                client.send(msg.encode())
            except:
                # Variavel Global que determina que o loop de reconexão deve continuar
                reconn = False
                self.msg.emit(0, 'Conexão perdida!', 'red')
                self.error.emit()
                return
            else:
                # Recebe resposta do servidor
                msg_server = client.recv(2048).decode('utf-8')
                print (msg_server)
                time.sleep(self.interval)

                # Interrompe o loop 
                if play == False:
                    break

# Estabelece conexão com o servidor
class ConnectServer(QThread):
    '''Realiza a conexão com o servidor'''

    conn = pyqtSignal()                     # retorna sinal de conexão estabelecida
    msg = pyqtSignal(int, str, str)         # retorna sinal com parametros para mensagem de status
    button = pyqtSignal(bool, bool, bool)   # retorna sinal com parametros para habilitar e desabilitar buttons

    def __init__(self, host, porta):
        super(ConnectServer, self).__init__()
        self.host = host
        self.porta = porta

    def run(self):
        global client
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
                self.conn.emit()    # Emite sinal de que a conexão foi estabelecida
                self.button.emit(1,0,0)

            else:
                self.msg.emit(0, 'Falha ao tentar se conectar!', 'red')
                self.msg.emit(3, 'Desconectado', 'red')

# Tenta reestabelecer conexão
class ReConn(QThread):
    '''Realiza a reconexão com o servidor
    interval: Tempo de espera em segundos para tentar nova conexão
    number_try: Numero maximo de tentativas de conexão'''

    re_conn = pyqtSignal()                  # retorna sinal de que a conexão foi estabelecida
    msg = pyqtSignal(int, str, str)         # retorna sinal com parametros para mensagem de status
    button = pyqtSignal(bool, bool, bool)   # retorna sinal com parametros para habilitar e desabilitar buttons

    def __init__(self, host, porta, interval, number_try):
        super(ReConn, self).__init__()
        self.host = host
        self.porta = porta
        self.interval = interval
        self.number_try = number_try

    def run(self):
        global label_loading
        cont = 0
        self.msg.emit(2, 'Tentando Reconectar-se', 'blue')

        while (cont < self.number_try):
            cont += 1

            # Intervalo para tentar nova conexão
            time.sleep(self.interval)

            # Inicia a tentativa de conexão
            self.connect_server = ConnectServer(self.host, self.porta)
            self.connect_server.start()

            # Se conexão estabelecida chama a função "is_connected"
            self.connect_server.conn.connect(self.is_connected)

            if reconn:
                label_loading = False   # Interrompe o loop da classe Loading quando reconexão estabelecida
                self.re_conn.emit()     # Emite sinal de que a reconexão foi estabelecida
                return

        # Interrompe o loop da classe Loading quando reconexão perdida
        label_loading = False

    # Define a variavel global "reconn" como True 
    def is_connected(self):
        global reconn
        reconn = True

# Define mensagens na label status quando em reconexão
class Loading(QThread):
    '''caracter: caractere a ser incrementado
    num_caracter: número máximo de caractere a ser exibido
    interval: intervalo em segundos para incremento do caractere'''

    msg = pyqtSignal(int, str, str)         # retorna sinal com parametros para mensagem de status
    button = pyqtSignal(bool, bool, bool)   # retorna sinal com parametros para habilitar e desabilitar buttons

    def __init__(self, caracter, num_caracter, interval):
        super(Loading, self).__init__()
        self.caracter = caracter
        self.num_caracter = num_caracter
        self.interval = interval
        
    def run(self):
        time.sleep(4)
        while (label_loading == True):
            loading = ''
            time.sleep(self.interval)
            
            for i in range(self.num_caracter):
                # Interrompe o loop quando conexão reestabelecida
                if not label_loading:
                    break

                # Realiza o incremento e emit o sinal
                loading += self.caracter
                self.msg.emit(0, loading, 'blue')
                time.sleep(self.interval)

            # Após incremento limpa a label status   
            self.msg.emit(0, '', 'blue')

        # Se reconexão reestabelecida
        if reconn:
            self.msg.emit(0, 'Conectado', 'green')

        else:
            self.msg.emit(0, 'Impossível reconectar-se!', 'red')
            self.msg.emit(3, 'Desconectado', 'red')
            self.button.emit(0,1,1)

# Variaveis Global
play = True             # pausa a execução do loop quando recebe False
client = ''             # variavel de conexão
reconn = False          # variavel de reconexão
label_loading = True    # variavel status label de reconexão