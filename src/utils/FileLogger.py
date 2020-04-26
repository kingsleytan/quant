#!/usr/bin/python3

import os
import sys
import logging
from datetime import datetime
from pytz import timezone, utc

up, join = os.path.dirname, os.path.join

def customTime(*args):
    utc_dt = utc.localize(datetime.utcnow())
    my_tz = timezone("Asia/Kuala_Lumpur")
    return utc_dt.astimezone(my_tz)

def customTimeConverter(*args):
    timeNow = customTime()
    return timeNow.timetuple()

def setup_logger(name, filename):
    fmt = '%(asctime)s | %(levelname)-5s | %(filename)s:%(lineno)d - %(message)s'
    formatter = logging.Formatter(fmt=fmt, datefmt='%Y-%m-%d %H:%M:%S')
    formatter.converter = customTimeConverter
    handler = logging.FileHandler(filename, mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logDir = join(up(os.path.dirname(os.path.realpath(__file__))), "logs")
logFile = logDir + "/{}.txt".format(str(customTime()).split(".")[0].replace(" ", "-"))
fileLogger = setup_logger("Quant", logFile)