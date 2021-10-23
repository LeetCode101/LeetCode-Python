from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        depth = 0
        levels = []
        queue = deque([root]) if root else deque()

        while queue:
            depth += 1
            level = []
            is_odd = depth & 1 == 1

            for _ in range(len(queue)):
                node = queue.popleft() if is_odd else queue.pop()
                level.append(node.val)

                if is_odd:
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
                else:
                    if node.right:
                        queue.appendleft(node.right)

                    if node.left:
                        queue.appendleft(node.left)

            levels.append(level)

        return levels
