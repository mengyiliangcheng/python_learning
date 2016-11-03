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
import logging.handlers
import logging
import os
import sys

class logger:
    
    logpath = $HOME
    logsize = 
    lognum = 3
    
    logname = os.path.join(logpath,sys.argv[0].split('/')[-1].split('.')[0])
    
    log = logging.getLogger()
    
    fmt = logging.Formatter('[%(asctime)s][%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    
    handle1 = logging.handlers.RotatingFileHandler(logname,maxBytes=logsize,backupCount=lognum)
    handle1.setFormatter(fmt)
    
    log.addHandler(handler1)
