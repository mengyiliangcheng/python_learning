#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sudisk_download.py
#descrption			modify the module of directory,tidy up some comments and syntax  
#author				pengyicheng
#date				20161115
#version			1.1
#python_version		2.6.6
#========================================================================

import os

print'                                                              ' 
print'                   UDISK DOWNLOAD PYTHON 1.0                  '
print'       ===============================================        '
print'                          MACHINE MODEL                       '
print'                                                              '
print'            1.G810                     2.G3                   '
print'            3.G870                                            '
print'                                                              '
print'            e.EXIT                                            '
print'                                                              '
print'       ===============================================        '

def InputModel():
    while(True):
        choice = raw_input("PLEASE SELECT MACHINE MODEL: ")
        if not choice.isdigit():
            if choice.upper() == 'E':
                print 'THANKS FOR USE! BYE BYE ~'
                exit(0)
            else:
                print 'PLEASE CHOOSE RIGHT NUMBER'
        else:
            return choice

class pos_model:
    MACHINE_MODEL = 'G3'
    SELECT_NUM    = '1'
    SUBDIR        = '47'
    MODEL_TABLE = { '1':['G810','42'],'2':['G3','31'],
                    '3':['G870','4B']}

    def __init__(self,model_number):
        self.SELECT_NUM = str(model_number)
    def getSubDir(self):
        self.SUBDIR = self.MODEL_TABLE[self.SELECT_NUM ][1]
        print 'subdir is :' + self.SUBDIR    
    def getMachineModel(self):
        self.MACHINE_MODEL = self.MODEL_TABLE[self.SELECT_NUM][0]
        print 'model is :' + self.MACHINE_MODEL

    def getFileNum(self):
        file_num = 0
        for i in ['mtd0','mtd0_dll','mtd0_res']:
            filepath = os.getcwd() + os.path.sep + i
            try:
                file = os.listdir(filepath)
                file_num += len(file)
            except:
                print filepath + 'is not exist'
        return file_num

    def getConfigFile(self,fp):
        file_num = 0
        for i in ['mtd0','mtd0_dll','mtd0_res']:
            filepath = os.getcwd() + os.path.sep + i
            file = i.split('_')
            
            destpath = '/' + '/'.join(file) + '/'     #add '/' ;ex:'hello.c' convert to '/hello/c/'
            #destpath = os.path.sep + os.path.sep.join(file) + os.path.sep  #I think it's good through this function to get path;no,only '/' in linux
            try:
                file = os.listdir(filepath)
                for dir in file:
                    recent = ['recent',str(file_num),'=1;',dir,destpath,dir]  #format : recent[x]=1;file_name+destination path + file_name
                    recent_string = ''.join(recent)    #convert list to string
                   # print recent_string
                    fp.write(recent_string + '\r\n')   #write string to file
                    file_num += 1
            except:
                pass

    def mergeFile(self):
        import os 
        import shutil
        path = os.getcwd() + os.path.sep + self.MACHINE_MODEL       
        if os.path.isdir(path):     #if directory is exist ,delete it,and create a new directory
            shutil.rmtree(path)
        os.mkdir(path)
        #destination path : machine_model + machine_code 
        destpath = os.getcwd() + os.path.sep + self.MACHINE_MODEL + os.path.sep +  self.SUBDIR
        if os.path.isdir(destpath): #if directory is exist ,delete it,and create a new directory
            shutil.rmtree(destpath)
        os.mkdir(destpath)
        try:
            shutil.copy('config.ini',destpath)
        except:
            print 'remove config.ini error'

        abspath = os.getcwd()
        for i in ['mtd0','mtd0_dll','mtd0_res']:
            filepath = abspath + os.path.sep + i
           # print filepath + '   is current path' 
            file = os.listdir(filepath)
           # print file
               
          #  for dir in file:
          #      subfile = filepath + os.path.sep + dir
          #      shutil.copy(subfile,destpath)
            os.chdir(filepath)      #change current directory to subfile path
            for dir in file:
                shutil.copy(dir,destpath)
        os.chdir(abspath)

    def run(self):
        self.getSubDir()
        self.getMachineModel()
        file_num = self.getFileNum()
        print 'total file is :' + str(file_num)
        try:
            os.remove('config.ini')
        except:
            pass
        fp = open('config.ini','w')
        fp.write('[History]' + "\r\n")
        fp.write('RecentCount=' + str(file_num) + "\r\n")
        self.getConfigFile(fp)
        fp.close()    
        self.mergeFile()   
        print 'operate success !'

def main():
    choice = InputModel()
    choice_model = pos_model(choice)
    choice_model.run()    

if __name__ == '__main__':
    main()



