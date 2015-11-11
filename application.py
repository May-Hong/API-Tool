#coding:utf-8
#author:the5fire

from urls import urls

import tornado.web
import os
SETTINGS = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
        )

application = tornado.web.Application(
        handlers = urls,
        **SETTINGS
        )
