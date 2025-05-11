def convertToBinary(x: int) -> str:
	result = ['0'] * 8
	
	j = 7
	for i in range(7):
		if x & (1 << i):
			result[j] = '1'
		j -= 1

	return "".join(result)

print(convertToBinary(4))
print(convertToBinary(5))
