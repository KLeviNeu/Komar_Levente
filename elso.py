import socket
S_addr = input("Add meg a cimet: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((S_addr, 80))
sock.send(b"GET / HTTP1.1\r\nHost: " + bytes(S_addr, "UTF8") + b"\r\nConnection:close\r\n\r\n")
reply = sock.recv(100000000000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))
