import types

@types.coroutine
def sock_recv(sock, maxsize):
    result = yield('recv',sock, maxsize)
    return result