# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

class RaftDataLog(object):
        
        # raft存储日志
        

    def __init__(self):
        
        # 初始化日志类

        self.__raftLogList = []
        

    def RaftDataLogCheck(self):
        
        # 日志检查方法
        
        pass

    def RaftDataLogCommit(self):
        
        # raft协议提交日志方法
        
        pass

    def RaftDataLogDelete(self):
        
        # raft协议日志删除
        
        pass

    def RaftDataLogInitial(self):
        
        # raft机器初次启动后开始获取日志初始化信息
        
        pass

    def RaftDataLogInitialRecever(self):
        
        # raft机器初始化完成后开始追加日志
        
        pass

    def RaftDataLogWrite(self):
        
        # raft日志落盘
        
        pass
