from socket import *
import argparse

s = socket(AF_INET, SOCK_STREAM)

parser = argparse.ArgumentParser()
parser.add_argument('--address','-s', default='localhost')
parser.add_argument('--port','-p', type=int, default=2500)
args = parser.parse_args()

BUFSIZE = 1024
s.connect((args.address, args.port))

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("Received message: %s" % data.decode())

s.close()