# coding:utf-8
import web
import qrcode
import requests
import json
from PIL import Image
import time


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
    return items


def qc(info):

    # 创建qrcode对象
    qr = qrcode.QRCode(
        version = 1 ,#一个整数 范围是1-40 表示二维码的代销
        error_correction = qrcode.ERROR_CORRECT_Q, # 纠错/容错率 越高挡住的部分就越多
        box_size = 10 ,
        border = 4 , # 表示二维码距离图像外边框的距离
    )

    qr.add_data(
        '''BEGIN:VCARD\n
        VERSION:3.0\n
        FN:%s\n
        ORG:%s\n
        TITLE:%s\n
        ADR;work:%s\n
        TEL;work:%s\n
        EMAIL;work:%s\n
        URL:%s\n
        NOTE:%s\n
        END:VCARD'''%(info['name'],info['company'],info['title'],info['address'],info['mobile'],info['email'],info['url'],info['desc'])
    )

    #img是二维码
    img =qr.make_image()  #创建二维码图片
    img =img.convert('RGBA')
    img_w,img_h =img.size  #二维码图片的大小

    #logo是logo图片
    logo = Image.open("static/images/logo1.png") #打开logo图片
    #logo_w,logo_h =logo.size

    n = 4
    logo_w = int(img_w/n)
    logo_h = int(img_h/n)
    logo1_w,logo1_h = logo.size

    if logo1_w > logo_w:
        logo1_w =logo_w
    if logo1_h > logo_w:
        logo1_h = logo_h

    logo = logo.resize((logo1_w,logo1_h),Image.ANTIALIAS)
    w = int((img_w - logo1_w )/2)
    h = int((img_h - logo1_h )/2)
    img.paste(logo,(w,h),logo)

    # img.sava("static/1.png")
    # return "static/1.png"

    path = "static/imgcard/%s.jpg" %time.time()
    img.save(path)
    return path

urls = ( #命名空间
    '/','Index', #  /= 路径 index=类名
)

renter = web.template.render('templates')


class Index(object):
    def GET(self):
        ip = web.ctx.ip
        ip_info = ipconfig(ip)
        ipinfo = u"请求IP:%s 地址:%s" % (ip, ip_info)
        print ipinfo
        return renter.index()

    def POST(self):
        ip = web.ctx.ip
        ip_info = ipconfig(ip)
        ipinfo = u"请求IP:%s 地址:%s" % (ip, ip_info)
        print ipinfo
        i = web.input()
        return qc(i)
    #    return 'static/images/logo1.png'


if __name__ == '__main__':
    web.application(urls, globals()).run()
