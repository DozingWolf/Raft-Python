# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine
from parameterloader import ParaLoder
from multiprocessing import Process, Queue
import time
import os


class RaftListener(RaftMachine):
    def __init__(self):
        super().__init__(modelname = 'RMListener')
        self.__listenAddrList = super().getNeighborIPList()
        self.__listenerPort = super().getLocalhostPort()
        self.__listenerHostName = super().getLocalhostName()
        self.__listenerIP = super().getLocalhostIP()
        self.__listenLogger = super().getRMLogger()
        self.__mainProcessSID = 0
        self.__subProcessSID = 0
        print(self.__listenAddrList)

    def callLogicalCenter(self,logdata):
        pass

    def forkListenerProcess(self,lport,lip):
        pass

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
lsnInstance.getRaftMachineInfo()
lsnInstance.getListenerInfo()
