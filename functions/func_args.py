def func(*args, **kwargs):
    print(args)
    print(kwargs)

def funca(x, *, z):    
    print(x)
    print(z)

def funcb(a,b,c,d):
    print(a,b,c,d)


def add(x,y):
    return x+y

def add_wrapper(*args, **kwargs):
    print('Wrapping!')
    return add(*args,**kwargs)

# func()
# func(1,2,x=4,z='hello')
# funca(1,z=2)

# args=(1,2)
# kwargs={'c':3, 'd':4}
# funcb(*args,**kwargs)
# data=(1,2,3,4)
# funcb(*data)

print(add_wrapper(1,5))
