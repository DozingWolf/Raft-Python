# -*- coding: utf-8 -*-
__author__ = 'DozingWolf'

import json
import os
import io
import time

class ParaLoder(object):

    #def __init__(self,p_path,*p_item):  # load multi variable
    def __init__(self,p_path):  # load all variable
        self.__parameterPath = p_path
        # self.__parameterIteam = p_item
        # self.resultDict = {}
        self.__pararesult = {}

    def loadParameter(self):

        parameter_dict = open(file=self.__parameterPath,mode='r')
        self.__pararesult = json.loads(parameter_dict.read())
        # multi parameter
        # for key,iteam in enumerate(self.__parameterIteam):
        #     self.resultDict.update({iteam:para_dict[iteam]})
        # self.resultDict.update(result=1)
        return self.__pararesult , len(self.__pararesult)