def uppercase_decoration(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decoration
def say_hi():
    return 'helo there'

print(say_hi())