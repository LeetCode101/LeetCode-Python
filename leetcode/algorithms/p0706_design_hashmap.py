from collections import deque


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def add(self, node):
        if node.key > self.key:
            if not self.right:
                self.right = node
            else:
                self.right.add(node)
        elif node.key < self.key:
            if not self.left:
                self.left = node
            else:
                self.left.add(node)
        else:
            self.value = node.value

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key > key:
            return self.left.get(key) if self.left else -1
        else:
            return self.right.get(key) if self.right else -1

    def remove(self, key):
        if self.key == key:
            if not self.left and not self.right:
                return None
            elif not self.left or not self.right:
                return self.left or self.right
            else:
                min_node = self.right._find_min()
                self.key = min_node.key
                self.value = min_node.value
                self.right = self.right.remove(self.key)
        elif self.key > key and self.left:
            self.left = self.left.remove(key)
        elif self.key < key and self.right:
            self.right = self.right.remove(key)

        return self

    def traverse(self):
        queue = deque([self])
        nodes = []

        while queue:
            node = queue.popleft()
            nodes.append(node)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return nodes

    def _find_min(self):
        current = self

        while current.left:
            current = current.left

        return current


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None] * 16
        self.size = 0
        self.load_factor = 0.75

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self._hash(key)
        new_node = Node(key, value)

        if not self.nodes[h]:
            self.nodes[h] = new_node
        else:
            self.nodes[h].add(new_node)

        self.size += 1

        if self.size > self.load_factor * len(self.nodes):
            self._rehash()

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        h = self._hash(key)

        if self.nodes[h]:
            return self.nodes[h].get(key)

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key
        if this map contains a mapping for the key
        """
        h = self._hash(key)

        if self.nodes[h]:
            self.nodes[h] = self.nodes[h].remove(key)
            self.size -= 1

    def _rehash(self):
        new_nodes = [None] * (len(self.nodes) * 2)
        old_nodes = self.nodes
        self.nodes = new_nodes

        for node in old_nodes:
            if not node:
                continue

            for n in node.traverse():
                self.put(n.key, n.value)

    def _hash(self, key):
        return key % len(self.nodes)
