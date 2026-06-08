from typeChecking import check_type


def command_ARMSET(dataList:list[tuple], parsedOutput: list):
	newData = [{}]

	arrayName= parsedOutput[0] 
	index = parsedOutput[1]

	if not index.isnumeric():
		return ["F", "Invalid Index"]

	else:
		index = int(index)

	indice = {index : check_type(parsedOutput[2])}
	
	newData[0][arrayName] = {}
	newData[0][arrayName][str(index)] = check_type(parsedOutput[2])
	print(newData[0])

	index += 1
	for values in parsedOutput[3:]:
		newData[0][arrayName][str(index)] = check_type(values)
		index += 1	

	return ["S", newData[0]]
