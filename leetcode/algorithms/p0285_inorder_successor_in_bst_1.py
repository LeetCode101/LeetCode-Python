import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        least_value_greater_than_p = sys.maxsize
        target_node = None
        current = root

        while current:
            if p.val < current.val < least_value_greater_than_p:
                target_node = current
                least_value_greater_than_p = current.val
                current = current.left
            elif current.val <= p.val:
                current = current.right

        return target_node
