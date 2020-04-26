#!/usr/bin/python3

from tornado.web import url
from configs import server_configs, quant_configs

from .BaseRequestHandler import BaseRequestHandler
from .Main import Main
from .Quant import Quant

from QuantHandler import QuantHandler

# Quant handler
handler = QuantHandler(
            configs=dict(quant_configs, 
            **{ "debug": server_configs["debug"] }))

routes = [
    url(r'/', Main),
    url(r'/quant/login', Quant, dict(handler=handler)),
    url(r'/quant/logout', Quant, dict(handler=handler)),
    url(r'/quant/connected-users', Quant, dict(handler=handler)),
]