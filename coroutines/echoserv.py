from curses import echo
from socket import *

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        print("Got connection from", addr)
        echo_handler(client)

def echo_handler(client):
    while True:
        data = client.recv(100000)
        if not data:
            break
        client.sendall(b'Got:' + data)
    print("Closing connection to", client.getpeername())
    client.close()

if __name__ == "__main__":
    echo_server(("", 25000))
        
