from socket import socket, AF_INET, SOCK_STREAM 
from time import time
from inputHandler import handle_request, get_aof_contents, load_aof

SAVING = False 

BACKLOG_SIZE = 10
BIND_IP = "0.0.0.0"
BIND_PORT = 9998

server = socket(AF_INET, SOCK_STREAM)
server.bind((BIND_IP, BIND_PORT))
server.listen(BACKLOG_SIZE) 

# load backup
if SAVING:
	backupFile = get_aof_contents()
	load_aof(backupFile)


while True:
	client, addr = server.accept()	
		
	returnedData = handle_request(client)
		
	# sending data back
	client.send(str(returnedData).encode())
