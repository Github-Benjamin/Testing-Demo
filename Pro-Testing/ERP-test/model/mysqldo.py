import MySQLdb

def InsertMysql(sql,params):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='question', charset='utf8')
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.executemany(sql, params)
    cursor.close()
    conn.commit()
    conn.close()
    return  'Success'

def SelectMysql(sql):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='question', charset='utf8')
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return  data

def DelMysql(sql):
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='question', charset='utf8')
    cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()
    return  'Success'