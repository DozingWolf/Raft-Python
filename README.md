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
    20190812
        1. 尝试编写一组可以持续使用测试的虚拟RPC发送器。
    20190817
        1. 发现对线程进程的理解存在欠缺，先尝试写一个线程和进程的demo。
    20190818
        1. 今天终于把多进程和socket的demo写出来了，之后有空的时候把进程和socket联合使用起来看一下。
    20190819
        1. 尝试写一个多进程和socket的联合demo。
        2. 完成联合demo的监听侧进程，明天尝试写发送侧进程。
        3. 现在完成的demo中，监听侧进程父进程负责接收监听UDP报文，通过queue发送至子进程进行处理。生产情况下考虑父进程处理，子进程监听。若出现异常情况下去，可以考虑较为方便的重启子进程而不影响父进程的事务。
        4. 发送侧进程考虑父进程接收外部数据提交或轮询某个值，fork出的子进程用于发送UDP报文。这样当发送器出现问题时不会影响状态轮询。
    20190820
        1. 完成联合demo的编写。
        2. 明天尝试把监听侧进程做一下修改。
        3. 同时考虑增加一定错误判断情况。
    20190825
        1. 写一个内部类和派生类的demo。
        2. 和NewOnePerson讨论后决定使用派生类。
        3. 设计思路：RM基类完成基础调用(包括但不限于读取配置，建立日志)，子类完成各类内部业务。
        4. 按照以上思路，需要修改raftmachine.py包，一些方法可以被移出来。需要在rm基类内添加传入的模块名参数(已添加)
    20190901
        1. 派生出rmlistener，设计思路：

        ```
            1. 派生自rm基类。
            2. 添加listener需要的变量。
            3. 创建多进程。
            4. 子进程开始监听所有接收到的信息。
            5. 子进程接收到的信息利用queue发送给父进程。
            6. 父进程根据基本逻辑判断，调用logicalcenter的各种方法。
            7. 派生的listener类最终需要被未来的logicalcenter进行调用。
            8. listener于logicalcenter使用queue进行数据交换。（确认？还是直接listener调用？）
        ```

        1. rm基类需要编写一个函数，用于获取本机ip。
        2. 遍历配置参数时改变思路，local参数不再记入列表。
        3. local参数直接记入local，供调用。
        4. 基类增加方法用于提供派生类调用参数。
    20191110
        1. AFK很久，重新开始编码。
        2. 编写了监听模块，已经可以建立监听。
        3. 下一步要编写一个发送者进行测试。或者考虑使用testcode中的发送者进行测试。
        4. 发现在监听模块、控制模块和发送模块之间的数据同步有点问题，现在可以用bsddb做共享数据的存储，但是模块间互相调用有点问题。看到有一些解决方案是使用进程间queue来实现，可以尝试以下。或者使用pipe管道来实现。尝试写一个demo来试试看。(http://www.py3study.com/Article/details/id/245.html)
        5. 新的想法，监听类与发送类可以写在不同py包内，通过调度py包来统一分配，这样就可以解决pipe必须在一个文件内的情况。或者调用同一个py包模块是否可行？有待尝试。
    20191114
        1. 编写sender模块。
        2. 发现sender和listener模块中，getRaftCharacter和updateLocalRaftCharacter两个方法好像可以抽象到raft machine基类中去。需要再仔细思考以下。
        3. 引发出的问题，raftmachine的character如何获取？基类提供方法和变量，再logicalcenter中实现character的变换好像是最合适的一种方案。
    20191115
        1. 编写sender模块。
        2. sender模块的发送需要仔细考虑，系统执行中，同时存在向某一个服务器发送的单播消息，也存在向所有服务器发送的广播消息。
        3. 此时按照demo中的写法执行效率不是最佳的，会造成有较多进程进行发送，不是很好。再次情况下，考虑将发送的心跳数据和目标地址信息拼成list或dict，再压入queue。udpSocketSender收到queue的消息后，for ip in enumerate(ip_list)解析发送地址，socket.sendto(message,ip)。
        4. 基于以上，sender.py第50行开始需要重写。
        5. 伪代码：
            生产者侧（数据准备器）
            queue_message = [message,ip_list]
            queue.put(queue_message)
            消费者侧（发送器）
            while true:
                getdata = queue.get(true)
                message = getdata[0]
                ip_list = getdate[1]
                for ip in enumerate(ip_list):
                    socket.sendto(message,ip)
                sleep(hb_interval)
    20191117
        1. sender模块中需要考虑发送者进程的关闭事务。
        2. 关闭时需要考虑该进程是否存在，否则会被弹出错误。
        3. sender模块会对外发送的数据不同，把压入队列的动作抽出来作为一个新的function设计。
        4. 抽取function到外部，重新写了sender模块。
        5. 实现发送者应对单独或多个发送目标的情况下，可以自动处理两种情况。
        6. 测试sender和listener完成，消息发送和接收成功。
        7. 至此，完成发送和接收的所有基础工作。下一步，准备实现raft分布式处理事务。