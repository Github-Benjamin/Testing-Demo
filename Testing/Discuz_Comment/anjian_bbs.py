# _*_ coding:utf-8 _*_
import random
import sys
import time

import requests

import joke_data

reload(sys)
sys.setdefaultencoding('utf-8')


def hf(s,joke_data):
    header = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'177',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'pgv_pvid=7516873208; ASP.NET_SessionId=bnjs3nap1nbfs1auqyykof5y; __qc_wId=295; forumpageid=1; AJSTAT_ok_pages=3; AJSTAT_ok_times=2; Hm_lvt_5d96b144d9b7632ed0ce359527dcc65d=1484708330,1484787872; Hm_lpvt_5d96b144d9b7632ed0ce359527dcc65d=1484789055; visitedforums=207,218; dnt=userid=3778068&password=EmMpabOI2ky72dTSHM8huXHzbF7DHDGQZfAzNWtuj0jg26cVwACwVg%3d%3d&tpp=0&ppp=0&pmsound=0&invisible=0&referer=showtopic.aspx%3ftopicid%3d625159%26page%3d8%26auctionpage%3d1%26forumpage%3d1&sigstatus=1&expires=43200&userinfotips=&visitedforums=218; lastactivity=onlinetime=198750814&oltime=197531823; lastposttitle=d41d8cd98f00b204e9800998ecf8427e; lastpostmessage=6537e99af2c2223642df9f70a0b5afca; lastolupdate=199167306; lastposttime=2017-01-19 09:31:42; dntusertips=userinfotips=%e7%a7%af%e5%88%86%3a9%2c%e7%94%a8%e6%88%b7%e7%bb%84%3a%e5%b0%8f%e5%ad%a6%e4%b8%80%e5%b9%b4%e7%ba%a7%2c%e9%b2%9c%e8%8a%b1%3a+0%e6%9c%b5%2c%e9%93%9c%e5%b8%81%3a+74%e4%b8%aa%2c%e9%93%b6%e5%b8%81%3a+160%e4%b8%aa%2c%e9%87%91%e5%b8%81%3a+0%e4%b8%aa; allowchangewidth=',
        'Host':'bbs.anjian.com',
        'Origin':'http://bbs.anjian.com',
        'Pragma':'no-cache',
        'Referer':'http://bbs.anjian.com/showtopic-625159-8.aspx?forumpage=1&typeid=-1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

    data = {
        'BTitle2':None,
        'postlayer':'-1',
        'postid':'0',
        'handlekey':None,
        'usesig':None,
        'postreplynotice':'on',
        'Char3':'%s\n\n{:5_129:}本帖子ID为：%s'%(joke_data, s),
        'replysubmit':None
    }

    # data = urllib.quote(data)

    r = requests.post("http://bbs.anjian.com/tools/ajax.aspx?topicid=%s&postid=0&postreplynotice=true&t=quickreply"%s,headers=header,data=data)
    r = r.text
    return r

a = 0
b = 0
for  i in range(3000):
    s = random.randint(32345, 699999)
    c = '%s' % joke_data.joke_data()
    r = '%s'%hf(s,c)
    s = '%s'%s
    if s in r:
        a = a+1
        print '帖子ID： %s  第  %s  次回复成功！'%(s,a)
        time.sleep(35)
    else:
        b = b+1
        print '帖子未找到，回帖失败: %s '%b
