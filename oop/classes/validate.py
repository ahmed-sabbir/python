
class Integer(object):
    """
    This class in an example of descriptor
    """
    def __init__(self,name) -> None:
        self.name=name

    def __get__(self, instance, cls) -> str:
        return instance.__dict__[self.name]

    def __set__(self, instance, value) -> None:
        if not isinstance (value, int):
            raise TypeError('Expected int')
        instance.__dict__[self.name]=value

class Float(object):
    """
    This class in an example of descriptor
    """
    def __init__(self,name) -> None:
        self.name=name
    
    def __get__(self, instance, cls) -> float:
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value) -> None:
        if not isinstance(value, float):
            raise TypeError("Expected float")
        instance.__dict__[self.name]=value

class Point(object):
    x = Integer('x')
    y = Integer('y')

    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        