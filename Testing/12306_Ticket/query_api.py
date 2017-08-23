
#coding:utf-8
import top.api

def query_api(query_phone,query_data):
    req = top.api.AlibabaAliqinFcSmsNumQueryRequest()
    req.set_app_info(top.appinfo('{key_id}', '{key_md5}'))

    req.biz_id = None
    req.rec_num = "%s"%(query_phone)
    req.query_date = "%s"%(query_data)
    req.current_page = 1
    req.page_size = 10

    try:
        resp = req.getResponse()
        return resp
    except Exception, e:
        print '二二二'
        print (e)

def data_x(query_phone,query_data):
    resp = query_api(query_phone,query_data)
    items = []

    data_a = resp['alibaba_aliqin_fc_sms_num_query_response']['total_count']
    fc_partner_sms_detail_dto = resp['alibaba_aliqin_fc_sms_num_query_response']['values']['fc_partner_sms_detail_dto']

    for i in range(data_a):
        item = []
        item.append(fc_partner_sms_detail_dto[i]['extend']) #公共回传参数,消息返回
        item.append(fc_partner_sms_detail_dto[i]['rec_num']) #接受手机号
        item.append(fc_partner_sms_detail_dto[i]['sms_content'])  #短信内容
        item.append(fc_partner_sms_detail_dto[i]['sms_send_time']) #发送时间
        items.append(item)
    for i in items:
         print U'手机号:%s 发送时间:%s 短信内容:%s 返回参数:%s' % (i[1], i[3], i[2], i[0])

data_x({tel_number}, 20161227)
