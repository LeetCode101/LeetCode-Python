class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        size = 0
        current = head
        dummy = Node(-1)
        prev = dummy
        original_list_mapping, new_list_mapping = {}, {}

        while current:
            prev.next = Node(current.val)
            prev = prev.next
            original_list_mapping[current] = size
            new_list_mapping[size] = prev
            current = current.next
            size += 1

        current, new_current = head, dummy.next

        while current:
            if current.random:
                random_node_index = original_list_mapping[current.random]
                new_current.random = new_list_mapping[random_node_index]

            current, new_current = current.next, new_current.next

        return dummy.next
