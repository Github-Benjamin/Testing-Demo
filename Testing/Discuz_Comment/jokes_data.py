#coding:utf-8

import  MySQLdb
import random

# db = web.database(dbn='mysql',host='127.0.0.1',port=3306,user='root',pw='',db='demo',charset='utf8')

db = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='demo',charset='utf8')
cursor = db.cursor()

def dd(s):
    dd = cursor.execute("select *  from joke where id = '%s'" % (s))
    results = cursor.fetchall()
    return results[0][1]

def joke_data():
    s = random.randint(569, 14731)
    # print dd(s)
    return dd(s)

# joke_data()
