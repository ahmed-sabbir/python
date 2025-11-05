class Holding(object):
    def __init__(self,name,date,shares,price) -> None:
        self.name=name
        self.date=date
        self.shares=shares
        self.price=price # s.price=32.2 uses the following func impl

    @property
    def price(self) -> float:
        return self._price #Hiding price in a private attribute
    
    @price.setter
    def price(self,newprice) -> None:
        if not isinstance(newprice,float):
            raise TypeError('Expected float')
        if newprice < 0 :
            raise ValueError('Must be >= 0')
        self._price=newprice

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, newShares) -> None:
        if not isinstance(newShares,int):
            raise TypeError('Expected int')
        self._shares=newShares
        
    def __repr__(self) -> str:
        return 'Holding ({!r},{!r},{!r},{!r})'.format(self.name,self.date,self.shares,self.price)
    
    def __str__(self) -> str:
        return '{} shares of {} at ${:0.2f}'.format(self.shares,self.name,self.price)
    
    @property
    def cost(self) -> float:
        return self.shares*self.price
    
    def sell(self,nShares) -> None:
        self.shares -=nShares
