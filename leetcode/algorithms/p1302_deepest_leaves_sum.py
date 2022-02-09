import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        deepest_sum = 0

        while queue:
            size = len(queue)
            deepest_sum = 0

            for _ in range(size):
                node = queue.popleft()
                deepest_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return deepest_sum
