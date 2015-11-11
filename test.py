#! /usr/bin/env python
#coding=utf-8
#eidt www.jbxue.com
#
import subprocess
import time
import os
def osping():
#调用系统的ping命令
    return1=os.popen('ping -w 1 10.69.20.124')
#    print return1
#t_f = os.popen ("ping 192.168.1.1")

#print return1.read()
    if return1.read:
        print 'ping os ping fail'
    else:
        print 'ping os ping ok'             
osping()
