#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sadd_head_for_python.py
#descrption			add head string for python file
#author				pengyicheng
#date				20161116
#version			1.0
#python_version		2.6.6
#========================================================================

#import argv from sys
import sys
import os
from time import strftime

DestPath = ''
argv = sys.argv
Extension = '.py'
Head_str = '#!/usr/bin/env python'

def usage():
    print '- [Usage] : python sadd_head_for_python.py <filepath>'

if len(argv) > 1:

    FilePath = sys.argv[1]
    if os.path.isdir(FilePath):
        DestPath = FilePath
    else:
        usage()
else:
    DestPath = os.getcwd()

print DestPath

def check_extension(file):
    if file.endswith(Extension):
        return True
    else:
        return False

dest_dir = '11_11_11'

def add_head(file):
    import shutil
    global dest_dir
    try:
        fp = open(file,'r')
    except:
        return     
    head_line = fp.readline()
    if head_line.find(Head_str) >= 0:
        #print 'ok'
        pass
    else:
        ftmp = open('new'+file,'w')
        fp.seek(0,0)
        data = fp.read()
        ftmp.write(Head_str + '\r\n' + data)
        ftmp.close()
        dest_path = os.getcwd() + os.path.sep + dest_dir
        if not os.path.exists(dest_path):
            dest_dir = strftime("%H_%M_%S")
            os.mkdir(dest_dir)
        
        shutil.copy('new'+file,dest_dir)
        os.remove('new' + file)
        #print 'no'
    fp.close()

orignal_path = os.getcwd()
os.chdir(DestPath)

for file in os.listdir(os.getcwd()):
    if check_extension(file):
        add_head(file)
        

print 'operate success!'
