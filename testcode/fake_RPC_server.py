# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket
from multiprocessing import Process, Queue
import pickle

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# bind
udp_socket.bind(('127.0.0.1',6231))
print('bind udp on port 6231')

while True:
    # 开始接收数据
    data,addr = udp_socket.recvfrom(1024)
    print('receve data from %s:%s. , data = ' %addr,pickle.loads(data))
    print('return message to sender%s:%s' %addr)
    # 构造反馈数据流
    return_data = pickle.loads(data)
    # 发送反馈数据
    udp_socket.sendto(pickle.dumps(return_data[0]),addr)