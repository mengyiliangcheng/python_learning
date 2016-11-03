#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#title				sdaemon.py
#descrption			 
#author				pengyicheng
#date				20161102
#version			1.0
#python_version		2.6.6
#========================================================================

def create_daemon():
    import os, sys, time
    try:
        pid = os.fork()
        if pid > 0:             #parent process get pid > 0;child process get pid = 0
            sys.exit(0)         #parent process exit
    except OSError,error:
        print 'fork #1 failed:'
        sys.exit(1)

    os.chdir("/")               #decouple from parent environment
    os.setsid()
    os.umask(0)
    
    try:                        #do second fork
        pid = os.fork()
        if pid > 0 :
            print "daemon PID %d" %pid
            sys.exit(0)         #exit from second parent
    except OSError,error:
        print 'fork #2 failed'
        sys.exit(1)
    run()

def ping():
    import os
    os.system('ping www.baidu.com > /dev/nul')

def run():
    while True:
        import time, threading
        fp = open('/home/ping.log','a')
        fp.write('start time-------:%s\n'%time.ctime())
        fp.flush()
        t = threading.Thread(target = ping,args = ())
        t.start()
        time.sleep(3)
        fp.write("end of time ------:%s\n"%time.ctime())
        fp.flush()
    fp.close()

if __name__ == "__main__":
    create_daemon()

