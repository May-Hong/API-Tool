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
import commands
import json

#excelfile = raw_input("Enter Excel filename:\n")
excelfile = sys.argv[1]+".xls"
#log = codecs.open("logs/"+str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))+".log", "w", "utf-8")
# fReport.writelines(self.createHeader())
if excelfile.count(".xls") < 0:
#    log.writelines(unicode(excelfile + " should be an Excel file, such as api.xls"))
#print unicode(excelfile + " should be an Excel file, such as api.xls")
    sys.exit()
reportfile = excelfile[5:-4]+".html"


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


def gbkurlencode(str):
    '''urlencode in gbk format
    '''
    return urllib.quote(str.decode(sys.stdin.encoding,'ignore').encode('gbk'))



def utf8urlencode(str):
    '''urlencode in utf-8 format
    '''
    return urllib.quote(str.decode(sys.stdin.encoding,'ignore').encode('utf8'))


def randomCN(num):
    '''随机生成中文字符
       @num: 随机生成字符串的长度
    '''
    if isinstance(num,int):
        nums = num
    elif unicode(num).isdecimal(): 
        nums = string.atoi(num)
    else:
        nums = 0
      
    randint = lambda : unichr(random.randint(0x4e00, 0x9fa5))
    strs = ''.join(randint() for i in xrange(nums))
    return strs


def randomKR(num):
    '''随机生成韩文字符
       @num: 随机生成字符串的长度
    '''
    if isinstance(num,int):
        nums = num
    elif unicode(num).isdecimal(): 
        nums = string.atoi(num)
    else:
        nums = 0
       
    randint = lambda : unichr(random.randint(0xAC00,0xD7AC))
    strs = ''.join(randint() for i in xrange(nums))
    return strs


def randomJP(num):
    '''随机生成日文字符
       @num: 随机生成字符串的长度
    '''
    if isinstance(num,int):
        nums = num
    elif unicode(num).isdecimal(): 
        nums = string.atoi(num)
    else:
        nums = 0
    
    randint = lambda : unichr(random.randint(0x30AC,0x30FE))
    strs = ''.join(randint() for i in xrange(nums))
    return strs


def randomEN(num):
    '''随机生成英文字符
       @num: 随机生成字符串的长度
    '''
    strs = ""   
    if isinstance(num,int):
        nums = num
    elif unicode(num).isdecimal(): 
        nums = string.atoi(num)
    else:
        nums = 0
  
    for i in xrange(nums):
        randint = random.randint(65,122)
        while randint<97 and randint>90:
            randint = random.randint(65,122)               
        strs = strs.join(['',chr(randint)]) 

    return strs


def randomRFE(num):
    '''随机生成圆框英文如Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ 
                                                              ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ
       @num: 随机生成字符串的长度
    '''
    if isinstance(num,int):
        nums = num
    elif unicode(num).isdecimal(): 
        nums = string.atoi(num)
    else:
        nums = 0
        
    randint = lambda : unichr(random.randint(0x24B6,0x24E9))
    strs = ''.join(randint() for i in xrange(num))
    
    return strs


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

def createHeader():
    header = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Miniblog API Test Result</title>
    <script type="text/javascript" src="src/jquery.js"></script>
    <script type="text/javascript" src="src/Expand_Collapse.js"></script>
    <link type="text/css" rel="stylesheet" href="src/skin.css">
