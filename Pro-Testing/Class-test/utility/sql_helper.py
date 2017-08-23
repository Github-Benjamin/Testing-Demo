import MySQLdb

class   MysqlHelper(object):

    def __init__(self):
        pass

    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='question', charset='utf8')
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        cursor.execute(sql,params)
        data  =  cursor.fetchall()

        cursor.close()
        conn.close()
        return data

    def Get_One(self,sql,params):
        conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='question', charset='utf8')
        cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

        cursor.execute(sql,params)
        data  =  cursor.fetchone()

        cursor.close()
        conn.close()
        return data