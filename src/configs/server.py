#!/usr/bin/python3

from os import environ

server_configs = {
    "host": "0.0.0.0",
    "port": 8083,
    "max_workers": 1000,
    "debug": True,
    "wait_sec_shutdown": 1
}

default_get_response = '''
    <html style="height: 100%; display: table; margin: auto;">
        <body style="height: 100%; display: table-cell; vertical-align: middle;">
            <h1 style="font-family: 'Raleway', sans-serif; font-weight: 100;">
                Quant Python API
            </h1>
        </body>
    </html>
'''