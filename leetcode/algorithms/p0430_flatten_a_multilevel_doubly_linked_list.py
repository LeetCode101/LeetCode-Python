# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if head.child:
            child_head = self.flatten(head.child)
            child_tail = child_head

            while child_tail and child_tail.next:
                child_tail = child_tail.next

            next = self.flatten(head.next)
            head.next, child_head.prev = child_head, head
            head.child = None

            if next:
                child_tail.next, next.prev = next, child_tail
        else:
            head.next = self.flatten(head.next)

        return head
