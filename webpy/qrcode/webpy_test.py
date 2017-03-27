# coding:utf-8
import web

urls = ( #命名空间
    '/','Index', #  /= 路径 index=类名
     "/(.*)",'example'
)


app =  web.application(urls, globals())
renter = web.template.render('templates')

class Index(object):
    def GET(self):
        return renter.index()
    def POST(self):
        i = web.input()
        print i


def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")
    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

app.notfound = notfound

class example:
    def GET(self):
       raise web.notfound()


if __name__ == '__main__':
     #web.application(urls, globals()).run()
    app.run()
