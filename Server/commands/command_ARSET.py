# define the array name:
from typeChecking import check_type


def command_ARSET(dataList:list[tuple], parsedOutput: list):
	newData = [{}]

	arrayName= parsedOutput[0] 
	index = parsedOutput[1]

	if not index.isnumeric():
		return ["F", "Invalid Index"]

	else:
		index = int(index)

	newData[0][arrayName] = {}
	newData[0][arrayName][str(index)] = check_type(parsedOutput[2])
	print(newData[0])

	index += 1
	for values in parsedOutput[3:]:
		if values.isnumeric():

			index = int(values)
			# I know, I know..
			continue

		newData[0][arrayName][str(index)] = check_type(values)
		index += 1	

	return ["S", newData[0]]
