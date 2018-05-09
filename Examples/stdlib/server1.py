import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(("", 2000))
sock.listen(5)
 
while True:
    sktup = sock.accept()
 
# usually we open a new thread or process to handle the client
    bMessage = sktup[0].recv(1024, 0)
    print("Msg Recieved: ", bMessage.decode())
