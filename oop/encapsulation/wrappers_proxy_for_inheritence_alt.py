class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):
        '''
        For developers.
        This method is used to control the string output of this class. Called when object is looked from the python interpreter
        e.g. 
        h=Holding('AA','2007-06-11',100,32.2)
        h
        '''
        return 'Holding({!r},{!r},{!r},{!r})'.format(self.name,self.date,self.shares,self.price)
    
    def __str__(self) -> str:
        '''
        For output.
        This method is used by print function, string conversion.
        e.g. 
        h=Holding('AA','2007-06-11',100,32.2)
        print(h)
        str(h)
        '''
        return '{} shares of {} at ${:0.2f}'.format(self.shares,self.name,self.price)

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

import csv

'''
Portfolio class's attribute holdings is list
'''
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


