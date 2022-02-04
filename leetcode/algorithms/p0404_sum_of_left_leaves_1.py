import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        queue = collections.deque([(root, None)])

        while queue:
            size = len(queue)

            for _ in range(size):
                node, parent = queue.popleft()

                if parent and node is parent.left \
                        and not node.left and not node.right:
                    sum += node.val

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

        return sum
