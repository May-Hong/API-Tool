#! /usr/bin/env python
# -*- coding=utf-8 -*-
import sys
import urllib
import random
import xlrd
import re
import itertools
import string
import codecs
import time
import os
import datetime
import chardet

reload(sys)
sys.setdefaultencoding("utf-8")

def list2str(listi):
    stri = unicode(listi)
    stri = re.sub("\[u'|'\]","",stri)
    return stri


def url2str(listi):
    stri = unicode(listi)
    stri = re.sub("\|","/",stri)
    return stri

def match2replace(str):
    strs = str.lower()
    if strs.count("utf8urlencode(randomcn("):
        stro1 = re.sub("utf8urlencode\(randomcn\(|\)\)","",strs)
        stro2 = randomCN(stro1)
        stro = utf8urlencode(stro2)
        return stro
    elif strs.count("gbkurlencode(randomcn("):
        stro1 = re.sub("gbkurlencode\(randomcn\(|\)\)","",strs)
        stro2 = randomCN(stro1)
        stro = gbkurlencode(stro2)
        return stro
    elif strs.count("utf8urlencode(randomkr("):
        stro1 = re.sub("utf8urlencode\(randomkr\(|\)\)","",strs)
        stro2 = randomKR(stro1)
        stro = utf8urlencode(stro2)
        return stro
    elif strs.count("utf8urlencode(randomjp("):
        stro1 = re.sub("utf8urlencode\(randomjp\(|\)\)","",strs)
        stro2 = randomJP(stro1)
        stro = utf8urlencode(stro2)
        return stro
    elif strs.count("utf8urlencode(\""):
        stro = re.sub("utf8urlencode\(\"|\"\)","",strs)    
        stro = utf8urlencode(stro)
        return stro
    elif strs.count("gbkurlencode(\""):
        stro = re.sub("gbkurlencode\(\"|\"\)","",strs) 
        stro = gbkurlencode(stro)
        return stro
    elif strs.count("randomcn("):
        stro = re.sub("randomcn\(|\)","",strs)  
        stro = randomCN(stro)
        return stro
    elif strs.count("randomkr("):
        stro = re.sub("randomkr\(|\)","",strs)    
        stro = randomKR(stro)
        return stro
    elif strs.count("randomjp("):
        stro = re.sub("randomjp\(|\)","",strs)    
        stro = randomJP(stro)
        return stro
    elif strs.count("randomen("):
        stro = re.sub("randomen\(|\)","",strs)    
        stro = randomEN(stro)
        return stro
    else:
        return str

excelfile = sys.argv[1]+".xls"

if excelfile.count(".xls") < 0:
    sys.exit()

workbooks = xlrd.open_workbook(excelfile)
testurls = workbooks.sheet_names()

testcases = ""
for iurls in xrange(len(testurls)):  
    icasenums = 0
    sheets = workbooks.sheet_by_index(iurls)
    colnum = sheets.ncols
    urllist = []
    if sheets.nrows < 6:
        continue
    hoststr = sheets.row_values(0)[1]
    hostip = ""
    hosturl = ""

    if hoststr.count("|") > 0:
         hostip = hoststr.split("|")[1]
    else:
        hostip = hoststr
    notes = sheets.row_values(1)[1]
    urllist.append(hostip + url2str(testurls[iurls]))
    testcases = testcases+"url:"+list2str(urllist)+"|"
#testcases = testcases+"notes:"+notes+"|"

    for irownum in xrange(5,sheets.nrows):  
        methodlist = sheets.row_values(irownum)[1].split('|')
        testcases=testcases+"methodlist:"+list2str(methodlist)+"|"
        islogin = sheets.row_values(irownum)[2]
        testcases=testcases+"islogin:"+islogin+"|"
        username = sheets.row_values(irownum)[3]
        
        userpassword = sheets.row_values(irownum)[4]
        testcases=testcases+"username:"+username+"|"
        testcases=testcases+"userpassword:"+userpassword+"|"
        expectedResult = sheets.row_values(irownum)[5]
        testcases=testcases+"expectedResult:"+expectedResult+"|"
        casenotes = sheets.row_values(irownum)[6]
#testcases=testcases+"casenotes:"+casenotes+"|"
   
        for parai in xrange(7,colnum):
            tmpstrs = match2replace(str(sheets.cell(irownum,parai).value).strip())
            tmpstrs = re.sub('"','\\"',tmpstrs)
            tmpstrs = re.sub('\.0','',tmpstrs)
            
            if tmpstrs.lower()== "none":
                continue
            
            if str(sheets.row_values(irownum)[1]).upper().count('MULTIPART/FORM-DATA') <= 0:
                testcases=testcases+str(sheets.cell(4,parai).value).strip()+":"+tmpstrs+"|"
            else:
                testcases=testcases+str(sheets.cell(4,parai).value).strip()+":"+tmpstrs+"|"

print testcases
