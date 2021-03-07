# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node

            return node

        prev, current = head, head.next

        while current is not head:
            if prev.val <= insertVal <= current.val:
                prev.next = Node(insertVal, current)

                return head

            if prev.val > current.val \
                    and (prev.val <= insertVal or insertVal <= current.val):
                prev.next = Node(insertVal, current)

                return head

            prev, current = current, current.next

        prev.next = Node(insertVal, current)

        return head
