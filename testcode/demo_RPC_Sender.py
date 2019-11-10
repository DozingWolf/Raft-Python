# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from multiprocessing import Process, Queue
import pickle,os,datetime,random,time
import socket

udpServer = ('127.0.0.1',7600)

def udpSocketSender(queue,userver):
    udpSocketLink = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        getInnerData = queue.get(True)
        sleepTime = random.randint(401, 599)/1000
        print('RPC Sender will sleep %s seconds.' % sleepTime)
        time.sleep(sleepTime)
        udpSocketLink.sendto(getInnerData,userver)
        print('i have send a message to %s:%s'%userver)

def rpcMaker(sendtimes=1):
    if isinstance(sendtimes, int):
        returnData = []
        for i in range(0, sendtimes):
            sendDataList = [i, ['127.0.0.1', 'CSY.com', 'RM.01', 'Leader'], {
                'term': 1, 'index': 1, 'Leader': 'RM.01', 'data': datetime.datetime.now()}]
            returnData.append(sendDataList)
        return returnData
    else:
        print('veriable sendtimes(value = %s) is not a int type'%sendtimes)
        return 'ERROR'
    

if __name__ == "__main__":
    prcQueue = Queue()
    senderProcess = Process(target=udpSocketSender,args=(prcQueue,udpServer,))
    senderProcess.start()
    outputData = rpcMaker(5)
    for rowDate in outputData:
        pckOutPutData = pickle.dumps(rowDate)
        prcQueue.put(pckOutPutData)
