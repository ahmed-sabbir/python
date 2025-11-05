class Holding(object):
    def __init__(self, name, date, shares, price) -> None:
        self.name= name
        self.date=date
        self.shares=shares
        self.price=price

    def __repr__(self) -> str:
        return 'Holding ({!r},{!r},{!r},{!r})'.format(self.name,self.date,self.shares,self.price)
    
    def __str__(self) -> str:
        return '{} shares of {} at {:0.2f}'.format(self.shares,self.name,self.price)
    
    def cost(self) -> float:
        return self.shares*self.price
    
    def sell(self, shares):
        self.shares -= shares