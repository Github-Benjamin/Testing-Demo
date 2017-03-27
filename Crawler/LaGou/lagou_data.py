# coding:utf-8
import requests
import json

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8") #输出的内容UTF-8

items = []

def get_content(pn):#多页
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false"

    print pn

    data = {
        'first' : 'true',
        'pn' : pn ,
        'kd' : '测试'
        }

    html = requests.post(url,data).text # 获取网页内容
    html = json.loads(html) #转换

    for i in range(14):
        item = []
        item.append(html['content']['positionResult']['result'][i]['companyFullName'])  #公司名称
        item.append(html['content']['positionResult']['result'][i]['companySize'])  #公司规模
        item.append(html['content']['positionResult']['result'][i]['positionName']) #职称
        item.append(html['content']['positionResult']['result'][i]['salary']) #薪资
        item.append(html['content']['positionResult']['result'][i]['positionAdvantage']) #福利
        item.append(html['content']['positionResult']['result'][i]['workYear']) #工作年限
        items.append(item)#列表中写入列表
    return items

get_content(1)

def write():
    ID = 1 #声明一个变量,页数
    while ID <=1:
        get_content(ID) #多页,改变页数操作
        ID += 1
        for i in items:
            print (u"%s %s |职位:%s |薪资:%s |要求:%s |福利:%s \n"%(i[0],i[1],i[2],i[3],i[5],i[4]))

#调用
# a = write()
