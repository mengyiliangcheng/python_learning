#!/usr/bin/env python 

#File Name:ifelse.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

score = int (raw_input('input score:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print '%d belongs to %s' % (score,grade)



