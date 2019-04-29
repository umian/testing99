import socket

mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysocket.connect(("www.netbsd.org",80))

mysocket.send(b"GET /HTTP/2.0\n\n")

res=mysocket.recv(1024)

while res != b"":
    print(res)
    res = mysocket.recv(1024)
    