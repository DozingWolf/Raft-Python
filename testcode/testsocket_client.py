# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',6231))

print(s.recv(1024).decode('utf-8'))
i=0
while i<4:
    s.send(b'CSY is Edmond_%d' % i)
    print(s.recv(1024).decode('utf-8'))
    i += 1
print('client will be send exit code...')
s.send(b'exit')
s.close()