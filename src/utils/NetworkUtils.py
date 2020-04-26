#!/usr/bin/python3

import urllib
import simplejson
from .Network import Panic

def parseEncodedString(encodedString: str):
    return urllib.parse.unquote(urllib.parse.unquote(encodedString))

def unloadRequestParams(data):
    res = {}
    for k, v in data.items():
        res[k] = data[k][0].decode(encoding="utf-8")
    return res

def decodeRequest(req) -> dict:
    method = req.method
    if method == "GET":
        data = unloadRequestParams(req.arguments)
        return data

    # other than get
    data = simplejson.loads(req.body) if str(req.body, "utf-8") != "" else {}
    return data