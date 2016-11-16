#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sudisk_download.py
#descrption			 
#author				pengyicheng
#date				20161109
#version			1.0
#python_version		2.6.6
#========================================================================


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
        import os
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
        import os
        file_num = 0
        for i in ['mtd0','mtd0_dll','mtd0_res']:
            filepath = os.getcwd() + os.path.sep + i
            file = i.split('_')
            
            destpath = '/' + '/'.join(file) + '/'
            #print 'dest = ' + destpath
            try:
                file = os.listdir(filepath)
                #print file
                for dir in file:
                    #print dir
                    recent = ['recent',str(file_num),'=1;',dir,destpath,dir]
                    #print recent
                    recent_string = ''.join(recent)
                   # recent_string = 'recent' + file_num + ';' + dir + ';' + filepath + dir 
                    print recent_string
                    fp.write(recent_string + '\r\n')
                    file_num += 1
            except:
                pass#print  'file in ' + filepath + ' is none'
    def mergeFile(self):
        import os 
        import shutil
        path = os.getcwd() + os.path.sep + self.MACHINE_MODEL# + os.path.sep + self.SUBDIR
       # if os.path.isdir(path):
       #     shutil.rmtree(self.SUBDIR)
        if os.path.isdir(path):
           # os.mkdir(self.MACHINE_MODEL)
            shutil.rmtree(path)
        os.mkdir(path)

        destpath = os.getcwd() + os.path.sep + self.MACHINE_MODEL + os.path.sep +  self.SUBDIR
        if os.path.isdir(destpath):
            shutil.rmtree(destpath)
       # os.mkdir(self.SUBDIR)
        os.mkdir(destpath)
        shutil.copy('config.ini',destpath)
        for i in ['mtd0','mtd0_dll','mtd0_res']:
            filepath = os.getcwd() + os.path.sep + i
           # destpath = os.getcwd() +os.path.sep + self.MACHINE_MODEL + os.path.sep + self.SUBDIR
           #try:
            file = os.listdir(filepath)
            print file
               # shutil.copytree(i,self.SUBDIR)
            for dir in file:
                subfile = filepath + os.path.sep + dir
                shutil.copy(subfile,destpath)

    def run(self):
        self.getSubDir()
        self.getMachineModel()
        file_num = self.getFileNum()
        print file_num
        fp = open('config.ini','w')
        fp.write('[History]' + "\r\n")
        fp.write('RecentCount=' + str(file_num) + "\r\n")
        self.getConfigFile(fp)
        fp.close()    
        self.mergeFile()   

def main():
    choice = InputModel()
    choice_model = pos_model(choice)
    choice_model.run()    

if __name__ == '__main__':
    main()



