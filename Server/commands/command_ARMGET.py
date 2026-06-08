def command_ARMGET(dataList: list[dict], parsedOutput: list):
	key = dataList[0].get(str(parsedOutput[0]))
	returnedData = []
	
	if isinstance(key, dict):
		for index in parsedOutput[1:]:
			if index.isnumeric():
				if key[index]:
					value = str(index), key[index]
				else:
					value = str(index), "). (nil)"

				returnedData.append(value)
	else:
		value = "(nil)"
	return ["G", returnedData]
