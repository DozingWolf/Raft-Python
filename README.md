# Raft-Python
利用python实现raft算法
## 尝试利用python实现raft
可能执行效率很低，见谅
## 文件结构
### design resources
    
    设计资料
    
### source code
    
    项目源码
    
### testcode
    
    项目进行中进行的测试源码

### parameter

    项目配置文件

### 。。。。。。

    待添加
    
## 组件使用

### BSDDB 后端持久化存储

## 使用通信方式

### socket UDP连接
### multiprocessing 多进程
### multithreaded 多线程

## 开发日志
    20190802
        1. 确认使用配置项来确定raft集群的范围。
        2. 使用json文件来写配置项目。
    20190802 
        1. 调用原有的配置功能模块，发现现有的逻辑应该是一次性加载全部的配置文件到内存中。明天需要修改这个块逻辑，去除可变参数，直接加载全部配置项目。
    20190803
        1. 对配置加载包的改造完成。
        2. 对主程序中调用配置加载的程序还需要考虑，现在获取到的是一个dict字典，而代码在主程序中需要根据有多少服务器配置数量来创建变量。这个地方需要再考虑下如何做比较合适。
    20190805
        1. 变更了配置json文件的数据结构，把原本落在每台机器配置上的domain name提取到machine list之外进行。
        2. 完善了配置加载器。
        3. 编写了getinfo方法，用于暴露raft状态信息。
        4. 添加BSDDB组件。
        5. 看了下代码，感觉还是需要添加logging模块，之后重新研究一下logging的使用。
    20190807
        1. 添加BSDDB模块。
        2. 改造BSDDB模块内原有的logger
        3. logger使用logconfig
        4. 全局调用一份logconfig
        5. logconfig写入标准程序配置文件内
        6. 在raftmachine包内同步添加logger