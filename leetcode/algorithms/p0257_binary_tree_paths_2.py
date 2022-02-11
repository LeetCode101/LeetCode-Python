from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []
        stack = [(root, '')]

        while stack:
            node, path = stack.pop()
            new_path = path + str(node.val)

            if not node.left and not node.right:
                result.append(path + str(node.val))

            if node.left:
                stack.append((node.left, new_path + '->'))

            if node.right:
                stack.append((node.right, new_path + '->'))

        return result
