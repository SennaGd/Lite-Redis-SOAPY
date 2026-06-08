from ast import parse


def command_ARGET(dataList: list[dict], parsedOutput: list):
	key = dataList[0].get(str(parsedOutput[0]))
	if isinstance(key, dict):
		value = key[parsedOutput[1]]
	else:
		value = "(nil)"
	return ["G", value]
