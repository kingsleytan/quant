#!/usr/bin/python3

def findObjectByKeyInList(l: list, k: any, v: any):
    """
    Find an object in a list of objects, filter by key
    Return None if not exist
    """

    return next((i for i in l if i[k] == v), None)

def getObjectsByKeyInList(l: list, k: any, v: any):
    """
    Get a list of objects that matches search requirement
    """
    
    return list(filter(lambda i: i[k] == v, l))