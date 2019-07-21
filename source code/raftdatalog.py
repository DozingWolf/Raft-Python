# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

class RaftDataLog(Base):
        ***
        raft存储日志
        ***

    def __init__():
        ***
        初始化日志类
        ***
        __raftLogList = []
        pass

    def RaftDataLogCheck():
        ***
        日志检查方法
        ***
        pass

    def RaftDataLogCommit():
        ***
        raft协议提交日志方法
        ***
        pass

    def RaftDataLogDelete():
        ***
        raft协议日志删除
        ***
        pass

    def RaftDataLogInitial():
        ***
        raft机器初次启动后开始获取日志初始化信息
        ***
        pass

    def RaftDataLogInitialRecever():
        ***
        raft机器初始化完成后开始追加日志
        ***
        pass

    def RaftDataLogWrite():
        ***
        raft日志落盘
        ***
        pass
