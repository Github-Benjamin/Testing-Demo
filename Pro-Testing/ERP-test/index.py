#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web,json
from model.mysqldo import InsertMysql,SelectMysql,DelMysql

urls = (
    '/','Index',
    '/page/(.d*)', 'Page',
    '/jsonpage/(.d*)', 'JsonPage',
    '/post','Post',
    '/del','Del',
    '/edit','Edit',
)

render = web.template.render('templates')

class   Index(object):
    def GET(self):
        sql = 'SELECT id,pname,pguige,pchenbenjia,pxiaoshoujia,psctime,pyxtime,pjhtime from item LIMIT 0,5'
        data = SelectMysql(sql)
        if data:
            return render.index(data)
        else:
            return render.index(None)

class   Page(object):
    def GET(self,page):
        try:
            page = int(page)
            start = (page-1)*5
            end = page*5
            sql = 'SELECT * from item LIMIT %s,%s'%(end,5)
            data = SelectMysql(sql)
            return render.index(data)
        except:
            raise web.seeother('/')

class   JsonPage(object):
    def GET(self,page):
        try:
            page = int(page)
            start = (page-1)*5
            end = page*5
            sql = 'SELECT * from item LIMIT %s,%s'%(end,5)
            data = SelectMysql(sql)
            return json.dumps(data)
        except:
            raise web.seeother('/')

class   Post(object):
    def POST(self):
        data = web.input()
        params = []
        for i in range(len(data)/7):
            pname = data.get('pname%s'%i)
            pguige = data.get('pguige%s'%i)
            pchenbenjia = data.get('pchenbenjia%s'%i)
            pxiaoshoujia = data.get('pxiaoshoujia%s'%i)
            psctime = data.get('psctime%s'%i)
            pyxtime = data.get('pyxtime%s'%i)
            pjhtime = data.get('pjhtime%s'%i)
            datafile = (pname,pguige,pchenbenjia,pxiaoshoujia,psctime,pyxtime,pjhtime)
            params.append(datafile)
        sql = 'insert into item(id,pname,pguige,pchenbenjia,pxiaoshoujia,psctime,pyxtime,pjhtime) values(NULL,%s,%s,%s,%s,%s,%s,%s)'
        InsertMysql(sql,params)
        raise web.seeother('/')

class   Del(object):
    def GET(self):
        params = web.input().get('id')
        if  params:
            sql = 'delete from item where id=%s'%params
            try:
                DelMysql(sql)
                raise web.seeother('/')
            except:
                return 'Data error'
        else:
            return 'Data error'

class   Edit(object):
    def GET(self):
        params = web.input().get('id')
        sql = 'select * from item where id=%s'%params
        data = SelectMysql(sql)
        data = json.dumps(data)
        return data
    def POST(self):
        data = web.input()
        if  data:
            id,pname, pguige, pchenbenjia, pxiaoshoujia, psctime, pyxtime, pjhtime=data.get('id'),data.get('pname'),data.get('pguige'),data.get('pchenbenjia'),data.get('pxiaoshoujia'),data.get('psctime'),data.get('pyxtime'),data.get('pjhtime')
            try:
                sql = "update item  set pname='%s',pguige='%s',pchenbenjia='%s',pxiaoshoujia='%s',psctime='%s',pyxtime='%s',pjhtime='%s' where id=%s"%(pname, pguige, pchenbenjia, pxiaoshoujia, psctime, pyxtime, pjhtime,id)
                SelectMysql(sql)
                return json.dumps({'code':200})
            except:
                return 'Data error'

if __name__ == "__main__":
    web.application(urls, globals()).run()
