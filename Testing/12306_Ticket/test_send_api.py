#coding:utf-8
import top.api

# app_key = {key_md5}

def send_api(send_phone,send_text):
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(top.appinfo('{ken_id}', '{key_md5}'))

    req.extend = "111222333"  #公共回传参数,消息返回
    req.sms_type = "normal"   #短信类型
    req.sms_free_sign_name = "我是白痴"   #短信签名
    req.sms_param = "{\'text\':\'%s\'}"%(send_text)   # 可选 JOSN
    req.rec_num = "send_phone"   #手机号
    req.sms_template_code = "SMS_36010240"    #短信模板内容

    print req.sms_param

    try:
        resp = req.getResponse()
        print (resp)
    except Exception, e:
        print (e)
