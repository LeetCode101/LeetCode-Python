class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        dummy = Node(-1)
        prev = dummy
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            node = Node(current.val)
            node.left, prev.right = prev, node
            prev = node
            current = current.right

        if prev is not dummy:
            prev.right = dummy.right
            dummy.right.left = prev

        return dummy.right
