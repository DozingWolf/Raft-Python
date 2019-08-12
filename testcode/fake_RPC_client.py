# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6231))

rpc_message = [['127.0.0.1', 'CSY.com', 'RM.01'],[1,1,0],['i am a students']]
pck_rpc_message = pickle.dumps(rpc_message)
print(pck_rpc_message)
print(s.recv(1024).decode('utf-8'))
i = 0
while i < 4:
    s.send(pck_rpc_message)
    print(s.recv(1024).decode('utf-8'))
    i += 1
    
print('client will be send exit code...')
s.send(b'exit')
s.close()
