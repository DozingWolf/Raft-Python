# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from json2para import ParaLoder
from hashcheck import ParaHashcheck
from logger import NewLogger
from bsddb3 import db
import bsddb3
import time,sys
import struct
import os,stat

'''
only support btree mode
'''
'''
需要考虑把数据类型转换模块抽象化成一个方法
'''
class BerkeleyDB(object):
    def __init__(self,b_path,b_file):
        # log para
        self.__dbLogpath = './log/'
        self.__logfilepath = 'BSDDB_LOG.log'
        # log handlers
        self.__basebsddbLogger = NewLogger(m_path=self.__dbLogpath, f_path=self.__logfilepath)
        self.__bsddbLogger = self.__basebsddbLogger.setting()
        # initial
        self.__os = os.name
        self.dbenv = db.DBEnv()
        self.bsddb_path = b_path
        if self.__os == 'posix':
            os.makedirs(name=self.bsddb_path,mode=0o666,exist_ok=True)
            self.__bsddbLogger.info('this is a posix system')
        else:
            # os windows
            self.__bsddbLogger.info('this is a windows system')
        self.bsddb_file = b_file
        self.dbenv.open(b_path,db.DB_CREATE | db.DB_INIT_MPOOL)
        self.dbinst = db.DB(self.dbenv)
        self.dbinst.open(b_file,db.DB_BTREE,db.DB_CREATE,mode=0o666)
        print(self.bsddb_path+self.bsddb_file)
        if self.__os == 'posix':
            # if os = posix, add chmod
            os.chmod(self.bsddb_path+'/'+self.bsddb_file,stat.S_IRWXU)
        else:
            # os windows
            pass
    def __pint2cint(self,indata):
        return struct.pack('i', indata)
    def insertdata(self,key,value):
        if isinstance(key, int):
            # print(key,'is int')
            inner_key = self.__pint2cint(indata=key)
        else:
            # print(key,'is str')
            inner_key = key.encode(encoding='utf-8')
        try:
            self.dbinst.put(inner_key,value)
            self.dbinst.sync()
            self.__bsddbLogger.info('insert data success!')
        except Exception as e:
            raise
            self.__bsddbLogger.warning('insert data failured!')
    def readalldata(self):
        result = self.dbinst.items()
        return result
    def readpairdate(self,key):
        if isinstance(key, int):
            inner_key = self.__pint2cint(indata=key)
        else:
            inner_key = key.encode(encoding='utf-8')
        result = self.dbinst.get(inner_key)
        return result
    def droppairdata(self,key):
        if isinstance(key, int):
            inner_key = self.__pint2cint(indata=key)
        else:
            inner_key = key.encode(encoding='utf-8')
        try:
            self.dbinst.delete(inner_key)
            self.dbinst.sync()
            self.__bsddbLogger.info('delete data success!')
        except Exception as e:
            raise
            self.__bsddbLogger.warning('insert data failured!')
    def closedb(self):
        self.dbinst.close()
    def closeenv(self):
        self.dbenv.close()
    def syncdb(self):
        self.dbinst.sync()
