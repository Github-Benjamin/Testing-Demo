import sys
sys.path.append('D:\python\daytest')
from utility.sql_helper import MysqlHelper


class   Admin(object):

    def __init__(self):
        self.__helper = MysqlHelper()

    def Get_one(self,id):
        sql = 'select * from testlogin where id=%s'
        params = (id,)
        return self.__helper.Get_One(sql,params)

    def CheckValueData(self,username,password):
        sql = 'select * from testlogin where username = %s and password = %s'
        params = (username,password,)
        return self.__helper.Get_One(sql,params)