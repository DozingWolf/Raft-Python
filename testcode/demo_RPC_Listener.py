# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import socket,os
from multiprocessing import Process, Queue
import pickle

serverInfo = ('127.0.0.1',6231)

updSocketServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

updSocketServer.bind(serverInfo)

print('server was started on %s:%s'%serverInfo)

print('start new process to edit data list')

print('this is No.%s pid'%os.getpid())

def dataEditer(queue):
    print('my father is : %s'%os.getppid())
    print('i am : %s'%os.getpid())
    while True:
        getDatafromQueue = queue.get(True)
        print('i got a data : %s'%getDatafromQueue)
        print('now i will unpickle this information')
        unpckDatafromQueue = pickle.loads(getDatafromQueue)
        print('finally data is :%s'%unpckDatafromQueue)

if __name__ == "__main__":
    prcQueue = Queue()
    actionProcess = Process(target=dataEditer, args=(prcQueue,))
    actionProcess.start()
    while True:
        rcvData,srcAddr = updSocketServer.recvfrom(1024)
        print('get RPC message from %s:%s'%srcAddr)
        prcQueue.put(rcvData)
