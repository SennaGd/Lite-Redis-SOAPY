def command_ARSET(dataList: list[dict], parsedOutput: list):
	#ARSET balls one 2 2

	#balls[0] = one
	#balls[1] = 2
	#balls[2] = 2
	
	print(parsedOutput)

	# define the array name:
	name = parsedOutput[0]
	
	parsedOutput[0].pop() # remove name
	
	arr = []
	for values in parsedOutput:
		arr.append(values)
	
