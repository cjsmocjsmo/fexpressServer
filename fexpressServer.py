#!/usr/bin/python3

import os
import random
import hashlib
import re
import time
import uuid
import shutil
from urllib.parse import urlparse, parse_qs
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import util

fexp = util.FExpress()

define('server_port',
       default=6795,
       help='run on the given port',
       type=int,
       )


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/fexpress", MainHandler),
            (r"/fexpconnect", VPNConnectHandler),
            (r"/fexpdisconnect", VPNDisConnectHandler),
            (r"/fexpstatus", VPNStatusHandler),
        ]
        settings = dict(
            static_path="",
            template_path="",
            login_url="/",
            # cookie_secret = hashlib.sha512(str(random.randrange(100)).encode('utf-8')).hexdigest(),
            xsrf_cookies=False,
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class VPNConnectHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        CONN = fexp.connect()
        self.write(dict(conn=CONN))


class VPNDisConnectHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        DISCO = fexp.disconnect()
        self.write(dict(disco=DISCO))


class VPNStatusHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        STATUS = fexp.status()
        self.write(dict(status=STATUS))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.server_port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()


# class AllPlaylistsHandler():
# 	@tornado.gen.coroutine
# 	def getpls(self):
# 		try: return [(d['playlistname'], d['playlistid']) for d in db.playlists.find({}).sort([('playlistname', pymongo.ASCENDING)])]
# 		except KeyError: return []

# 	@tornado.web.authenticated
# 	@tornado.gen.coroutine
# 	def get(self):
# 		plname = yield self.getpls()
# 		plnamez = u"Please create a playlist"
# 		if plname != []: self.write(dict(plnames=plname))
# 		else: self.write(dict(plnames=plnamez))
