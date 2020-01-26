from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue1 = deque([root]) if root else deque()
        queue2 = deque()
        level = []
        levels = []

        while queue1:
            node = queue1.popleft()
            level.append(node.val)

            if node.left:
                queue2.append(node.left)

            if node.right:
                queue2.append(node.right)

            if not queue1:
                queue1, queue2 = queue2, queue1
                levels.append(level)
                level = []

        return levels
