# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine
from parameterloader import ParaLoder
from multiprocessing import Process, Queue
import time,datetime
import os
import socket
import pickle
import random

class RaftSender(RaftMachine):
    def __init__(self):
        super().__init__(modelname='RaftSender')
        self.__senderAddrList = super().getNeighborIPList()
        self.__senderPort = super().getLocalhostPort()
        self.__senderHostName = super().getLocalhostName()
        self.__senderLocalIP = super().getLocalhostIP()
        self.__senderLogger = super().getRMLogger()
        self.__rmDomain = super().getRMDomain()
        self.__mainProcessSID = 0
        self.__subProcessSID = 0
        # 应该获取邻居的list
        self.__neighborServerList = super().getNeighborIPList()
        #
        self.__raftCharacter = super().getLocslCharacter()
        self.__senderLogger.debug(
            'Local raft machine\'s character is %s' % super().getLocslCharacter())
        # create a inner queue
        self.__senderQueue = Queue()
        # get a out queue

        # 
        self.__senderLogger.debug(
            'Set socket parameter(socket.AF_INET,socket.SOCK_DGRAM)')
        self.__updSocketLink = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def callLogicalCenter(self):
        def getRaftCharacter(self):
            # ask logical center
            self.__newRaftCharacter = ''
            return self.__newRaftCharacter
        def updateLocalRaftCharacter(self):
            self.__raftCharacter = self.getRaftCharacter()

    def makeRPCHeartbeatMessage(self, rpcdata=datetime.datetime.now()):
        self.__heartbeatMessage = [[self.__senderLocalIP, self.__rmDomain, self.__senderHostName, self.__raftCharacter], {
            'term': 1, 'index': 1, 'Leader': 'RM.01', 'data': rpcdata}]
        return self.__heartbeatMessage

    def udpSocketSender(self, queue):
        self.__subProcessSID = os.getpid()
        while True:
            self.__getInnerData = queue.get(True)
            self.__sendMessage = self.__getInnerData[0]
            if type(self.__getInnerData[1]) == list:
                for self.__aimsNo ,self.__aimsIP in enumerate(self.__getInnerData[1]):
                    self.__aimsIPPortSet = (self.__aimsIP,self.__senderPort)
                    self.__updSocketLink.sendto(
                        self.__sendMessage, self.__aimsIPPortSet)
                    self.__senderLogger.debug('row message is %s' % self.__sendMessage)
                    self.__senderLogger.debug('i have send a message %s:%s' % self.__aimsIPPortSet)
            else:
                self.__aimsNo = 0
                self.__aimsIPPortSet = (self.__getInnerData[1],self.__senderPort)
                self.__updSocketLink.sendto(
                    self.__sendMessage, self.__aimsIPPortSet)
                self.__senderLogger.debug('row message is %s' % self.__sendMessage)
                self.__senderLogger.debug('i have send a message to %s:%s'% self.__aimsIPPortSet)

            self.__heartbeatIntervalTime = random.randint(401, 599)/1000
            self.__senderLogger.debug('RPC Sender will sleep %s seconds.' %
                    self.__heartbeatIntervalTime)
            time.sleep(self.__heartbeatIntervalTime)
        
    def startSenderProcess(self):
        self.__mainProcessSID = os.getpid()
        self.__senderLogger.info('Sender pid is %s' % self.__mainProcessSID)
        self.__sendProcess = Process(target=self.udpSocketSender, args=(self.__senderQueue,))
        self.__sendProcess.start()

    def closeSenderProcess(self):
        try:
            os.kill(self.__subProcessSID, 0)
        except OSError:
            return OSError
        else:
            self.__subProcessSID = -99
            self.__sendProcess.terminate()

    def pushIntoSendQueue(self,message,iplist):
        self.__sendProcessPicklle = [pickle.dumps(message),iplist]
        self.__senderQueue.put(self.__sendProcessPicklle)

# test code
rs = RaftSender()
rs.startSenderProcess()
rs.pushIntoSendQueue(rs.makeRPCHeartbeatMessage(), ['127.0.0.1','10.62.24.1'])
rs.pushIntoSendQueue(rs.makeRPCHeartbeatMessage(rpcdata = 'Test_message_127.0.0.1'), ['127.0.0.1', '10.62.24.1'])
time.sleep(5)
rs.closeSenderProcess()


