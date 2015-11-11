#coding:utf-8

from handlers.index import MainHandler
from handlers.index import ResultHandler
from handlers.index import EditHandler
from handlers.index import SaveHandler
urls = [
    (r'/', MainHandler),
    (r'/result', ResultHandler),
    (r'/edit',EditHandler),
    (r'/save',SaveHandler)
]


