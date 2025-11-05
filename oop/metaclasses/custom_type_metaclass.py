class custom_type(type):
    """
    This is a metaclass that creates new class definitions.
    Its a way to monitor what happens when a new class is created.
    """
    def __new__(meta, clsname, bases, methods):
        print('Creating: ', clsname)
        print('Bases: ', bases)
        print('Methods: ', methods)
        print('Meta: ', meta)
        return super().__new__(meta, clsname, bases, methods)
    
class Base(metaclass=custom_type):
    pass
        
    
class A(Base):
    def yow(self):
        pass    

# class B(Base):
#     def grok(self):
#         pass


def main():
    pass

if __name__ == '__main__':
    main()