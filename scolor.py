#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

#File Name:scolor.py
#Author:pengyicheng
#Version:1.0
#Create Time:20161102
#Description:

class bcolors:
    HEADER = '\033[95m'     #pink 
    OKBLUE = '\033[94m'     #blue
    OKGREEN = '\033[92m'    #green
    WARNING = '\033[93m'    #light yellow
    FAIL = '\033[91m'       #red
    ENDC = '\033[0m'        #white
    BOLD = '\033[1m'        #bold
    UNDERLINE = '\033[4m'   #underline
if __name__ == '__main__':
    print bcolors.HEADER + "waring character " + bcolors.ENDC

def print_warning(str):
    print bcolors.WARNING + str + bcolors.ENDC    

def print_bold(str):
    print bcolors.BOLD + str + bcolors.ENDC

def print_header(str):
    print bcolors.HEADER + str + bcolors.ENDC

def print_fail(str):
    print bcolors.FAIL + str + bcolors.ENDC

def print_okblue(str):
    print bcolors.OKBLUE + str + bcolors.ENDC


