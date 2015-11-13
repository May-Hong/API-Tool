#! /usr/bin/env python
# -*- coding=utf-8 -*-
import sys
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import os

#reload(sys)
#sys.setdefaultencoding("utf-8")
#print sys.argv[1]
input=sys.argv[1].split('#')
url_list=input[0].split(':')[2]#.split('/')
url_list=url_list[2:].split('/')
excel="data/"+url_list[0]+"/"
#i=1
for k  in range(1,len(url_list)):
    excel=excel+url_list[k]+"-"
excel=excel[:-1]+".xls"
#+url_list[2]+".xls"
#print excel
rb=open_workbook(excel,formatting_info=False)
wb=copy(rb)
sheet=wb.get_sheet(0)
paras=input[1].split('*')
i=0
for para in paras:
    text=para.split('|')
    j=1
    for t in text:
        t=unicode(t, "utf-8")
        if(j==6):
            j=j+1
            continue
        sheet.write(4+i,j,t)
        j=j+1
    i=i+1
os.remove(excel)
wb.save(excel)
print excel[:-4]