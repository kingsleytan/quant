#!/usr/bin/python3

from tornado.gen import coroutine
from tornado.concurrent import run_on_executor
from .BaseRequestHandler import BaseRequestHandler

from utils import decodeRequest, Success
from configs import default_get_response

class Main(BaseRequestHandler):

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
        return default_get_response

    @run_on_executor
    def handlePost(self):
        data = decodeRequest(self.request)
        return Success(200, data)