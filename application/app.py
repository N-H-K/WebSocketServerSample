#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

##
# @file app.py
# @date 2017-03-26

import tornado.ioloop
import tornado.web
import tornado.websocket

clients = []

on_messaged = None

def send(message):
    for cl in clients:
        cl.write_message(message)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if self not in clients:
            clients.append(self)

    def on_message(self, message):
        print "recieved: %s" % message
        if on_messaged is not None:
            on_messaged(message)

    def on_close(self):
        if self in clients:
            clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('view.html')

class WebApiHandler(tornado.web.RequestHandler):
    def get(self, command):
        print command
        send(command)
        self.write('command: %s' % command )


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/api/v1/(?P<command>[^\/]+)", WebApiHandler),
    (r"/websocket", WebSocketHandler),
])

if __name__ == "__main__":
    print "listen web ui:    http://localhost:8080/"
    print "listen websocket: http://localhost:8080/websocket"
    print "listen we bapi:   http://localhost:8080/api/v1/[command]"
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()
