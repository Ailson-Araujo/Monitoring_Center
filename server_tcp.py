import socket
import _thread

num_client = 0
def conn_server():

    global num_client
    LIMITE = 2
    HOST = ''                
    PORT = 9001                    
    addr = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen()

    print ('Aguardando conexão...')

    while True:
        conn, client = server.accept()
        if num_client < LIMITE or num_client == 0:
            num_client += 1
            _thread.start_new_thread(receive_client, (conn, client))
        else:
            conn.close()

def receive_client(conn, client):

    print ('conectado a: ', client)
    global num_client
    msg = ''
    while True:
        
        try:
            char = conn.recv(2048).decode('utf-8')
            #print ('caracter: ', char)
            if not char:
                num_client -= 1
                print (client, ' Desconectado!')
                conn.close()
                return

            msg = msg + char
            #print ('concatenação: ', msg)
            #print ('ultima: ', msg[-1::])
            if msg[-1::]== '\r' or msg[-1::] == '\n':
                _thread.start_new_thread(send_client, (conn, msg))
                msg = ''
        except:
            num_client -= 1
            print (client, ' Desconectado!')
            conn.close()
            return

def send_client(conn, msg):
    global num_client
    try:
        print('Recebido: ', msg)
        msg = msg + '\n'
        conn.send(msg.upper().encode('utf-8'))
    except:
        num_client -= 1
        print (' Desconectado!')
        conn.close()

conn_server()