#!/usr/bin/python3

from tornado.gen import coroutine
from tornado.concurrent import run_on_executor
from .BaseRequestHandler import BaseRequestHandler

from validator import *
from utils import decodeRequest, Success, Panic
from configs import default_get_response


class Quant(BaseRequestHandler):

    def initialize(self, handler):
        self.handler = handler

    @coroutine
    def get(self):
        result = yield self.handleGet()
        self.response(result)

    @coroutine
    def post(self):
        result = yield self.handlePost()
        self.response(result)

    @run_on_executor
    def handleGet(self):
        data = decodeRequest(self.request)
        return Success(200, data)

    @run_on_executor
    def handlePost(self):
        uri = self.request.uri
        data = decodeRequest(self.request)

        try:
            if uri == "/quant/login":
                loginSchema.validate(data)
                return self.handler.login(data)
            if uri == "/quant/logout":
                logoutSchema.validate(data)
                return self.handler.logout(data)
            if uri == "/quant/connected-users":
                return self.handler.getConnectedUsers()
        except Exception as err:
            return Panic(400, getattr(err, "args")[0])
        