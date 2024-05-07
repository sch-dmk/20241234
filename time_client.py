import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('114.71.221.7', 9999))
print("Time: ", sock.recv(1024).decode())
sock.close()
