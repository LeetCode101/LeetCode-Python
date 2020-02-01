class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        current = head
        dummy = Node(-1)
        prev = dummy
        old_new_list_mapping = {}

        while current:
            prev.next = Node(current.val)
            old_new_list_mapping[current] = prev.next
            prev = prev.next
            current = current.next

        current, new_current = head, dummy.next

        while current:
            if current.random:
                new_current.random = old_new_list_mapping[current.random]

            current, new_current = current.next, new_current.next

        return dummy.next
