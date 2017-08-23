# coding:utf-8
from daytest import Admin

def Main():
    user = raw_input('username:')
    pwd = raw_input('password:')
    admin = Admin()
    if admin.CheckValueData(user,pwd):
        print 'Login success'
    else:
        print 'Login faild'

if __name__ == '__main__':
    Main()