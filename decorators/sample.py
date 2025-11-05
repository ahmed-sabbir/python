from logger import logformat, logmethods

jaggedlogged=logformat('consumer override {func.__name__}')

@jaggedlogged
def add(x,y):
    '''
    Adds x and y
    Returns int
    '''
    print('Calling Add')
    return x+y

@jaggedlogged
def sub(x,y):
    print('Subtracting')
    return x-y
@jaggedlogged
def mul(x,y):
    return x*y

@logmethods
class Spam(object):
    def __init__(self, value) -> None:
        self.value=value

    def yow(self):
        print('Yow!')

    def grok(self):
        print('Grok!')