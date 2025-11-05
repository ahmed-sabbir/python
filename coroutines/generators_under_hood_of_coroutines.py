import types

@types.coroutine
def sock_recv(sock, maxsize):
    # yield statement makes a request to the event loop to recieve requests at a socket 
    # it pauses execution here
    # when event loop responds back to the request, the generator resumes execution 
    # or the coroutine will finish running if not resumed.
    result = yield ('recv', sock, maxsize) # Emitting and recieving a result
    return result

s=sock_recv('somesocket', 10000)
print(s.send(None))
try:
    print(s.send('Some data'))
except StopIteration as value:
    print(value.value)


async def greeting(name):
    return f"Hello, {name}!"

g = greeting("world")   
try:
    g.send(None)
except StopIteration as v:
    result =v.value
    print(result)


def cor():
    n=0
    while True:
        result = yield n # Emitting and recieving a result
        print('Got:', result)
        n+=1
c=cor()
print(c.__next__())
print(c.send('Hello'))
print(c.send('World'))

print('---')

def gen():
    n = 5 
    while n > 0:
        yield n
        n -=1
gg =gen()
print(gg.send(None))
print(gg.__next__())
print(gg.__next__())
print(gg.send(None))

