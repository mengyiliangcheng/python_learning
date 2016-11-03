#!/usr/bin/env python 

#File Name:sfunction.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161101
#Description:

"""
def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

s1 = "spanm"
s2 = "jsilmn"
print intersect(s1,s2)


Tn = 0
Sn = []
n = 4
a = 4
slist = range(n)
print slist
for count in slist:
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn,
    if count < slist[-1]:
        print '+',
print '=',
#print ""
Sn = reduce(lambda x,y:x + y,Sn)
print Sn 
"""
def hello_world():
    print 'hello world'

def three_hellos():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    print "use internal"
else:
    print "import by others"

