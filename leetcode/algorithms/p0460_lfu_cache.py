import collections


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._size = 0
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def __len__(self):
        return self._size

    def append_head(self, node):
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node
        self._size += 1

    def pop(self, node):
        if self._size == 0:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def pop_tail(self):
        tail = self._tail.prev

        self.pop(tail)

        return tail


class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node_cache = {}
        self._frequency_cache = collections.defaultdict(DoublyLinkedList)
        self._min_frequency = 0

    def get(self, key: int) -> int:
        if key not in self._node_cache:
            return -1

        node = self._node_cache[key]
        self._update(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._node_cache:
            node = self._node_cache[key]
            self._update(node)
            node.value = value
        else:
            if self._size == self._capacity:
                node = self._frequency_cache[self._min_frequency].pop_tail()
                del self._node_cache[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node_cache[key] = node
            self._frequency_cache[1].append_head(node)
            self._min_frequency = 1
            self._size += 1

    def _update(self, node):
        frequency = node.frequency

        self._frequency_cache[frequency].pop(node)

        if self._min_frequency == frequency \
                and not self._frequency_cache[frequency]:
            self._min_frequency += 1

        node.frequency += 1
        self._frequency_cache[frequency + 1].append_head(node)
