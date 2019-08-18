# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import os
import datetime
from multiprocessing import Process, Queue

print('process id:',os.getpid(),' is start')

def osforkfunction():
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' %
            (os.getpid(), os.getppid()))
        for i in range(0,10):
            print(datetime.datetime.now())
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
        print('U must call me father')

def mprcfunction(prc_name,que_list):
    print('I am child process (%s) and my parent is %s.' %
          (os.getpid(), os.getppid()))
    for i in range(0, 100):
        # que_list.put('EXIT')
        data_output = prc_name + ' ' + \
            str(datetime.datetime.now()) + ' ' + str(os.getpid())
        print(data_output)
        que_list.put(data_output)
    que_list.put('EXIT')

def mprcfunction_2(prc_name,que_list):
    print('I am child process (%s) and my parent is %s.' %
          (os.getpid(), os.getppid()))
    print('my father is ',os.getppid())
    i = 0
    while True:
        i += 1
        data_input = que_list.get(True)
        print('no.',i,' another process \'s information is :', data_input)
        if data_input == 'EXIT':
            break
    

if __name__ == "__main__":
    print('U must call me father',os.getpid())
    prc_queue = Queue()
    subprocess = Process(target=mprcfunction, args=('test_prc_1', prc_queue,))
    subprocess_2 = Process(target=mprcfunction_2,
                           args=('test_prc_2', prc_queue,))
    subprocess.start()
    subprocess_2.start()
    # subprocess.join()
    # subprocess_2.join()
    # subprocess_2.terminate()
    print('End subprocess!!!')

