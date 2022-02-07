import collections
import sys
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        min_level = 0
        max_sum = -sys.maxsize
        queue = collections.deque([root])

        while queue:
            level += 1
            size = len(queue)
            current_sum = 0

            for _ in range(size):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if max_sum < current_sum:
                min_level = level
                max_sum = current_sum

        return min_level
