
from typing import Any
import csv

class Typed(object):
    expected_type=object
    
    def __init__(self, name):
        self.name=name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TyperError("Expected {}".format(self.expected_type))
        instance.__dict__[self.name]=value

class Integer(Typed):
    expected_type=int

class Float(Typed):
    expected_type=float

class String(Typed):
    expected_type=str

def validate(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
           setattr(cls,key,value(key))
        return cls
    return decorate        

@validate(name=String, shares=Integer, price=Float)
class Holding(object):
    def __setattr__(self, __name: str, __value: Any):
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

class Portfolio(object):
    def __init__(self):
        self.holdings=[]

    def __repr__(self) -> list:
        return self.holdings.__repr__()
    
    '''
    Allows to forward the request to the inner list holdings
    Any access to an unknown attribute will be forwarded to this list.
    Refer to holding_functional.py for more usage of __getattr__
    '''
    def __getattr__(self, name):
        return getattr(self.holdings, name)

    @classmethod
    def from_csv(cls, filename):
        self=cls()
        with open(filename, 'r') as f:
            rows=csv.reader(f)
            header=next(rows)
            for row in rows:
                h=Holding(row[0],row[1],int(row[2]),float(row[3]))
                self.holdings.append(h)
        return self
        
    def total_cost(self):
        return sum(holding.shares*holding.price for holding in self.holdings)
    
    def current_value(self):
        ...

    def __len__(self):
        return len(self.holdings)
    
    def __getitem__(self, key):
        if isinstance(key,str):
            return [h for h in self.holdings if h.name==key]
        return self.holdings[key]
    
    def __iter__(self):
        return self.holdings.__iter__()


portfolio=''
    
if __name__ == '__main__':
    portfolio = Portfolio.from_csv('../../data/portfolio.csv')

