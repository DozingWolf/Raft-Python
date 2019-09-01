# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

class fatherClass(object):
    def __init__(self,name):
        self.__inner_variable = 'i am father class'
        self.__flag = 'Father!'
        self.__name = name

    def actionFunction(self):
        print(self.__inner_variable)
        print(self.__flag)
        print(self.__name)

    def getInnerVariable(self):
        return self.__inner_variable

    def getFlag(self):
        return self.__flag

class sonClass(fatherClass):
    def __init__(self,sonname):
        super().__init__(name = sonname)

newInstance = sonClass('Luke')
newInstance.actionFunction()
newInstance_2 = sonClass('Fi')
newInstance_2.actionFunction()