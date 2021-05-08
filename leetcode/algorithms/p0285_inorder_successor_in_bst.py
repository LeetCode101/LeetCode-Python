import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        least_greater_than_p = sys.maxsize
        target = None
        current = root

        while current:
            if p.val < current.val < least_greater_than_p:
                target = current
                least_greater_than_p = current.val
                current = current.left
            elif current.val <= p.val:
                current = current.right

        return target