</head>
<body>
    <h1 align="center">API Test Result</h1>
    <p align="right">
        <input type="submit" id="Expand ALL" value="展开用例" onclick="Expand_Header()"/>
        <input type="submit" id="Expand ALL" value="展开详情" onclick="Expand_All()"/>
        <input type="submit" id="Collapse ALL" value="收起所有" onclick="Collapse_All()"/>
    </p>
    <hr />
    <div class="URLID" id="URLID">
        <table width="100%" border="1" style="table-layout:fixed">
            
    """
    return header


def addAPIHead(apinums, url, funcdesc, paradesc):
    apihead = "\
    <tr class=\""+apinums+"""_apiheader">
      <td width="10%" scope="col" class="T_Header"><a href="#">"""+apinums+"""</a></td>
      <td width="10%" scope="col" class="C_Display">接口说明</td>
      <td width="30%" scope="col" class="L_Display">"""+url+"""<BR>"""+funcdesc+"""</td>
      <td width="10%" scope="col" class="C_Display">参数说明</td>
      <td width="50%" scope="col" class="L_Display">"""+str(paradesc)+"""</td>
    </tr>
    """
    
    return apihead


def addCaseHead(casenums, curls, casenotes,expected, isPass,time_connect,time_starttransfer,time_total):
    tempstri = ""
    if str(isPass) == "True":
        tempstri = str("<b><font color='Green'> PASS </font></b>")
    else:
        tempstri = str("<b><font color='Red'> FAIL </font></b>")
    timestr = str("time_connect: " +time_connect+"<BR>time_starttransfer: "+time_starttransfer+"<br>time_total: "+time_total)
    casehead ="""
    <tr class="case"""+casenums+"""_cheader" style="display:none;">
      <td>&nbsp;</th>
      <td class="T_Header"><a href="#">"""+casenums+"""</a></td>
      <td colspan="3" class="URL_Details">"""+curls+"<br>"+casenotes+"""</td>
    </tr>

    <tr class="case"""+casenums+"""_content" style="display:none;">
      <td>&nbsp;</th>
      <td class="C_Display">期望结果</td>
      <td class="L_Display">"""+expected+"""</td>
      <td class="runresult">"""+tempstri+"""</td>
      <td class="LU_Display">"""+timestr+"""</td>
    </tr>  
    <tr class="case"""+casenums+"""_content" style="display:none;">
      <td>&nbsp;</th>
      <td class="C_Display">运行结果</td>
      <td colspan="3" class="L_Display">"""
    return casehead
  
def addCaseEnd():  
    caseend = """</td>
    </tr>
    """
    return caseend


def  addSummary(total, passnum, failnum):
    temps = "Total: <b>%s</b>  Pass: <b><font color='Green'>%s</font></b>  Fail: <b><font color='Red'>%s</font></b>" %(total, passnum, failnum)
    summary = """
    <tr >
      <td colspan="2" class="C_Display">结果统计</td>
      <td class="C_Display">"""+temps+"""</td>
      <td class="C_Display">运行时间</td>
      <td class="C_Display">"""+str(datetime.datetime.now()).split('.')[0]+"""</td>
    </tr>
    """
    return summary


def  closeFile():
    closefile = """
      </table>
  <hr />
</div>
</body>
</html>
    """
    return closefile
       
workbooks = xlrd.open_workbook(excelfile)
commands.getstatusoutput('mkdir data/result/'+sys.argv[2])
#cp -r src 10.75.14.153/
commands.getstatusoutput('cp -r data/result/src data/result/'+sys.argv[2])
fReport = codecs.open("data/result/"+sys.argv[2]+"/"+reportfile.split('/')[1], "w", "utf-8")
#workbooks = xlrd.open_workbook('monitor.xls')
#workbooks = xlrd.open_workbook('list.xls')
#fReport = codecs.open('Test004.html', "w", "utf-8")
fReport.writelines(createHeader())

testurls = workbooks.sheet_names()
curllist = []
passNum = 0
failnum = 0

for iurls in xrange(len(testurls)):  
    icasenums = 0
    sheets = workbooks.sheet_by_index(iurls)
    colnum = sheets.ncols
    urllist = []
    if sheets.nrows < 6:
#log.writelines("Excel %s Sheet 格式不正确" % (str(testurls[iurls])))
# print "Excel %s Sheet 格式不正确" % (str(testurls[iurls]))
        continue
    hoststr = sheets.row_values(0)[1]
    hostip = ""
    hosturl = ""
    if sys.argv[2]!="127.0.0.1":#oststr.count("|") > 0 :
        hostip = 'http://'+sys.argv[2]#oststr.split("|")[0]
        if hoststr.count("|") > 0:
           appkey =hoststr.split("|")[0]
           hosturl = hoststr.split("|")[1]
           if(hosturl[7:].count("/")>0):
               head ='curl -H "Host:%s" ' %hosturl[7:].split("/")[0]+' -H "%s" ' %appkey
               hostip = hostip+'/%s' %hosturl[7:].split("/")[1]
           else:
               head ='curl -H "Host:%s" ' %hosturl[7:]+' -H "%s" ' %appkey
        else:
           hosturl = hoststr[7:]#.split("|")[1]
           if(hosturl.count("/")>0):
               head = 'curl -H "Host:%s" ' %hosturl.split("/")[0]
               hostip = hostip + '/%s' %hosturl.split("/")[1]
           else:
                head = 'curl -H "Host:%s" ' %hosturl
    else:
