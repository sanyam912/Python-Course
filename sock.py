import socket
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostname(),87))
s.listen(5)
conn,addrs=s.accept()
data = conn.recv (BUFFER_SIZE)
print(data.decode())
