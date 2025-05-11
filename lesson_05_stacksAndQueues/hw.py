# 1. Create a Reverse Polish Notation calculator
class RPN:
	def __init__(self):
		self.stack = []

	def process(self, value):
		if str(value) in "+-*/":
			num2 = self.stack.pop()
			num1 = self.stack.pop()
			result = 0
			if str(value) == "+":
				result = num1 + num2
			elif str(value) == "-":
				result = num1 - num2
			elif str(value) == "*":
				result = num1 * num2
			elif str(value) == "/":
				result = num1 / num2

			self.stack.append(result)
		else:
			self.stack.append(value)
  
	def result(self):
		return int(self.stack[0])

rpn = RPN()
rpn.process(5)
rpn.process(4)
rpn.process("+")
print(rpn.result())

rpn = RPN()
rpn.process(5)
rpn.process(4)
rpn.process("-")
print(rpn.result())

rpn = RPN()
rpn.process(3)
rpn.process(2)
rpn.process("*")
print(rpn.result())

rpn = RPN()
rpn.process(9)
rpn.process(3)
rpn.process("/")
print(rpn.result())

rpn = RPN()
rpn.process(5)
rpn.process(4)
rpn.process("+")
rpn.process(3)
rpn.process("/")
rpn.process(5)
rpn.process("*")
rpn.process(15)
rpn.process("-")
print(rpn.result())

# 2. Write a method that removes the maximum value from a stack
from collections import deque
def remove_max(values):
	if not values:
		return

	high = max(values)
	queue = deque()

	while values:
		val = values.pop()
		if val != high:
			queue.appendleft(val)

	while queue:
		values.append(queue.popleft())

	return high


# arrange
input_arr = [7,77,88,2,97,5,117,107,61,107,52]
# act / assert
print(remove_max(input_arr)) # == 117
print(input_arr == [7,77,88,2,97,5,107,61,107,52])
# input = [7,77,88,2,97,5,107,61,107,52]


