from parsing.checkFloat import parse_to_float
from parsing.checkBool import parse_to_bool
from parsing.checkInt import parse_to_int

def check_type(value):
	value = parse_to_float(value) if type(value) != float else value	
	if isinstance(value, float): return value 

	value = parse_to_int(value) if type(value) != int else value
	if isinstance(value, int): return value 

	value = parse_to_bool(value) if type(value) != bool else value
	if isinstance(value, bool): return value

	return str(value)


