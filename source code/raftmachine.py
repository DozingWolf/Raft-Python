# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'


from parameterloader import ParaLoder

class RaftMachine(object):

    print('Raft-Python Machine')

    def __init__(self):

        # 加载配置文件
        self.__raftNode = []
        self.__raftIP = []
        self.__raftHostName = []
        self.__raftHostDomain = []
        self.__raftPort = []
        # 
        self.__raftHeartBeat = 500  # unit is ms
        self.__raftTerm = 0
        self.__raftCharacter = 'Leader'

        self.__nodeParaIteam , self.__nodeQty = ParaLoder('../parameter/RMP.json').loadParameter()
        
        for self.__paraNodeNo, self.__paraIteam in enumerate(self.__nodeParaIteam):
            print('node no = ',self.__paraNodeNo,'iteam = ',self.__paraIteam)

    def RaftMachineInitial(self):
        
        # Raft算法初始化
        
        pass

    def RaftMachineCharacterSwitch(self):
        
        # Raft角色切换
        
        pass

    def getRaftMachineInfo(self):
        
        # 获取raft机器运行状态信息
        
        pass

    def endRaftMachine(self):
        
        # 关闭raft机器
        
        pass
