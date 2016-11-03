#!/usr/bin/env python
#print "hello \n world"
import string
import hello
#path = 'c:\share\test\new'
#print path
path1 = r'c:\share\test\new'  #close transferred meaning 
print path1

"""
s = raw_input('input a string:\n')
letters = 0
space = 0
numbers = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        numbers += 1
    else:
        others += 1
print 'char = %d,space = %d,number = %d,other = %d'\
         % (letters,space,numbers,others)
"""
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1
L2 = ['1','2','3','4','5']
s2 = ','.join(L2)
print s2
