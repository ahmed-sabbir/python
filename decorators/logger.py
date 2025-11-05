from functools import wraps

def logformat(logstatement):
    def logged(func): 
        '''
        Idea: Give me a function, I'll put logging
        around it.
        equivalent to calling: logcall.logged(mul) or logcall.logged(add)
        '''
        print('decorator invoked for ', func.__name__)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(logstatement.format(func=func))
            return func(*args,**kwargs)
        
        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper
    return logged

loggedjagged=logformat('Logger invoked from logcall module function: {func.__name__}')


def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):
            setattr(cls,key,loggedjagged(value))
    return cls
    
