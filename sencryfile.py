#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		sencryfile.py
#descrption			 
#author				pengyicheng
#date				20161110
#version			1.0
#python_version		2.6.6
#========================================================================

import sys
import crypt
import base64

#support file type
FileType = ['.txt','.c']

#show usage
def usage():
    print ('[-] Usage: ./sencryfile.py <filename>  support file type: .txt .c')
    exit(0)

#encrypt char
def encry_char(char):
    chadd = ord(char) + 2
    chasc = chr(chadd)
    return chasc

#decryption 
def decry_char(char):
    chsub = ord(char) - 2
    chasc = chr(chsub)
    return chasc

#encrypt string
def encry_string(str,isEncry):
    convert_str = []
    for i in range(len(str)):
        ch = str[i]
        if isEncry:
            chasc = encry_char(ch)
        else:
            chasc = decry_char(ch)
        convert_str.append(chasc)
    string_line = ''.join(convert_str)
    return string_line

#use base64 to encrypt
def encry_string_base64(str,isEncry):
    if isEncry:
        string_line = base64.encodestring(str)
    else:
        string_line = base64.decodestring(str)
    return string_line

#encrypt file
def encry(file):
    f = open(file,'r')
    fb = open('encry_'+file,'w')
    for line in f:
        #string_line = encry_string(line,True)
        string_line = encry_string_base64(line,True)
        fb.write(string_line)
    f.close()
    fb.close()

#decrytion file
def de_encry(file):
    fc = open('decry_'+file,'w')
    fb = open('encry_'+file,'r')
    for line in fb:
        #string_line = encry_string(line,False)
        string_line = encry_string_base64(line,False)
        fc.write(string_line)
    fc.close()
    fb.close()
    print 'encrypt file success !'

#check file type
def isFileType(file):
    for i in range(len(FileType)):
        if file.find(FileType[i]) > 0:
            return True
    return False

#check file is exist
def isFileExist(file):
    import os
    dir = os.getcwd()
    path = dir + os.path.sep + file
    if os.path.exists(path):
        return True
    else:
        return False

def main():
    if len(sys.argv) < 2:
        usage()
    file = sys.argv[1]
    if not isFileType(file):
        usage()
    elif not isFileExist(file):
        print 'file is not exist !'
    else:
        encry(file)
        de_encry(file)

if __name__ == '__main__':
    main()


