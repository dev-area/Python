import socket

sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect(('localhost',2000))
 
sock.send('hello')
