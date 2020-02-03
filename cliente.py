import socket
import os
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conecta = s.connect((HOST, PORT))

cmd = sys.argv[2:]
comando = " ".join(cmd)

s.sendall(comando)
data = s.recv(20480)
print(data)
s.close()
