# -*- coding: utf-8 -*-
__author__ = 'DozingWolf'

import json
import os
import io
import time

# rst = para_hashcheck(file_path, para_path)

class ParaLoder(object):

    def __init__(self,p_path,*p_item):
        self.__parameterPath = p_path
        self.__parameterIteam = p_item
        self.resultDict = {}

    def loadParameter(self):

        parameter_dict = open(file=self.__parameterPath,mode='r')
        para_dict = json.loads(parameter_dict.read())
        for key,iteam in enumerate(self.__parameterIteam):
            self.resultDict.update({iteam:para_dict[iteam]})
        self.resultDict.update(result=1)
        return self.resultDict