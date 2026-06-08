from commands.command_SET import command_SET 
from commands.command_GET import command_GET
from commands.command_DEL import command_DEL
from commands.command_ARSET import command_ARSET
from commands.command_ARGET import command_ARGET
from commands.command_ARMSET import command_ARMSET
from commands.command_ARMGET import command_ARMGET

from data import dataList

commandsList = {
		"GET" : command_GET,
		"SET" : command_SET,
		"DEL" : command_DEL,
		"ARSET": command_ARSET,
		"ARGET": command_ARGET,
		"ARMSET":command_ARMSET,
		"ARMGET":command_ARMGET,
	}


def handle_commands(parsedOutput: list):
#	if len(parsedOutput) == 0:
#		return None
#	if r"\n" in parsedOutput[len(parsedOutput)-1]:
#		print("NEWLINE CHAR")
	
	fetchedFunc = commandsList[parsedOutput[0]]	
	returnedData =	fetchedFunc(dataList, parsedOutput[1:])	

	returnData = None

	# Assign Variables
	if returnedData[0] == "S":
		dataList[0] |= returnedData[1]
		returnData = "Ok"
	# Get Variables
	if returnedData[0] == "G":
		returnData = returnedData[1]

	if returnedData[0] == "D":
		dataList[0] = returnedData[1]
	# False return
	if returnedData[0] == "F":
		returnData = "Invalid Command/Variable(s)."

	
	if type(returnData) == list:
		if len(returnData) == 1:
			returnData = returnData[0]

	return returnData 


