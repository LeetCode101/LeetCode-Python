import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = collections.deque([(root, 0, 0)])

        while queue:
            node, level, sum_so_far = queue.popleft()
            sum_so_far = sum_so_far * 10 + node.val

            if node.left:
                queue.append((node.left, level + 1, sum_so_far))

            if node.right:
                queue.append((node.right, level + 1, sum_so_far))

            if not node.left and not node.right:
                total += sum_so_far

        return total
