from socket import socket
from commandManager import handle_commands
from data import dataList

# list of commands that shouldn't be saved (useless)
getList = [
	"GET",
	"ARGET"
	"ARMGET"
]

def parse_input(receivedSocket: str):
	"""Splits each word in segments returned inside a list"""

	parsedOutput= []
	word = ""	


	for i in range(len(receivedSocket)):
		if receivedSocket[i] == " ":
			parsedOutput.append(word)
			word = ""
		else:
			word += receivedSocket[i]
		
		if word[len(word)-3: len(word)-1] == "\n":
			word = word[0:len(word)-1]

		if i == len(receivedSocket)-1:

			parsedOutput.append(word)
		
	return parsedOutput


def handle_request(client_socket: socket):
	try:
		receivedString = client_socket.recv(1024).decode()
		print(receivedString[len(receivedString)-3:len(receivedString)-1])
		if receivedString[len(receivedString)-3:len(receivedString)-1] == "\n":
			receivedString = receivedString[0:len(receivedString)-3]
		parsedOutput = parse_input(receivedString)
		update_aof(receivedString, parsedOutput, getList)
		returnData = handle_commands(parsedOutput)

		print("[-] RECEIVED {", parsedOutput[0], "} REQUEST")

		return returnData
	except:
		pass

# SAVING #

# test function | expects: ["GET hello", "SET hello world"]
def test(commandsList ) -> bool:
	for command in commandsList:
		parsedOutput = parse_input(command)
		returnData = handle_commands(parsedOutput)	
			
		print(returnData)
	print(dataList)
	return True

# returns backup file as list
def get_aof_contents():
	fileContents = []
	with open("save.txt", "r") as file:
		for line in file:
			line =	line.replace("\n", "")
			fileContents.append(line)	

	return fileContents


# updates the backup file
def update_aof(unparsedCommand, parsedCommand, getList):
	if parsedCommand[0] in getList:
		return False	
	
	with open("save.txt", "a") as backupFile:
		backupFile.write(unparsedCommand+"\n")	
	return True


# load append only file (backup/oinstart)
def load_aof(commandsList):
	print("Loading backup.. please wait!")

	for command in commandsList:
		parsedOutput = parse_input(command)
		handle_commands(parsedOutput)
	
	print("backup loaded successfully!")


