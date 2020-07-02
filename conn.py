import  socket

server_host="127.0.0.1"
server_port=5003

#send 1kb a time
buffer_size=1024
#Below is server code
#socket object
s=socket.socket()

#socket binding
s.bind((server_host,server_port))

#server will listen 5 connection
s.listen(5)
print(f"Listening as {server_host}:{server_port}...")

#accept()-Accept the connection
#client_socket-returns a new socket representing the connection
#client_address- ip and port of client
client_socket,client_address=s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!!")
message="test message".encode()
client_socket.send(message)

while True:
    cmd=input("Enter the command:")
    #send the cmd to the client
    client_socket.send(cmd.encode())
    if cmd.lower()=="exit":
        break
    #retreive cmd results
    results=client_socket.recv(buffer_size).decode()
    print(results)
client_socket.close()
s.close()
