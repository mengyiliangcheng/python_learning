#!/usr/bin/env python 

#File Name:test.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

print "hello world"
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j ) and ( j != k ):
                print i,j,k


