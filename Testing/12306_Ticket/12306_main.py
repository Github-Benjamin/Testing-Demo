# coding:utf-8
import urllib
import ssl
import json
import send_api
import city_data
import datetime

city_begin = city_data.query_city('成都')
city_end = city_data.query_city('{Destination}')
begin_time = '2017-01-01'

print begin_time,city_begin,city_end

ssl._create_default_https_context = ssl._create_unverified_context   #解决12306 https证书错误的问题

def get_12306():

    starttime = datetime.datetime.now()  #开始访问时间

    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(begin_time,city_begin,city_end)
    request = urllib.urlopen(url).read()
    text = json.loads(request)

    endtime = datetime.datetime.now()  #结束访问时间

    # queryLeftNewDTO 数据
    # station_train_code 车次
    # start_time 出发时间
    # arrive_time 到达时间
    # lishi 历时
    # rw_num 软卧
    # wz_num 无座
    # yw_num 硬卧
    # yz_num 硬座

    for i in text['data']:
        text_queryLeftNewDTO = i['queryLeftNewDTO']
        #print text_queryLeftNewDTO
        text_tmp = u'''车次:%s 出发时间:%s 历时:%s 硬卧:%s 硬座:%s'''%(text_queryLeftNewDTO['station_train_code'],text_queryLeftNewDTO['start_time'],text_queryLeftNewDTO['lishi'],text_queryLeftNewDTO['yw_num'],text_queryLeftNewDTO['yz_num'])
        print text_tmp

    span = (endtime - starttime).total_seconds()
    print '车票查询请求时间%.2fs'%(span)

get_12306()
