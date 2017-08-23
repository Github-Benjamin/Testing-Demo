# -*- coding: utf-8 -*-
import requests
import re
import header_config
import time

username_list = []
reg = []

#username = 'test08'
def Register(username):
    r_url = 'http://www.gongjixiadan.net/xiadangongji/auth/opentype/reg?mail=%s@qq.com&username=%s&password=e10adc3949ba59abbe56e057f20f883e&logoutacc=&callback=jQuery172011389183566103545_%s&_=%s'%(username,username,header_config.login_time(),header_config.login_time())
    try:
        r_html = requests.post(url=r_url,headers=header_config.header_two).text
        Selfcode = re.findall(re.compile(r'"Selfcode":(.*?),'),r_html)[0]
        #print r_html
        if Selfcode != None:
             reg.append(Selfcode)
        else:
            print 'Register Failed!'
    except:
        print 'Register Failed'

def Login(username,Selfcode):
    login_url = 'http://www.gongjixiadan.net/xiadangongji/auth/login?username=%s&password=e10adc3949ba59abbe56e057f20f883e&callback=jQuery17209444932910811483_%s'%(username,header_config.login_time())
    try:
        login_html = requests.post(url=login_url,headers=header_config.header_one).text
        if 'token' in login_html:
            token = re.findall(re.compile(r'"token":"(.*?)"}'),login_html)[0]
        else:
            print 'login Failed'
    except:
        print 'Request url Failed One'

    JHM_url = 'http://www.gongjixiadan.net/xiadangongji/invitationcode/use?token=%s&code=%s&callback=jQuery1720184164045098139_%s'%(token,Selfcode,header_config.login_time())

    try:
        JHM_html = requests.post(url=JHM_url,headers=header_config.header_one).text
        if '"errcode":0' in JHM_html:
            pass
        else:
            print 'Do Failed'
    except:
        print 'Request url Failed Two'
a = 28
while True:
    for i in range(a,a+4):
        username = 'Benjamin00%s'%i
        time.sleep(0.3)
        username_list.append(username)
        Register(username)

    print username_list
    print reg

    for x in range(len(username_list)):
        for y in range(len(reg)):
            print username_list[x],reg[y]
            time.sleep(0.3)
            Login(username_list[x],reg[y])

    del username_list[:]
    del reg[:]
    a = a+4
    print a
    if a >24000:
        break
