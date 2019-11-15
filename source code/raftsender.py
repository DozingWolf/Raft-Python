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
        self.__senderLogger.debug(
            'raft machine\'s character is %s' % self.__raftCharacter)
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

    def forkSenderProcess(self,serverlist):
        self.__mainProcessSID = os.getpid()
        self.__senderLogger.info('Sender pid is %s'%self.__mainProcessSID)
        
        def udpSocketSender(queue):
            while True:
                self.__getInnerData = queue.get(True)
                self.__heartbeatIntervalTime = random.randint(401, 599)/1000
                print('RPC Sender will sleep %s seconds.' %
                      self.__heartbeatIntervalTime)
                time.sleep(self.__heartbeatIntervalTime)
                self.__updSocketLink.sendto(
                    self.__getInnerData, neighborserver)
                print('i have send a message to %s:%s' % neighborserver)
        self.__senderQueue = Queue()
        self.__sendProcess = Process(target=udpSocketSender, args=(
            self.__senderQueue, self.__neighborServerList,))
        self.__sendProcess.start()
        

