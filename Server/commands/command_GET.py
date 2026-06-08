def command_GET(dataList: list[dict], dataIndex):
	returnedData = []
	for key in dataIndex:
		value = dataList[0].get(key)
		if value == None:
			value = "(nil)"

		returnedData.append(value)

	return ["G", returnedData]
	

