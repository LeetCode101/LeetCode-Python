import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = collections.deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev = None

            if size == 1 and level & 1 == queue[0].val & 1:
                return False

            for _ in range(size):
                node = queue.popleft()

                if prev is not None:
                    if self._is_odd(level) and (
                            self._is_odd(node.val) or prev <= node.val):
                        return False
                    elif self._is_even(level) and (
                            self._is_even(node.val) or prev >= node.val):
                        return False

                prev = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return True

    def _is_odd(self, value):
        return value & 1 == 1

    def _is_even(self, value):
        return not self._is_odd(value)
