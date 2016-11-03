#!/usr/bin/env python 

#File Name:list.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

a = [1,2,3]
b = a[:]     #copy list a to b
print b
b[1] = 1
print 'b is '
print b
print 'a is '
print a
del b[1]
print 'after delete b[1]'
print b
print 'length of b :'
print len(b)





