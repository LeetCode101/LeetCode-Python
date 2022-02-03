import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 1
        queue = collections.deque([(root, 1)])

        while queue:
            size = len(queue)
            width = queue[-1][1] - queue[0][1] + 1

            for _ in range(size):
                node, id = queue.popleft()

                if node.left:
                    queue.append((node.left, id * 2))

                if node.right:
                    queue.append((node.right, id * 2 + 1))

            max_width = max(max_width, width)

        return max_width
