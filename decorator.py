from functools import wraps

print('welcome to decorator!')

def line_controller(func):
    @wraps(func)
    def inner(*args):
        if args[1] > len(args[0].data):
            return args[0].data
        
        return func(*args)
    
    return inner
