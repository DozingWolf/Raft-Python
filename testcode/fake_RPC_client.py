# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket
import pickle
# 打开UDP连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1,10):
    print('no%d'%i)
    # 构造发送数据的数据流
    rpc_message = pickle.dumps(
        [i,['127.0.0.1', 'CSY.com', 'RM.01'], [1, 1, 0], ['i am a students']])
    # 发送构造好的数据
    udp_socket.sendto(rpc_message,('127.0.0.1', 6231))
    # 接受服务端的反馈
    rcv_data,rcv_addr = udp_socket.recvfrom(1024)
    print('we have receved %s from %s' %(pickle.loads(rcv_data),rcv_addr))
udp_socket.close()
