import web

urls = (
    '/wx', 'Handle',
)

class Handle(object):
    def GET(self):
        return "hello, lisatttt !!!!!"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
