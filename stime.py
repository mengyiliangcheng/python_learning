#!/usr/bin/env python 

#File Name:time.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

import time
import datetime

d = {1:'a',2:'b'}
for key,value in dict.items(d):
    print key,value
    time.sleep(1)     #stop one second 

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

time.sleep(1)

print (datetime.date.today().strftime('%d/%m/%Y'))
myBirthDay = datetime.date(1941,1,4)
print (myBirthDay.strftime('%d/%m/%Y'))

myBirthNextDay = myBirthDay + \
    datetime.timedelta(days=1)
print (myBirthNextDay.strftime('%d/%m/%Y'))

myFirstBirthDay = myBirthDay.replace(year=myBirthDay.year -1)
print (myFirstBirthDay.strftime('%d/%m/%Y'))
