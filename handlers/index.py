#coding:utf-8

import tornado.web
from model.entity import Entity
import commands

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        entity = Entity("data")
        self.render('show.html',result='',zNodes=entity.interface("data"))
        
class ResultHandler(tornado.web.RequestHandler):
    def post(self):
        flag=0
        paras = self.get_argument('paras')
        host=self.get_argument('host',default="127.0.0.1")
        if(paras[0]==","):
            paras = paras[1:]
        paras =paras.replace('/','-')
        paras =paras.replace('|','/')
        file=paras.split(',')
        if(host.count("\n")>0):
            host=host.split('\n')
            flag=1
        entity = Entity(file,host,flag)
        entity.get(file,host,flag)
        str=""
        str1=""
        value=[]
        key=[]
        res=open("data/result.tmp")
        for line in res.readlines():
            line=line.split(':')
            key.append(line[0])
            dic = {line[0]:line[1]}
            value.append(dic.copy())
        key=list(set(key))
        for k in key:
            str=k+":"
            for v in value:
                for (k1, v1) in v.items():
                    if(k1==k):
                        str=str+v1.strip()+","
# str=str[:-1]+";"
            str=str+";"
            str1=str1+str
# print str1
        res.close()
        commands.getstatusoutput("rm -rf data/result.tmp")
        self.write(str1)

class EditHandler(tornado.web.RequestHandler):
    def post(self):
        paras = self.get_argument('paras')
        if(paras[0]==","):
            paras = paras[1:]
        paras =paras.replace('/','-')
        paras =paras.replace('|','/')
        file=paras.split(',')
        entity = Entity(file)
        entity.edit(file)
        str=""
        res=open("data/read.tmp")
        for line in res.readlines():
            str=str+"*"+line
        res.close()
        commands.getstatusoutput("rm -rf data/read.tmp")
        self.write(str[1:])

class SaveHandler(tornado.web.RequestHandler):
    def post(self):
#  print self.get_argument('paras')
        paras = self.get_argument('paras').encode('utf-8')
# print paras
        entity = Entity(paras)
        str=entity.save(paras)
        self.write(str)
