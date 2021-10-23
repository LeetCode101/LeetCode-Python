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
        queue1 = deque([root]) if root else deque()
        queue2 = deque()

        while queue1 or queue2:
            depth += 1
            level = []
            is_odd = depth & 1 == 1

            if is_odd:
                for _ in range(len(queue1)):
                    node = queue1.popleft()
                    level.append(node.val)

                    if node.left:
                        queue2.append(node.left)

                    if node.right:
                        queue2.append(node.right)
            else:
                for _ in range(len(queue2)):
                    node = queue2.pop()
                    level.append(node.val)

                    if node.right:
                        queue1.appendleft(node.right)

                    if node.left:
                        queue1.appendleft(node.left)

            levels.append(level)

        return levels
