from socket import socket, AF_INET, SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 9998))

message = input()
client.send(message.encode())

# convert bytes to str
received = str(client.recv(1024))

# parsing string | remove bytes b'' 
received = received[2:len(received)-1]
print(received)

