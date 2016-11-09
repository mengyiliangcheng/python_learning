#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		scount_lines.py
#descrption			 
#author				pengyicheng
#date				20161109
#version			1.0
#python_version		2.6.6
#========================================================================

import sys
import os 
import codecs
#from _pyio import open

TotalCount = 0
FileType = ['.c','.h']
DescLineBegin = '//'
DescBlockBegin = r'/**'
DescBlockEnd = r'*/'
FileEncode = 'utf-8'

def main():
    Dir = os.getcwd()
    if len(sys.argv) >= 2:
        Dir = sys.argv[1]
    if os.path.exists(Dir) and os.path.isdir(Dir):
        print ('target directory is %s'% Dir)
        CountDir(Dir)
        print ('total code line is %d ' % TotalCount)
    else:
        print ('target should be a directory !')

#check filetype is setted FileType
def isFileType(file):
    for i in range(len(FileType)):
        if file.find(FileType[i]) > 0:
            return True
    return False

#find directory and subdirectory     
def CountDir(Dir):
    for file in os.listdir(Dir):
        #get file path:dir is directory,os.path.sep is separator('/' in linux;'\' in windows)
        absPath = Dir + os.path.sep + file
        #print absPath
        if os.path.exists(absPath):
            if os.path.isdir(absPath):
                CountDir(absPath)
            elif isFileType(absPath):
                try:
                    CountFile(absPath)
                except UnicodeDecodeError:
                    print('encode is different')

#count line in file
def CountFile(file):
    global TotalCount
    local_count = 0
    isInBlockNow = False
    #f = codecs.open(file,'r',FileEncode)
    f = open(file,'r')
    for line in f:
        #skip line beginning with '//'
        if line.find(DescLineBegin) == 0:
            continue
        #find beginning of block code 
        elif line.find(DescBlockBegin) >= 0:
            isInBlockNow = True
            local_count += 1
            continue
        #find endding of block code 
        elif line.find(DescBlockEnd) >= 0:
            isInBlockNow = False
            local_count -= 1
            continue
        #count numbers add one when not in block code
        elif isInBlockNow:
            continue
        else:
            local_count += 1 
    f.close()
    TotalCount += local_count
    print ('%s : %d' % (file,local_count))            

if __name__ == '__main__':
    main()
