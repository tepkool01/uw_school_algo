import logging


class HMapLinearProbe:
    def __init__(self):
        self.capacity = 10
        self.arr = [None] * self.capacity
        self.size = 0
        self.load_factor_threshold = 0.75

    def hash_key(self, key: str):
        total = 0
        for character in key:
            total += ord(character)

        return total % self.capacity

    def remove(self, key):
        el, hash_key = self._get_element_by_key(key)
        if el:
            self.size -= 1
            self.arr[hash_key] = None

    def _get_element_by_key(self, key):
        hash_key = self.hash_key(key)
        element = self.arr[hash_key]

        while element and element[0] != key:
            hash_key = self._get_next_hash_key(hash_key)
            element = self.arr[hash_key]

        return element, hash_key

    def get_by_key(self, key):
        el, _ = self._get_element_by_key(key)
        return el[1] if el else None

    def _get_next_hash_key(self, hash_key):
        return (hash_key + 1) % self.capacity

    def insert(self, key, val):
        hash_key = self.hash_key(key)
        self.size += 1
        if not self.arr[hash_key]:
            self.arr[hash_key] = [key, val]
        else:
            while self.arr[hash_key]:
                hash_key = self._get_next_hash_key(hash_key)
            self.arr[hash_key] = [key, val]

        if self.load_factor() > self.load_factor_threshold:
            self._rehash()

    def load_factor(self):
        return self.size / self.capacity

    def _rehash(self):
        logging.info(">>_rehash")
        old_arr = self.arr
        self.capacity = self.capacity * 2
        self.size = 0
        self.arr = [None] * self.capacity

        for element in old_arr:
            if element:
                self.insert(element[0], element[1])
