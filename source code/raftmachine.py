# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftdatalog import RaftDataLog


class RaftMachine(Base):

    print('Raft-Python Machine')

    def __init__():
        ***
        加载配置文件
        ***
        # demo variable
        __raftIP = '127.0.0.1'
        __raftHostName = 'Test.Machine.Node_01'
        __raftHostDomain = 'CSY.com'
        __raftNode = 1
        __raftPort = 7690
        __raftHeartBeat = 500  # unit is ms
        __raftTerm = 0
        __raftCharacter = 'Leader'
        pass

    def RaftMachineInitial():
        ***
        Raft算法初始化
        ***
        pass

    def RaftMachineCharacterSwitch():
        ***
        Raft角色切换
        ***
        pass

    def getRaftMachineInfo():
        ***
        获取raft机器运行状态信息
        ***
        pass

    def endRaftMachine():
        ***
        关闭raft机器
        ***
        pass
