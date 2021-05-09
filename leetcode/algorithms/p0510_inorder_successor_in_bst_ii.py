class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            current = node.right

            while current.left:
                current = current.left

            return current

        current = node

        while current.parent:
            if current.parent.left is current:
                return current.parent

            current = current.parent

        return None
