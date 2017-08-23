# _*_ coding:utf-8 _*_
import requests
import re
import web

joke_data = []
db = web.database(dbn='mysql',host='127.0.0.1',port=3306,user='root',pw='',db='demo',charset='utf8')

def get_jokeurl(PageNum):
    url = 'http://www.jokeji.cn/list_%s.htm'%PageNum
    html = requests.get(url)

    html.encoding = ('gb2312')
    html = html.text
    # print html

    reg1 = re.compile(r'''<li><b><a href="(.*?)"target="_blank" >''')
    jokeurl =  re.findall(reg1,html)

    reg2 = re.compile(r'''<P>(.*?)</P>''')

    for i in range(len(jokeurl)):
        # len(jokeurl)
        # print jokeurl[i]

        mast_url = 'http://www.jokeji.cn/%s' % jokeurl[i]
        jokehtml = requests.get(mast_url)

        # print mast_url

        jokehtml.encoding = ('gb2312')
        jokehtml = jokehtml.text

        jokedata = re.findall(reg2, jokehtml)

        for i in range(len(jokedata)):
            #len(jokedata)
            j_data = jokedata[i][2:].replace('<BR>','\n')
            joke_data.append(j_data)

def insert_sql(joke_data):
    db.insert('joke',joke_data=joke_data)

for i in range(51,99):
    get_jokeurl(i)

for i in range(len(joke_data)):
    print joke_data[i]
    insert_sql(joke_data[i])

# insert_sql('你好' )
