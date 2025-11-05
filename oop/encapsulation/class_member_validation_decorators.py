
from typing import Any


class Typed(object):
    """
    This class in an example of descriptor
    A descriptor is an object that implements 
    the get, set and delete operations 
    """
    expected_type=object

    def __init__(self,name=None):
        # name is a optional argument as defined above
        self.name=name
    
    """ 
    The get and set machinery are descriptors too.
    The .(dot) is mapped to get & set machinery
    """
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        #breakpoint()
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected {} ".format(self.expected_type))
        instance.__dict__[self.name]=value

class Integer(Typed):
    expected_type=int

class Float(Typed):
    expected_type=float

class String(Typed):
    expected_type=str

def typed(cls):
    for key, value in vars(cls).items():
        if isinstance(value,Typed):
            value.name=key
    return cls

def validate(**kwargs):
    def decorate(cls):
        for name, val in kwargs.items():
            setattr(cls, name, val(name))
        return cls
    return decorate

#@typed
@validate(name=String, shares=Integer, price=Float)
class Holding(object):
    # name=String('name')
    # shares=Integer('shares')
    # price=Float('price')
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name not in {'name','date','shares','price'}:
            raise AttributeError('No attribute called: {}'.format(__name))
        super().__setattr__(__name,__value)

    def __init__(self,name,date,shares,price) -> None:
        self.name=name
        self.date=date
        self.shares=shares
        self.price=price
    
    @property
    def cost(self) -> float:
        return self.shares*self.price
    
class Spam(object):
    def __getattribute__(self, __name: str) -> Any:
        '''
        Captures all lookup, i.e. s.x
        '''
        print(f'Getting: {__name}')

class Foo(object):
    def __getattr__(self, name):
        '''
        Captures bad lookups.
        In other words:
        Failsafe. Only called for missing attributes
        '''
        print(f'Producing {name} out of thin air!')        