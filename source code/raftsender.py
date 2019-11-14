# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine
from parameterloader import ParaLoder
from multiprocessing import Process, Queue
import time,datetime
import os
import socket
import pickle

class RaftSender(RaftMachine):
    def __init__(self):
        super().__init__(modelname='RaftSender')
        self.__senderAddrList = super().getNeighborIPList()
        self.__senderPort = super().getLocalhostPort()
        self.__senderHostName = super().getLocalhostName()
        self.__senderIP = super().getLocalhostIP()
        self.__senderLogger = super().getRMLogger()
        self.__rmDomain = super().getRMDomain()
        self.__mainProcessSID = 0
        self.__subProcessSID = 0
        # 应该获取邻居的list，拼接一个tuple
        self.__serverInfo = (self.__senderIP, self.__senderPort)
        #
        self.__raftCharacter = 'New'
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
        self.__heartbeatMessage = [[self.__senderIP, self.__rmDomain, self.__senderHostName, self.__raftCharacter], {
            'term': 1, 'index': 1, 'Leader': 'RM.01', 'data': rpcdata}]
        return self.__heartbeatMessage
    
    def sendHeartbeatMessage(self):
        pass

    def forkSenderProcess(self,queue,serverlist):
        pass
