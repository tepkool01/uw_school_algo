class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Tree:
	def __init__(self, arr):
		self.root = TreeNode(arr[0])
		for val in arr[1:]:
			self.insert(val)

	def insert(self, val):
		node = self.root
		while True:
			if val > node:
				if node.right is None:
					node.right = TreeNode(val)
					break
				node = node.right
			else: 
				if node.left is None:
					node.left = TreeNode(val)
					break
				node = node.left
