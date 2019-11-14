# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from raftmachine import RaftMachine

class RaftLogicalCenter(RaftMachine):
    def __init__(self):
        super().__init__(modelname = 'RaftLogicalCenter')
        self.__logicalCenterLogger = super().getRMLogger()
    def getLogicalCenterInfo(self):
        pass
