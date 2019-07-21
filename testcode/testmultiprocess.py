# -*- coding: utf-8 -*-

__author__ = 'DozingWolf'

import os

print('process id:',os.getgid(),' is start')

pid = os.fork()