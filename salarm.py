#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#script name		salarm.py
#descrption			 
#author				pengyicheng
#date				20161108
#version			1.0
#python_version		2.6.6
#========================================================================

import sys
import string 
#form time import sleep
import time

sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print "error"
    sys.exit(1)

try:
    minutes = int(sa[1])
except ValueError:
    print "error"
    sys.exit(1)

if minutes < 0:
    print "error"
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = "minute"
else:
    unit_word = "minutes"

try:
    if minutes > 0:
        print "sleeping for" + str(minutes) + unit_word
        time.sleep(seconds)
    print "wake up"
    for i in range(5):
       # print chr(7),
        time.sleep(1)
except KeyboardInterrupt:
    print "interrupt"
    sys.exit(1)



