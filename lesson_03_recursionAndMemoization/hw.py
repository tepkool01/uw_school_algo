def find_sum(arr):
	if len(arr) == 0:
		return 0
	if len(arr) == 1:
		return arr[0]
	return arr.pop() + find_sum(arr)


def is_palindrome(s):
	s =	s.replace(' ', '')
	if len(s) <= 1:
		return True

	if s[-1] == s[0]:
		return is_palindrome(s[1:-1])

	return False 
	

def step_ways(steps):
	if steps < 0:
		return 0
	if steps == 0:
		return 1

	return step_ways(steps - 1) + step_ways(steps - 2) + step_ways(steps - 3)


memory = {}
def step_ways_with_cache(steps):
	if steps < 0:
		return 0
	if steps == 0:
		return 1

	if steps in memory:
		return memory[steps]
	else:
		memory[steps] = step_ways_with_cache(steps - 1) + step_ways_with_cache(steps - 2) + step_ways_with_cache(steps - 3)

	return memory[steps]

