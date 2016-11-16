#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sfile.py
#descrption			 
#author				pengyicheng
#date				20161110
#version			1.0
#python_version		2.6.6
#========================================================================

import os

def listFile(filepath):
    try:
        pathDir = os.listdir(filepath) 
        for dir in pathDir:
            print dir
    except:
        print 'input is not a path'

def removeFile(file):
    if os.path.exists(file):
        os.remove(file)
        print 'file removed !'
    else:
        print 'file is not exist'

if __name__ == '__main__':
    path = os.getcwd()  + os.path.sep + 'encry_log.txt'
    listFile(path)
    removeFile(path)




