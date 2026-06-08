
def parse_to_bool(string: str):
	if string.lower() == "False":
		return False
	if string.lower() == "true":
		return True
	else: return string

