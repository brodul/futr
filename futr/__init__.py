from tornado import web, websocket, ioloop

cl = []


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)


def app_factory():
    app = web.Application([
        (r'/', IndexHandler),
        (r'/ws', SocketHandler),
    ])
    return app

if __name__ == '__main__':
    app = app_factory()
    app.listen(8888)
    ioloop.IOLoop.instance().start()
