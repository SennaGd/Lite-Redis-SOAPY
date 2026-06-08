import re

def check_if_float(string: str):
	dots = 0 # float only float if one "."
	dotIndex: list[int] = []
	
	index = 0
	for char in string:
		match = re.search(r"\.", char)
		if match:
			dots += 1
			
			# make sure no more than 1 dot
			if dots > 1:
				return False

			dotIndex.append(index)

		index += 1	
	if dots == 0:
		return False
	# remove dots | check if the value is numberic	
	return dotIndex[0] 

def parse_to_float(string: str):
	isFloat = check_if_float(string)
	if isFloat == False:
		return string 
	else:
		dotIndex: int = isFloat

	# remove dot, split string
	intSegment = string[0:dotIndex]
	intSegment = float(intSegment)
	
	# decimal parsing
	decimalSegment = string[dotIndex+1:len(string)]
	decimalLen = len(decimalSegment)
	
	multiplication = 1.0

	for _ in range(decimalLen):
		multiplication = multiplication / 10

	decimalSegment = float(decimalSegment) * multiplication
	parsedFloat = intSegment + decimalSegment

	return parsedFloat

