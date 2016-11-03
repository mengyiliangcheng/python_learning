#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

#File Name:sencrypt.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161102
#Description:

#encrypt the number
from sys import stdout
if __name__ == '__main':
    num = int(raw_input('input a number:\n'))
    mylist = []
    mylist.append(num % 10)
    mylist.append(num % 100 / 10)
    mylist.append(num % 1000 / 100)
    mylist.append(num / 1000)
    mylist.reverse()
    print mylist
    for i in range(4):
        mylist[i] += 5
    print mylist
     
#input a string ,save to file
if __name__ == '__main_':
    filename = raw_input('input a file name:\n')
    fp = open(filename,"w")
    ch = raw_input('input string:\n')
    while ch != '#':
        fp.write(ch)
        ch = raw_input('')
    fp.close()

#save file1 & file2 to file3
if __name__ == '__main__':
    import string
    fp = open('haha')
    a = fp.read()
    fp.close()

    fp = open('hah')
    b = fp.read()
    fp.close()

    fp = open('test.txt',"w")
    l = list (a + b)
    s = ''
    s = s.join(l)
    fp.write(s)
    fp.close()





