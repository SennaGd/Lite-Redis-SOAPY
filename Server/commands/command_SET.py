import re

def check_for_dots(string):
	match = re.search(r"\.", string)
	if match is None:
		return False 
	else:
		return True

def parse_to_float(string: str, dotIndex):
	# remove dot, split string
	intSegment = string[0:dotIndex]
	intSegment = float(intSegment)
	
	# decimal parsing
	decimalSegment = string[dotIndex+1:len(string)]
	decimalLen = len(decimalSegment)
	
	multiplication = 1.0

	for x in range(decimalLen):
		multiplication = multiplication / 10

	decimalSegment = float(decimalSegment) * multiplication
	
	parsedFloat = intSegment + decimalSegment

	return parsedFloat

def check_if_float(string: str):
	dots = 0 # float only float if one "."
	dotIndex = []
	
	index = 0
	for char in string:
		isDot = check_for_dots(char)
		if isDot == True:
			dots += 1
			dotIndex.append(index)
			
		index += 1	

	# remove dots | check if the value is numberic	
	if dots != 1:
		return False
	else:
		return dotIndex[0] 

def check_if_bool():
	...

def command_SET(dataList: list[dict], parsedOutput: list):
	key, value = None, None
	newData = [{}]

	# create key value pairs

	# string : V
	# int    : V
	# float  : V
	# bool   : X

	for i in range(len(parsedOutput)):	
		if i % 2 == 0:
			key = parsedOutput[i]
		else:
			if parsedOutput[i].isnumeric():
				value = int(parsedOutput[i])

			if not parsedOutput[i].isnumeric():
				value = parsedOutput[i]
			
			isFloat = check_if_float(parsedOutput[i])
			if isFloat is not False:
				# isFloat will be the index of the first dot inside the float
				value = parse_to_float(parsedOutput[i], isFloat)
				

		if key and value:
			newData[0][key] = value
			key, value = None, None

#		if len(newData[0]) == 0:
#			return ["F", None]

	return ["S", newData[0]] 
