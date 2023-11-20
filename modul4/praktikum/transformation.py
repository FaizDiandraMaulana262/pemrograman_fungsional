import math

def translasi(function):
    def wrapper(x, y):
        res = function(x, y)
        return {"x" : res["x"] + 2 , "y" : res["y"] + (-3)}
    return wrapper

def rotasi(function):
    def wrapper(x, y):
        res = function(x, y)
        rotX = res["x"] * math.cos(math.radians(60)) - res["y"] * math.sin(math.radians(60))
        rotY = res["x"] * math.sin(math.radians(60)) + res["y"] * math.cos(math.radians(60))
        return {"x" : rotX, "y" : rotY}
    return wrapper

def dilatasi(function):
    def wrapper(x, y):
        res = function(x, y)
        return {"x" : res["x"] * 1.5, "y" : res["y"] * 2}
    return wrapper