import collections
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
        queue = collections.deque([(root, '')])

        while queue:
            node, path = queue.popleft()
            new_path = path + str(node.val)

            if not node.left and not node.right:
                result.append(path + str(node.val))

            if node.left:
                queue.append((node.left, new_path + '->'))

            if node.right:
                queue.append((node.right, new_path + '->'))

        return result
