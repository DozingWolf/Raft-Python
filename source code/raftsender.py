# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine
from parameterloader import ParaLoder
from multiprocessing import Process, Queue
import time
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
        self.__mainProcessSID = 0
        self.__subProcessSID = 0
        
    def sendHeartbeatMessage(self):
        