from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        levels = []
        depth = 0

        while queue:
            depth += 1
            is_odd = depth & 1 == 1
            length = len(queue)
            level = [0] * length

            for i in range(length):
                node = queue.popleft()

                if is_odd:
                    level[i] = node.val
                else:
                    level[length - i - 1] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels
