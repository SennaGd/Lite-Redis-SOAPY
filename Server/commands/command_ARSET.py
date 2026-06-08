# define the array name:
from typeChecking import check_type


def command_ARSET(dataList:list[tuple], parsedOutput: list):
	newData = [{}]
	key = parsedOutput[0]
	values = []

	for value in parsedOutput[1:]:
		val = check_type(value)
		
		values.append(val)

	print(values)
	
	print(parsedOutput)
		
	if key and len(values)>0:
		newData[key] = values
	

	print(newData)
	return ["G", newData[0]]
