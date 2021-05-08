class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        target_node = None
        current = root

        while current:
            if current.val > p.val:
                target_node = current
                current = current.left
            elif current.val <= p.val:
                current = current.right

        return target_node
