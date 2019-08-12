# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket
import threading
import pickle


def tcplink(sock, addr):
    sock.send(b'Welcome!,this is edmond`s socket server!')
    while True:
        rep_data = sock.recv(1024)
        # if rep_data.decode('utf-8') == 'exit':
        #     break
        unpck_rep_data = pickle.loads(rep_data)
        print(type(unpck_rep_data))
        # return_message = '%s'%
        
        sock.send('%s \'s data has been recevered'%unpck_rep_data[0][0])
    sock.close()
    print('connect with ', addr, ' is closed')


print('socket server will be start...')
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1', 6231))
tcp_server.listen(6)
print('socket server listen was started with port 6231')
print('now listening...')
while True:
    sock_data, addr_data = tcp_server.accept()
    server_threading = threading.Thread(
        target=tcplink, args=(sock_data, addr_data))
    server_threading.start()
