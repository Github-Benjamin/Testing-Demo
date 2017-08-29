import web

urls =     ('/test/(.d*)','Test',)
render = web.template.render('templates')

class   Test(object):
    def GET(self,page):
        page = int(page)
        start = (page - 1) * 5
        end = page * 5
        sql = 'SELECT * from item LIMIT %s,%s' % (start, 5)
        data = SelectMysql(sql)

        ret = {'data':data,'page':page}

        return render.test(ret)