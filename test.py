#!/usr/bin/env python 

#File Name:test.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

import sys

while False:
    reply = raw_input("Enter text ")
    if reply == 'stop':
        break
    #check input number
    elif not reply.isdigit():
        print 'error input'
    else:
        print int(reply)**2
#print 'bye'* 8

while False:
    reply = raw_input("Enter text : ")
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print 'error input'    
    else:
        print num ** 2
#print 'bye' * 8




