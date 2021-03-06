#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define, parse_command_line
from tornado_redis_session import SessionHandler

define('port', default=3000, help='run on the given port', type=int)
define('debug', default=False, help='run in debug mode')

class MainHandler(SessionHandler):
    def get(self):
        self.write('Redis Session Example\n')
        count = self.session.count.int
        self.write(f'Current Session Value:{count}\n')
        self.session.count = count + 1
        self.write(f'Current Session Value:{self.session.count.int}\n')

def main():
    parse_command_line()
    application = tornado.web.Application([(r'/', MainHandler)], cookie_secret='udxas-efasx-ase323fs-3efsxf3eFdes')
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
