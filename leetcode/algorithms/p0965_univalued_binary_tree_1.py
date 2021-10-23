import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        value = root.val
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.val != value:
                return False

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return True
