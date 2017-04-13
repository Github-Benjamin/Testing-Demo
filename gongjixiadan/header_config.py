import time
import random

header_one ={
    'Host':'www.gongjixiadan.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Content-Type':'application/json',
    'X-Requested-With':'XMLHttpRequest',
    'Referer':'http://www.gongjixiadan.net/reglogin.html',
    'Cookie':'UserName=test02',
    'Connection':'keep-alive',
    'Content-Length': '0',
}

header_two ={
    'Host':'www.gongjixiadan.net',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.18 Mobile Safari/537.36',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Referer':'http://m.gongjixiadan.net/reglogin.html',
    'Cookie':'UserName=test02',
    'Connection':'keep-alive',
}


def login_time():
    login_time = '%s%s'%(int(time.time()),random.randint(100,999))
    return login_time
