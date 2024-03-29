# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket
import threading

def tcplink(sock,addr):
    sock.send(b'Welcome!,this is edmond`s socket server!')
    while True:
        rep_data = sock.recv(1024)
        if rep_data.decode('utf-8') == 'exit':
            break
        print(rep_data)
        sock.send(('hello! %s' % rep_data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connect with ',addr,' is closed')

print('socket server will be start...')
tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1',6231))
tcp_server.listen(6)
print('socket server listen was started with port 6231')
print('now listening...')
while True:
    sock_data,addr_data = tcp_server.accept()
    server_threading = threading.Thread(target=tcplink,args=(sock_data,addr_data))
    server_threading.start()