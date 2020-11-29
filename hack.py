# write your code here
import socket
import argparse

client_socket = socket.socket()
parser = argparse.ArgumentParser()
parser.add_argument("hostname")
parser.add_argument("port")
parser.add_argument("message")
args = parser.parse_args()
print(args)

address = (args.hostname, args.port,)
client_socket.connect(address)

data = args.message
data = data.encode()
client_socket.send(data)
