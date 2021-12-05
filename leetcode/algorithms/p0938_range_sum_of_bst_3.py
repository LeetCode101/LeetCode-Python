import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) \
            -> int:
        range_sum = 0
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if low <= node.val <= high:
                range_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            elif node.val < low and node.right:
                queue.append(node.right)
            elif node.val > high and node.left:
                queue.append(node.left)

        return range_sum
