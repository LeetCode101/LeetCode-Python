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
            return

        stack = [head]
        prev = Node(-1, None, head, None)

        while stack:
            root = stack.pop()
            root.prev, prev.next = prev, root

            if root.next:
                stack.append(root.next)
                root.next = None

            if root.child:
                stack.append(root.child)
                root.child = None

            prev = root

        head.prev = None

        return head
