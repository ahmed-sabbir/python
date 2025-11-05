from curses import echo
import types
from asyncechoserv import echo_handler

class Loop(object):
    @types.coroutine
    def sock_recv(self, sock, maxsize):
        result = yield ('I want to recieve from some socket 10000 bytes', sock, maxsize)
        return result

    @types.coroutine
    def sock_sendall(self, sock, data):
        result = yield ('sendall', sock, data)
        return result


if __name__ == '__main__':
    loop=Loop()
    coro=echo_handler('somsocket', loop)
    # the loop will drive the coroutine by doing send operations
    print(coro.send(None)) # recieves: ('I want to recieve on some socket 10000 bytes', 'somsocket', 10000)
    # the loop can set aside this coroutine for a while and do something else
    # but echo_handler will be blocked until it receives a result for the request
    print(coro.send(b'Some data'))
    print(coro.send(None))
    print(coro.send(b'More data'))
    # there is back and forth between the coroutine and whatever is driving the event loop