#     hostip = hoststr
        if hoststr.count("|") > 0:
           appkey = hoststr.split("|")[0]
           hostip = hoststr.split("|")[1]
           head = 'curl -H "%s" ' %appkey
        else:
           hostip = hoststr
           head = 'curl '
    notes = sheets.row_values(1)[1]
    parasinfo= sheets.row_values(2)[1]
    helpnotes = sheets.row_values(3)[1]
    #hosts = map(lambda x: x.strip(), hosts)
    #hosturl = map(lambda x: x.strip(), url2str(testurls[iurls]))
    #urllist.append(hosts + hosturl)

    if hostip[-1] == '/':
        hostip = hostip
    else:
        hostip = hostip + '/'
    urllist.append(hostip + url2str(testurls[iurls]))
    
    fReport.writelines(addAPIHead(str(iurls+1), list2str(urllist), notes, parasinfo))
       
    for irownum in xrange(5,sheets.nrows):
        time_connect = ''  
        time_starttransfer = ''
        time_total = ''
        
        formatlist = str(sheets.row_values(irownum)[0]).lower().split('|')
        methodlist = sheets.row_values(irownum)[1].split('|')
        islogin = sheets.row_values(irownum)[2]
        userinfo = sheets.row_values(irownum)[3] + ':' + sheets.row_values(irownum)[4]
        expectedResult = sheets.row_values(irownum)[5]
        explists = expectedResult.split('|')
        casenotes = sheets.row_values(irownum)[6]
 
        paraslist = []
        paras = ''
   
        for parai in xrange(7,colnum):
            tmpstrs = match2replace(str(sheets.cell(irownum,parai).value).strip())
            tmpstrs = re.sub('"','\\"',tmpstrs)
            tmpstrs = re.sub('\.0','',tmpstrs)
            
            if tmpstrs.lower()== "none":
                continue
            
            if str(sheets.row_values(irownum)[1]).upper().count('MULTIPART/FORM-DATA') <= 0:
                paras = paras.join(['',str(sheets.cell(4,parai).value).strip() + '=' + tmpstrs + '&'])
            else:
                paras = paras.join(['', '-F \"' + str(sheets.cell(4,parai).value).strip() + '=' + tmpstrs + '\" '])

        if len(paras) > 1 and paras[-1] == "&" :
            paras = paras[:-1]
        paraslist.append(paras)   
        urls = list(itertools.product(methodlist,urllist,formatlist,paraslist))

        for urlsi in xrange(len(urls)):
            curlCMD = ''
            RsText = []
            method = urls[urlsi][0].upper()
            url = urls[urlsi][1]
            format = urls[urlsi][2]
            paras = urls[urlsi][3]
            
            
            if str(islogin).upper() == 'YES': 
                if method == "GET":
                    curlCMD = head+'-u "%s" "%s%s?%s"' %(userinfo,url,format,paras)
                elif method == "POST":
                    curlCMD = head+'-u "%s" -d "%s" "%s%s"' %(userinfo,paras,url,format)
                elif method == "DELETE":
                    curlCMD = head+'%s -u "%s" "%s%s?%s"' %('-X DELETE',userinfo,url,format,paras)
                elif method == "POST/DELETE":
                    curlCMD = head+'-u "%s" -d "%s%s" "%s%s"' %(userinfo,paras,'&_method=DELETE',url,format)      
                elif method == "MULTIPART/FORM-DATA":
                    curlCMD = head+'-u "%s" %s "%s%s"' %(userinfo,paras,url,format)
                else:
                    curlCMD = "http请求错误，可能取值为：GET|POST|POST/DELETE|DELETE|multipart/form-data"  
            else:
                if method == "GET":
                    curlCMD = head+'"%s%s?%s"' %(url,format,paras)
                elif method == "POST":
                    curlCMD = head+'-d "%s" "%s%s"' %(paras,url,format)
                elif method == "DELETE":
                    curlCMD = head+'%s "%s%s?%s"' %('-X DELETE',url,format,paras)
                elif method == "POST/DELETE":
                    curlCMD = head+'-d "%s%s" "%s%s"' %(paras,'&_method=DELETE',url,format)      
                elif method == "MULTIPART/FORM-DATA":
                    curlCMD = head+'%s "%s%s"' %(paras,url,format)
                else:
                    curlCMD = "http请求错误，可能取值为：GET|POST|POST/DELETE|DELETE|multipart/form-data" 
