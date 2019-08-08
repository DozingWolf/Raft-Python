# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import os
import time
import datetime
from multiprocessing import Process,Queue

def run_proc(name):
    print(datetime.datetime.now(),'this is pid=', os.getpid(), ' process!it will be sleep 5 seconds')
    time.sleep(5)
    print(datetime.datetime.now(),'child process was waken up')


if __name__ == "__main__":
    print(datetime.datetime.now(),'father process id =', os.getpid())
    prcs = Process(target=run_proc,args=('csy_test',))
    print(datetime.datetime.now(),'tather process will be sleep 10 seconds')
    print(datetime.datetime.now(),'child process will be start')
    prcs.start()
    time.sleep(10)
    prcs.join()
    print(datetime.datetime.now(),'child process will be end')
