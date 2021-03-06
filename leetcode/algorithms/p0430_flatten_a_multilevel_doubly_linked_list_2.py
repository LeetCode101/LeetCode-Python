# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        dummy = Node(-1, None, None, None)

        self._flatten_to_stack(head, stack)

        while stack:
            current = stack.pop()
            next = dummy.next
            dummy.next, current.prev = current, dummy
            current.child = None

            if next:
                current.next, next.prev = next, current

        if dummy.next:
            dummy.next.prev = None

        return dummy.next

    def _flatten_to_stack(self, head: Node, stack):
        if not head:
            return

        current = head

        while current:
            stack.append(current)

            if current.child:
                self._flatten_to_stack(current.child, stack)

            current = current.next
