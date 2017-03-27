#coding:utf-8
import urllib
import re

def open_url(pg):

    url = "http://www.pengfu.com/index_%s.html" % (pg)
    html = urllib.urlopen(url).read()
    #print html

    reg = re.compile(r'''<h1 class="dp-b"><a href=".*?" target="_blank">(.*?)</a>''')
    reg = re.findall(reg,html)

    reb = re.compile(r'''[jpg|gif]src="(.*?)">''')
    reb = re.findall(reb,html)

    rea = []

    for i in range(len(reb)):
       rea.append((reb[i][-3:]))

    download_url = zip(reg,reb,rea)

    return download_url
    #.decode('utf-8')      #.encode('gbk')

def download_file(name,url,format):
        urllib.urlretrieve(url,"image/%s.%s"%(name,format))

def select_page(one,two):

    for i in range(one,two):

        page_data = open_url(i)
        page_number =  len(page_data)

        for i in range(page_number):
            name = page_data[i][0]
            url =  page_data[i][1]
            format = page_data[i][2]
            print name,url,format
            #download_file(name,url,format)

select_page(2,5)
