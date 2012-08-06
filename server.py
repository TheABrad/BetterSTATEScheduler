#!/usr/bin/env python

import logging
from tornado import web
from tornado import httpserver
from tornado import ioloop
from tornado.options import define, options, parse_command_line
from app import routes, settings
parse_command_line()



application = web.Application(routes, **settings)

if __name__ == "__main__":
    server = httpserver.HTTPServer(application)
    server.listen(options.port)
    logging.info("listening on :%s" % options.port)
    ioloop.IOLoop.instance().start()
