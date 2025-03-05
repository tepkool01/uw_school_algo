base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def to_base_10(videoId):
	result = 0
	for character in videoId:
		result = result * 62 + base_62.index(character)

	return result


def to_base_62(number):
	result = []
	
	while number > 0:
		result.append(base_62[number % 62])
		number = number // 62

	return "".join(reversed(result))


# assert main.to_base_10("LpuPe81bc2w") == 18327995462734721974
print(to_base_10("LpuPe81bc2w"))

# assert main.to_base_62(18327995462734721974) == "LpuPe81bc2w"
print(to_base_62(18327995462734721974))
