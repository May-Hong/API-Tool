# -*- coding: utf-8 -*-
import os
import commands
from multiprocessing import Process
import codecs
import json
class Entity(object):
   def __init__(self, name,host="127.0.0.1",flag=0):
       self.name = name
       self.host = host
       self.flag = flag
   """   @staticmethod
   def get(name):
       result=[]
       for k,v in enumerate(name):
         cmd='python ./model/api.py data/'+v
         status,res = commands.getstatusoutput(cmd)
         result.append(res)
       return result"""
   @staticmethod
   def interface(name):
        list=[]
        sum=1
        number=1
        listfile=os.listdir(name)
        for line in listfile:
            if(not os.path.isfile(line) and line!="result"):
                dic = {'id':number,'pId':0,'name':line,'open':'false'}
                list.append(dic.copy())
                filelist=os.listdir("data/"+line)
                for file in filelist:
                    file = file.replace('-','/')
                    if file[-4:] == '.xls':
                       sum=1
                       dic = {'id':sum+number,'pId':number,'name':file[:-4]}
                       list.append(dic.copy())
                       sum=sum+1
                number=sum+number
        return list
   @staticmethod
   def excute(v,host):
#print host
        cmd='python ./model/api.py data/'+v+' '+host
        status,res = commands.getstatusoutput(cmd)
        fReport = codecs.open("data/result.tmp", "a", "utf-8")
        fReport.writelines(res+"\n")
        fReport.close

# @staticmethod
   def get(self,name,host="127.0.0.1",flag=0):
        jobs=[]
        if(flag == 1):
           for key,val in enumerate(host):
                for k,v in enumerate(name):
                   p=Process(target=self.excute,args=(v,val))
                   jobs.append(p)
                   p.start()
           for j in jobs:
               j.join()
        else:
            for k,v in enumerate(name):
                p=Process(target=self.excute,args=(v,host))
                jobs.append(p)
                p.start()
            for j in jobs:
                j.join()

   @staticmethod
   def testcase(v):
       cmd='python ./model/read.py data/'+v
       status,res = commands.getstatusoutput(cmd)
       fReport = codecs.open("data/read.tmp", "a")#, "utf-8")
       fReport.writelines(res+"\n")
       fReport.close

   def edit(self,name):
       jobs=[]
       for k,v in enumerate(name):
           p=Process(target=self.testcase,args=(v,))
           jobs.append(p)
           p.start()
       for j in jobs:
           j.join()

   def save(self,name):
       cmd="python ./model/save.py '"+name+"'"
#       print cmd
       status,res = commands.getstatusoutput(cmd)
       read_cmd='python ./model/read.py '+res
#print read_cmd
       status,result = commands.getstatusoutput(read_cmd)
#       print result
       return result
