answers = []
def findCombinations(arr):
	if len(arr) == 2:
		answers.append("".join(arr[:]))
		return 

	# answers.append("".join(arr[:]))

	for letter in "123":
		arr.append(letter)
		findCombinations(arr)
		arr.pop()


findCombinations([])
print(answers)
print(len(answers))
