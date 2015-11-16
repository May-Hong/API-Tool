#coding:utf-8

from handlers.index import MainHandler
from handlers.index import ResultHandler
from handlers.index import EditHandler
from handlers.index import SaveHandler
from handlers.index import ReportHandler
from tornado.web import StaticFileHandler

urls = [
    (r'/', MainHandler),
    (r'/result', ResultHandler),
    (r'/edit',EditHandler),
    (r'/save',SaveHandler),
    (r"/report/(\w+)", ReportHandler),
]