#log.writelines(curlCMD)
#  print curlCMD
            curlCMDS = re.sub("curl","curl -s -w \"||%{time_connect}:%{time_starttransfer}:%{time_total}\"",curlCMD)
             
            RsText = os.popen(curlCMDS).readlines()  
            
            if len(RsText) < 1:
                time.sleep(2)
                RsText = os.popen(curlCMDS).readlines()        
            if len(RsText) > 0:
                for i in xrange(len(RsText)):
                    RsText[i] = re.sub('<','&lt;',RsText[i]) 
                    RsText[i] = re.sub('>','&gt;',RsText[i])  
                    if i == len(RsText)-1:
                        curl_times = RsText[-1].split("||")
                        RsText[i] = curl_times[0]
                        
                time_connect = curl_times[1].split(":")[0]   
                time_starttransfer = curl_times[1].split(":")[1] 
                time_total = curl_times[1].split(":")[2] 
            icasenums = icasenums+1
            
            isPass = True
#print json.load(explists[iexp]) 
            for iexp in xrange(len(explists)):
                for irs in xrange(len(RsText)):
#print json.dumps(json.loads(explists[iexp]))
                    if ((RsText[irs]).find(explists[iexp]) == -1):
                        isPass = False
                        break
            if isPass:
                passNum = passNum + 1
            else:
                failnum = failnum + 1
            
            RsTextstr = string.join(RsText)
            chardetsstr = chardet.detect(RsTextstr)['encoding']
            if chardetsstr == None:
                chardets = ""
            else:
                chardets = chardetsstr.lower()
            
            if chardets == 'gb2312':
                RsTextstr = unicode(RsTextstr,'GB2312','ignore').encode('utf-8','ignore') 
            elif chardets == 'big5': 
                RsTextstr = unicode(RsTextstr,'Big5','ignore').encode('utf-8','ignore') 
            elif chardets == 'ascii': 
                RsTextstr = RsTextstr
                #print RsTextstr
                #RsTextstr = re.sub("'","\\'",RsTextstr)
                #print RsTextstr
                #RsTextstr = "u'" + RsTextstr + "'"
                #RsTextstr = RsTextstr.encode('utf-8','ignore') 
            elif chardets == 'gbk': 
                RsTextstr = unicode(RsTextstr,'GBK','ignore').encode('utf-8','ignore') 
            elif chardets == 'euc-jp': 
                RsTextstr = unicode(RsTextstr,'EUC-JP','ignore').encode('utf-8','ignore')
            elif chardets == 'utf-8': 
                RsTextstr = RsTextstr.encode('utf-8','ignore')  
            else: 
                RsTextstr = RsTextstr
                    
            fReport.writelines(addCaseHead(str(iurls+1)+"-"+str(icasenums), curlCMD, casenotes,expectedResult, isPass,time_connect,time_starttransfer,time_total))
            fReport.writelines(RsTextstr)
            fReport.writelines(addCaseEnd())
# time.sleep(2)
        
fReport.writelines(addSummary(passNum+failnum, passNum, failnum)) 
fReport.writelines(closeFile())
fReport.close
#log.writelines("Command is completed, please open the following test report: "+reportfile)
#log.close
#print "Command is completed, please open the following test report: "+reportfile
excel = excelfile[5:-4].replace('-','/')
sumarry=sys.argv[2]+":"+excel+"|"+reportfile.split('/')[1]+"|"+str(passNum+failnum)+"|"+str(passNum)+"|"+str(failnum)
print sumarry
