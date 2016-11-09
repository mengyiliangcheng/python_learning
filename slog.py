#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#title				slog.py
#descrption			 
#author				pengyicheng
#date				20161103
#version			1.0
#python_version		2.6.6
#========================================================================

from lxml import etree
#from lxml.etree
import logging.handlers
import logging
import os
import sys

class logger:
    
    logpath = '/home/pyc/'
    logsize = 3
    lognum = 3
    
    logname = os.path.join(logpath,sys.argv[0].split('/')[-1].split('.')[0])
    
    #initial logger
    log = logging.getLogger()
    
    #format logger
    fmt = logging.Formatter('[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    
    #output log to file
    handle1 = logging.handlers.RotatingFileHandler(logname,maxBytes=logsize,backupCount=lognum)
    handle1.setFormatter(fmt)
    
    #output log to screen
    handle2 = logging.StreamHandler(stream=sys.stdout)
    handle2.setFormatter(fmt)
    
    log.addHandler(handle1)
    log.addHandler(handle2)
    
    log.setLevel(logging.INFO)
    
    @classmethod
    def info(cls,msg):
        cls.log.info(msg)
        return

    @classmethod
    def warning(cls,msg):
        cls.log.warning(msg)
        return 

    @classmethod
    def error(cls,msg):
        cls.log.error(msg)
        return 
    
