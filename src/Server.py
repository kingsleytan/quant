import json
import signal
from time import time
from math import floor
from functools import partial
from tornado.ioloop import IOLoop
from tornado.web import Application, url
from tornado.httpserver import HTTPServer

from utils import fileLogger
from configs import server_configs
from routes import routes

import faulthandler
faulthandler.enable()

class QuantServer(Application):

    def __init__(self, **kwargs):
        kwargs["handlers"] = routes
        kwargs["debug"] = server_configs["debug"]
        super(QuantServer, self).__init__(**kwargs)

    def signal_handler(self, server, signal, frame):
        io_loop = IOLoop.instance()

        def stop_loop(deadline):
            now = time()
            if now < deadline:
                fileLogger.info("Shutting down in {}s".format(floor(deadline - now)))
                io_loop.add_timeout(now + 1, stop_loop, deadline)
            else:
                io_loop.stop()
                fileLogger.info("Server shutdown gracefully!")
        
        def shutdown():
            fileLogger.info("Stopping http server")
            server.stop()
            fileLogger.info("Shutting down in {}s".format(server_configs["wait_sec_shutdown"]))
            stop_loop(time() + server_configs["wait_sec_shutdown"])

        fileLogger.warning("Caught signal: {}".format(signal))
        io_loop.add_callback_from_signal(shutdown)

if __name__ == "__main__":
    fileLogger.info("Quant is running at {}:{}".format(server_configs["host"], server_configs["port"]))
    app = QuantServer()
    server = HTTPServer(app)
    server.listen(port=server_configs["port"])

    signal.signal(signal.SIGTERM, partial(app.signal_handler, server))
    signal.signal(signal.SIGINT, partial(app.signal_handler, server))

    IOLoop.instance().start()