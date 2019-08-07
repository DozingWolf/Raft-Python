# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

from parameterloader import ParaLoder
import logging
import logging.config
from bsddb3 import db
import bsddb3
import time,sys
import struct
import os,stat

class BerkeleyDB(object):
    def __init__(self,b_file):
        # load db parameter
        self.__dbParaIteam , self.__dbParaQty = ParaLoder('../parameter/BSDDBP.json').loadParameter()
        self.__logConfigFile = self.__dbParaIteam['BSDDB_PARAMETER']['BSDDB_LOG_CONFIG_FILE']
        self.__logHandleName = self.__dbParaIteam['BSDDB_PARAMETER']['BSDDB_LOG_HANDLE_NAME']
        self.bsddb_path = self.__dbParaIteam['BSDDB_PARAMETER']['BSDDB_STORAGE_PATH']
        # load log parameter
        logging.config.fileConfig(self.__logConfigFile)
        # create log handle
        self.__dbLogger = logging.getLogger(self.__logHandleName)
        # initial
        self.__os = os.name
        self.dbenv = db.DBEnv()
        
        if self.__os == 'posix':
            os.makedirs(name=self.bsddb_path,mode=0o666,exist_ok=True)
            self.__dbLogger.info('this is a posix system')
        else:
            # os windows
            self.__dbLogger.info('this is a windows system')
        self.bsddb_file = b_file
        self.dbenv.open(self.bsddb_path, db.DB_CREATE | db.DB_INIT_MPOOL)
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
            self.__dbLogger.info('insert data success!')
        except Exception as e:
            raise
            self.__dbLogger.warning('insert data failured!')
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
            self.__dbLogger.info('delete data success!')
        except Exception as e:
            raise
            self.__dbLogger.warning('insert data failured!')
    def closedb(self):
        self.dbinst.close()
        self.__dbLogger.info('db was closed')
    def closeenv(self):
        self.dbenv.close()
        self.__dbLogger.info('dbenv was closed')
    def syncdb(self):
        self.dbinst.sync()
        self.__dbLogger.info('db has been sync')
