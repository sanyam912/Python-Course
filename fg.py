import socket
TCP_IP='50.0.0.2'
TCP_PORT=87
BUFFER_SIZE=1024
MESSAGE=str(input("ENTER : ")).encode()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
print('connected')
s.send(MESSAGE)
data=s.recv(BUFFER_SIZE)
print('receive data:',data)
s.close()
