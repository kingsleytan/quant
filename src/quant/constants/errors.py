#!/usr/bin/python3

def genError(code, message):
    return {
        "code": code,
        "message": message
    }

# custom error
IP_NOT_FOUND = genError(-1, "Device IP not found")

PASSWORD_ERROR = genError(1, "User name or password error")
NOT_AUTHORIZED = genError(2, "Not authorized to do this operation")
IP_MISMATCH = genError(55, "IP address not match")