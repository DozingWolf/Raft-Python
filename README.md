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