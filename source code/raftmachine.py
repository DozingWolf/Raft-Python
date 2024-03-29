# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import logging.config
import logging
import socket
from parameterloader import ParaLoder

class RaftMachine(object):

    print('Raft-Python Machine')

    def __init__(self,modelname):

        # 1. load parameter file
        # all cluster parameter
        self.__raftNodeDomain = ''
        # localhost  parameter
        self.__raftNode = []
        self.__raftIP = []
        self.__raftHostName = []
        self.__raftPort = []
        # dynamic parameter
        self.__raftCharacter = 'Follower'
        self.__raftHeartBeat = 500  # unit is ms
        self.__raftTerm = 0
        # load parameters
        self.__nodeParaIteam , self.__nodeQty = ParaLoder('../parameter/RMP.json').loadParameter()
        # assignment parameters
        self.__raftNodeDomain = self.__nodeParaIteam['RaftMachine_Node_Domain']

        for self.__paraNodeNo, self.__paraIteam in enumerate(self.__nodeParaIteam['RaftMachine_List']):
            # print('node no = ', self.__paraNodeNo,'iteam = ',self.__paraIteam)
            if self.__paraIteam != 'RaftMachine_Node_Local':
                self.__raftIP.append(
                    self.__nodeParaIteam['RaftMachine_List'][self.__paraIteam]['RaftMachine_Node_IP'])
                self.__raftNode.append(
                    self.__paraNodeNo)
                self.__raftHostName.append(
                    self.__nodeParaIteam['RaftMachine_List'][self.__paraIteam]['RaftMachine_Node_Name'])
                self.__raftPort.append(
                    int(self.__nodeParaIteam['RaftMachine_List'][self.__paraIteam]['RaftMachine_Node_Port'])
                )
        # assign localhost variable
        self.__rmLocalhostName = self.__nodeParaIteam['RaftMachine_List'][
            'RaftMachine_Node_Local']['RaftMachine_Node_Name']
        self.__rmLocalhost = self.__nodeParaIteam['RaftMachine_List'][
            'RaftMachine_Node_Local']['RaftMachine_Node_IP']
        self.__rmLocalhostPort = self.__nodeParaIteam['RaftMachine_List'][
            'RaftMachine_Node_Local']['RaftMachine_Node_Port']

        
        # 2. initial log handle
        self.__rmLogConfigFile = self.__nodeParaIteam['RaftMachine_Log_Config']
        logging.config.fileConfig(self.__rmLogConfigFile)
        self.__rmLogHandleName = self.__raftHostName[0] + '_' + self.__raftIP[0] + '_' + modelname
        self.__rmLogger = logging.getLogger(self.__rmLogHandleName)
        

    def regetRaftMachineParameter(self):
        pass
    def getRMDomain(self):
        return self.__raftNodeDomain
    def getLocslCharacter(self):
        return self.__raftCharacter
    def getNeighborIPList(self):
        return self.__raftIP
    def getNeighborHostnameList(self):
        return self.__raftHostName
    def getLocalhostIP(self):
        return self.__rmLocalhost
    def getLocalhostName(self):
        return self.__rmLocalhostName
    def getLocalhostPort(self):
        return self.__rmLocalhostPort
    def getRMLogger(self):
        return self.__rmLogger
    def RaftMachineInitial(self):
        
        # Raft算法初始化
        
        pass

    def RaftMachineCharacterSwitch(self):
        
        # Raft角色切换
        
        pass

    def getRaftMachineInfo(self):
        
        # 获取raft机器运行状态信息
        self.__rmLogger.info('Test by DW')
        print('=========================================')
        print('============Raft_Machine_Info============')
        print('=========================================')
        print('Raft Machine host name :', self.__raftHostName[0])
        print('Raft Machine host ip :',self.__raftIP[0])
        print('Raft Machine host port :',self.__raftPort[0])
        print('Raft Machine host in cluster\'s no :',self.__raftNode[0])
        print('Raft Machine cluster domain name :',self.__raftNodeDomain)
        print('now localhost character is :',self.__raftCharacter)
        print('now RM term in localhost is :',self.__raftTerm)
        print('=========================================')

    def endRaftMachine(self):
        
        # 关闭raft机器
        
        pass
