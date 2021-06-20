class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _append_head(self, node: Node) -> None:
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def _move_to_head(self, node: Node) -> None:
        self._pop(node)
        self._append_head(node)

    def _pop(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _pop_tail(self) -> Node:
        tail = self.tail.prev

        self._pop(tail)

        return tail

    def get(self, key: int) -> int:
        if key not in self.caches:
            return -1

        node = self.caches[key]

        self._move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            node = self.caches[key]
            node.value = value

            self._move_to_head(node)
        else:
            new_node = Node(key, value)

            self.caches[key] = new_node
            self._append_head(new_node)

            if len(self.caches) > self.capacity:
                tail = self._pop_tail()

                self.caches.pop(tail.key)
