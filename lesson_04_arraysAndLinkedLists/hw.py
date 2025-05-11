# Problem 1
def merge(a, b):
	if len(a) == 0 and len(b) == 0:
		return []
	if len(a) == 0:
		return b
	if len(b) == 0:
		return a
	
	answer = []
	a_index, b_index = 0, 0
	min_range = min(len(a), len(b))

	for _ in range(min_range):
		if a[a_index] < b[b_index]:
			answer.append(a[a_index])
			a_index += 1
		else:
			answer.append(b[b_index])
			b_index += 1

	if len(a) > len(b):
		answer.extend(a)
	else:
		answer.extend(b)

	return answer

print(merge([5, 10, 15, 20], [3, 7, 13, 60]))
print(merge([5, 10, 15, 20], [3, 7, 13, 60, 100]))


# Problem 2
def reverse_print(head):
	previous = None
	
	while head:
		next_node = head.next # remember next node
		head.next = previous
		previous = head
		head = next_node

	head = previous
	while head:
		print(head.val)
		head = head.next

# Problem 3
def reverse(head):
	previous = None

	while head:
		next_node = head.next
		head.next = previous
		previous = head
		head = next_node

	return previous

class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

reverse_print(a)

a_2 = Node(1)
b_2 = Node(2)
c_2 = Node(3)
a_2.next = b_2
b_2.next = c_2

reversed_list = reverse(a_2)
while reversed_list:
	print(reversed_list.val)
	reversed_list = reversed_list.next
