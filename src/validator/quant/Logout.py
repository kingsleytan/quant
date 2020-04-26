#!/usr/bin/python3

from schema import Schema, And, Use, Optional

logoutSchema = Schema({
    'ip': And(str, len),
    'lUserID': And(Use(int))
}, ignore_extra_keys=True)