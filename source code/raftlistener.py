# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine
from parameterloader import ParaLoder
from multiprocessing import Process, Queue
import time
import os
import socket
import pickle


class RaftListener(RaftMachine):
    def __init__(self):
        super().__init__(modelname = 'RMListener')
        self.__listenAddrList = super().getNeighborIPList()
        self.__listenerPort = super().getLocalhostPort()
        self.__listenerHostName = super().getLocalhostName()
        self.__listenerIP = super().getLocalhostIP()
        self.__listenLogger = super().getRMLogger()
        self.__rmDomain = super().getRMDomain()
        self.__mainProcessSID = 0
        self.__subProcessSID = 0
        print(self.__listenAddrList)
        # 
        self.__listenLogger.debug('RML is listening in %s:%s' % (self.__listenerIP, self.__listenerPort))
        self.__serverInfo = (self.__listenerIP,self.__listenerPort)
        #
        self.__listenLogger.debug(
            'Set socket parameter(socket.AF_INET,socket.SOCK_DGRAM)')
        self.__updSocketServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        # 
        self.__listenLogger.debug('Bind variable to socket server')
        self.__updSocketServer.bind(self.__serverInfo)
        

    def callLogicalCenter(self,logdata):

        def whenGetHeartbeatMessage(self):
            pass

        def whenGetVoteingInvitionMessage(self):
            pass

        def getRaftCharacter(self):
            # ask logical center
            self.__newRaftCharacter = ''
            return self.__newRaftCharacter
        def updateLocalRaftCharacter(self):
            self.__raftCharacter = self.getRaftCharacter()

    def forkListenerProcess(self):
        self.__mainProcessSID = os.getpid()
        self.__listenLogger.info('Listener pid = %s' % self.__mainProcessSID)
        def dataListerner(queue):
            self.__subProcessSID = os.getpid()
            self.__listenLogger.info('sub process pid = %s'%self.__subProcessSID)
            # self.__listenProcess = Process(target=dataListerner,args=(self.__rpcQueue,))
            # self.__listenProcess.start()
            while True:
                self.__listeningData, self.__listenAddr = self.__updSocketServer.recvfrom(1024)
                self.__listenLogger.debug(
                    'row message from %s is %s' % (self.__listenAddr, self.__listeningData))
                queue.put(self.__listeningData)
        self.__rpcQueue = Queue()
        self.__listenProcess = Process(
            target=dataListerner, args=(self.__rpcQueue,))
        self.__listenProcess.start()
        while True:
            self.__getDataFromListenerQueue = self.__rpcQueue.get(True)
            self.__listenLogger.debug(
                'Unpickly queue\'s data = %s' %self.__getDataFromListenerQueue)
            self.__picklyData = pickle.loads(self.__getDataFromListenerQueue)
            self.__listenLogger.debug('Data = %s'%self.__picklyData)

    def getListenerInfo(self):
        print('=========================================')
        print('==========Raft_Machine_Listener==========')
        print('=========================================')
        print('Raft Machine listener host name :', self.__listenerHostName)
        print('Raft Machine listener host IP :', self.__listenerIP)
        print('Raft Machine listener host port :', self.__listenerPort)
        print('Raft Machine listener main process sid :')
        print('Raft Machine listener listen process sid :')
        self.__listenLogger.info('This is a listener')
        self.__listenLogger.info('ip:%s , port:%s' % (self.__listenerIP , self.__listenerPort))

lsnInstance = RaftListener()
# lsnInstance.getRaftMachineInfo()
lsnInstance.getListenerInfo()
lsnInstance.forkListenerProcess()
