from tornado import web, websocket, ioloop

cl = []


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('elm/index.html')


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print message


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
