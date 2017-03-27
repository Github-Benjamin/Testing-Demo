# _*_ coding:utf-8 _*_
#!/usr/bin/python
import socket

def send_api():
    udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp.connect(('172.31.21.61',2425))
    data = 'Hello, I am Benjamin'.decode('gbk').encode('utf-8')
    udp.send("1:106:Tester:51test:32:%s"%data)
    udp.close()
    
# for i in range(1,255):
#     send_api(i)

send_api()

# many_people 172.31.20.xx
# 51_wifi 172.31.30.xx
# little_people 192.30.21.xx
