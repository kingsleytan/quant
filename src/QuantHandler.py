#!/usr/bin/python3

import os
import json
import atexit
from time import sleep
from copy import deepcopy
from threading import Thread, Timer
from quant.constants import (
    IP_NOT_FOUND,
    NOT_AUTHORIZED,
    PASSWORD_ERROR, 
    IP_MISMATCH)
from utils import Success, Panic, fileLogger
from utils.Common import findObjectByKeyInList

class QuantHandler(object):

    def __init__(self, configs: dict={}):
        self.instances = []
        for (k, v) in configs.items():
            setattr(self, k, v)
        
        fileLogger.info("Quant Handler created")
    
    def get(self):
        fileLogger.info("hello world")