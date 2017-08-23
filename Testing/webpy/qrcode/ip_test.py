# coding:utf-8
import requests
import json

# items= []

def ipconfig(ip):
    html = requests.post('http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip).text
    html = json.loads(html)  # 转换
    item = []
    item.append(html['data']['country'])  #国家
    item.append(html['data']['region'])  #省份
    item.append(html['data']['city'])  #城市
    item.append(html['data']['isp'])  #运营商
    # items.append(item)#列表中写入列表
    items = u'%s%s%s%s' % (item[0], item[1], item[2], item[3])
    print items

ip = '182.140.245.49'

ipconfig(ip)
