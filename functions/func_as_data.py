import time


names=['james', 'asif', 'nawab', 'penny']
names.sort(key=lambda name: name.upper())
print(names)

def greeting(name):
    print("Hello ", name)


def after(seconds, func):
    time.sleep(seconds)
    func()


after(1, lambda : greeting('sam'))

def add(x,y):
    def do_add():
        print('Adding {} & {} -> {}'.format(x,y,x+y))
        return x+y
    return do_add

add(6,6) # doesn't invoke the do_add, just returns the function
a=add(3,3)
a()
b=add('hello','zz')
after(2,b)