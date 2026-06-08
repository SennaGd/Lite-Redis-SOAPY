import re
from ..typeChecking import check_type

def command_SET(dataList: list[dict], parsedOutput: list):
	key, value = None, None
	newData = [{}]

	# create key value pairs
	for i in range(len(parsedOutput)):	
		# every equal index is a key
		if i % 2 == 0:
			key = parsedOutput[i]

		# unequal index is value
		else:
			value = check_type(parsedOutput[i])		

		if key and value:
			newData[0][key] = value
			key, value = None, None

	return ["S", newData[0]] 
