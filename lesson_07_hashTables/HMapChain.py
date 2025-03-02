from node import Node
import logging


class HMapChain:
	def __init__(self):
		self.capacity = 10
		self.arr = [None] * self.capacity
		self.size = 0
		self.load_factor_threshold = 1.5

	def hash_key(self, key: str):
		total = 0
		for character in key:
			total += ord(character)

		return total % self.capacity
	
	def get_by_key(self, key):
		hash_key = self.hash_key(key)
		element = self.arr[hash_key]
		while element:
			if element.key == key:
				return element.val
			element = element.next
		return None

	def insert(self, key, val):
		hash_key = self.hash_key(key)
		self.size += 1
		if self.arr[hash_key] is None:
			self.arr[hash_key] = Node(val=val, key=key)
			return

		ptr = self.arr[hash_key] 
		while ptr:
			if ptr.key == key:  # Override key
				ptr.val = val
				return
			if ptr.next is None:
				break
			ptr = ptr.next
		ptr.next = Node(val=val, key=key)

		if self.load_factor() > self.load_factor_threshold:
			self._rehash()

	def load_factor(self):
		return self.size / self.capacity

	def _rehash(self):
		logging.info(">>_rehash()")
		old_arr = self.arr
		self.capacity = self.capacity * 2
		self.arr = [None] * self.capacity
		self.size = 0

		for node in old_arr:
			while node:
				self.insert(node.key, node.val)
				node = node.next

		logging.info(f"<<_rehash - new size: {self.capacity}")

	def remove(self, key):
		hash_key = self.hash_key(key)
		element = self.arr[hash_key]
		prev = None

		while element:
			if element.key == key:
				if prev:
					prev.next = element.next
				else:
					self.arr[hash_key] = element.next
				self.size -= 1
				return True
			prev = element
			element = element.next

		return False
