#!/usr/bin/python3

from schema import Schema, And, Use, Optional

loginSchema = Schema({
    'ip': And(str, len),
    'port': And(Use(int)),
    'username': And(str, len),
    'password': And(str, len)
}, ignore_extra_keys=True)