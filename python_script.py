#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

#File Name:python_script.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161102
#Description:

from os.path import exists
from time import strftime
import os
import sys
import scolor
#print "script name:" ,sys.argv[0]
#for i in range(1,len(sys.argv)):
#    print "parameter",i,sys.argv[i]
#print len(sys.argv)

title = "demo.py"

#prints usage if not appropriate length of arguments are provided
def usage():
    scolor.print_warning("[-] Usage: ./python_script.py <filename>") 
    exit(0)

if len(sys.argv) < 2:
    scolor.print_fail("This script is used to create the file head for a new python script" )
    scolor.print_fail("You must bring a parameter as the prefix of the new script name. !" )
    usage()
    exit(3)

#input user information
elif sys.argv[1] == 'l':
    title = raw_input("Enter a title for your script:")
    title = title + '.py'
    title = title.lower()
    title = title.replace(' ','_')

    if exists(title):
        print "\nA script with this name is already exists"
        exit(1)

    descrpt = raw_input('Enter a description:')
    name = raw_input('Enter your name:')
    ver = raw_input('Enter the version number:')
#use default information
else:
    title = sys.argv[1] + '.py'
    title = title.replace(' ','_')
    
    if exists(title):
        print "\nA script with this name is already exists"
        exit(1)
    descrpt = " "
    name = "pengyicheng"
    ver = "1.0"

div = '===================================='

fp = open(title,'w')

date = strftime("%Y%m%d")

#write information to file
fp.write('#!/usr/bin/env python')
fp.write('\n# -*- coding: UTF-8 -*-')
fp.write('\n#script name\t\t' + title)
fp.write('\n#descrption\t\t\t' + descrpt)
fp.write('\n#author\t\t\t\t' + name)
fp.write('\n#date\t\t\t\t' + date)
fp.write('\n#version\t\t\t' + ver)
fp.write('\n#python_version\t\t2.6.6')
fp.write('\n#' + div * 2 + '\n')
fp.write('\n')
fp.write('\n')

fp.close()

#os.system("clear")

#call vim to edit
os.system("vim " + title)
exit(0)



