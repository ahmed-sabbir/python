def typed_property(property_name, expected_type):
    private_property_name='_' + property_name

    @property
    def prop(self): 
        '''
        name of the function(prop) doesn't matter
        '''
        return getattr(self, private_property_name)
    
    @prop.setter
    def prop(self,value):
        if not isinstance(value, expected_type):
            raise TypeError('Expected {}'.format(expected_type))
        setattr(self,private_property_name,value)

    return prop

Integer=lambda name: typed_property(name, int)
Float=lambda name: typed_property(name, float)
String=lambda name: typed_property(name, str)

class Holding(object):
    name=String('name')
    shares=Integer('shares')
    price=Float('price')

    def __init__(self, name, date, shares, price) -> None:
        self.name=name
        self.date=date
        self.shares=shares
        self.price=price
