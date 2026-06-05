def command_DEL(dataList: list[dict], dataIndex):
	returnedData = []
	print(dataIndex)
	for key in dataIndex:
		try:
			dataList[0].pop(key)
		except:
			...
		value = dataList[0].get(key)

		if value == None:
			value = "(nil)"

		returnedData.append(value)

	return ["G", returnedData]


