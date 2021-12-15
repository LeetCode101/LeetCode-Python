import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([(root, 0)])
        count = 0

        while queue:
            node, bits = queue.popleft()
            bits ^= 1 << node.val

            if self._is_leaf(node) and bits & (bits - 1) == 0:
                count += 1

            if node.left:
                queue.append((node.left, bits))

            if node.right:
                queue.append((node.right, bits))

        return count

    def _is_leaf(self, node):
        return not node.left and not node.right
