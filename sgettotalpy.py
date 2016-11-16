#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sgettotalpy.py
#descrption			get python file in the current directory and merge all file
#                   to one python file
#author				pengyicheng
#date				20161111
#version			1.0
#python_version		2.6.6
#========================================================================

import os

FileType = ['.py']
DestFile = 'total.txt'

#check file type
def isFileType(file):
    for i in range(len(FileType)):
        if file.find(FileType[i]) + len(FileType[i]) == len(file):
            if file.find(FileType[i]) > 0:
                return True
    return False

#check files type
def isFilesType(files):
    file_filter = []
    for file in files:
        if isFileType(file):
            file_filter.append(file)
    return file_filter

#merge file to '.txt' file
def mergeFileToTxt(files):
    absPath = os.getcwd() + os.path.sep + DestFile
    if os.path.exists(absPath):
        os.remove(absPath)
        print 'clear old file'
    fp = open(DestFile,'w')
    for file in files:
        f = open(file,'r')
        fp.write('----'*8 + '\r\n')
        for line in f:
            fp.write(line + '\r\n')
    fp.close()
    print 'creat ' + DestFile + 'success'

#get python file
def getPythonFile():
    path = os.getcwd()
    files = os.listdir(path)
    file_filter = isFilesType(files)
    mergeFileToTxt(file_filter)
        

if __name__ == '__main__':
    getPythonFile()






