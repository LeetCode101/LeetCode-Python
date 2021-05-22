from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, node):
        if node.value > self.value:
            if not self.right:
                self.right = node
            else:
                self.right.add(node)
        elif node.value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.add(node)

    def contains(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            return self.left and self.left.contains(value)
        else:
            return self.right and self.right.contains(value)

    def remove(self, value):
        if self.value == value:
            if not self.left and not self.right:
                return None
            elif not self.left or not self.right:
                return self.left or self.right
            else:
                self.value = self.right._find_min().value
                self.right = self.right.remove(self.value)
        elif self.value > value and self.left:
            self.left = self.left.remove(value)
        elif self.value < value and self.right:
            self.right = self.right.remove(value)

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


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None] * 16
        self.size = 0
        self.load_factor = 0.75

    def add(self, key: int) -> None:
        h = self._hash(key)
        new_node = Node(key)

        if not self.nodes[h]:
            self.nodes[h] = new_node
        else:
            self.nodes[h].add(new_node)

        self.size += 1

        if self.size > self.load_factor * len(self.nodes):
            self._rehash()

    def remove(self, key: int) -> None:
        h = self._hash(key)

        if self.nodes[h]:
            self.nodes[h] = self.nodes[h].remove(key)
            self.size -= 1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = self._hash(key)

        if self.nodes[h]:
            return self.nodes[h].contains(key)

        return False

    def _rehash(self):
        new_nodes = [None] * (len(self.nodes) * 2)
        old_nodes = self.nodes
        self.nodes = new_nodes

        for node in old_nodes:
            if not node:
                continue

            for n in node.traverse():
                self.add(n.value)

    def _hash(self, key):
        return key % len(self.nodes)
