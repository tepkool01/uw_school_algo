from collections import deque


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Tree:
	# 1) Write a function that takes in a list of integers, creates a binary tree with those integers
	def __init__(self, arr):
		self.root = TreeNode(arr[0])
		for val in arr[1:]:
			self._insert(val)

	def _insert(self, val):
		node = self.root
		while True:
			if val > node.val:
				if node.right is None:
					node.right = TreeNode(val)
					break
				node = node.right
			else:
				if node.left is None:
					node.left = TreeNode(val)
					break
				node = node.left

	# 2) Write a function that returns the in-order traversal of the tree as space-separated string.
	def in_order(self):
		answer = []
		stack = []
		node = self.root
		while stack or node:
			while node:
				stack.append(node)
				node = node.left

			node = stack.pop()
			answer.append(str(node.val))
			node = node.right

		return " ".join(answer)

	# 3) Write a function that returns the pre-order traversal of the tree as space-separated string.
	def pre_order(self):
		answer = []
		stack = [self.root]
		while stack:
			node = stack.pop()
			answer.append(str(node.val))

			if node.right: # Reversed!! This will get added first, and popped 2nd
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

		return " ".join(answer)

	# 4) Write a function that returns the post-order traversal of the tree as space-separated string.
	def post_order(self):
		answer = []
		stack = [self.root]
		while stack:
			node = stack.pop()
			answer.append(str(node.val))

			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)

		return " ".join(map(str, answer[::-1]))

	# 5) Write a function that determines the height of a given tree.
	def height(self):
		queue = deque([self.root])
		levels = 0
		while queue:
			levels += 1
			level_len = len(queue)
			for _ in range(level_len):
				node = queue.popleft()
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return levels - 1  # not counting root, per instructions

	# 6) Write a function that returns the sum of all values in a tree.
	def sum(self):
		stack = [self.root]
		total = 0
		while stack:
			node = stack.pop()
			total += node.val
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return total

	# 7) Write a function that returns a bool indicating that a value exists (or not) in a given tree.
	def contains(self, value):
		node = self.root
		while node:
			if node.val == value:
				return True
			elif value > node.val:
				node = node.right
			else:
				node = node.left

		return False


a = Tree([10, 15, 7, 9, 3, 24])
print(a.in_order())  # 3 7 9 10 15 24
print(a.pre_order())  # 10 7 3 9 15 24
print(a.post_order())  # 3 9 7 24 15 10
print(a.height())  # 2 (doesn't count root)
print(a.sum())  # 68
print(a.contains(2))  # False
print(a.contains(3))  # True