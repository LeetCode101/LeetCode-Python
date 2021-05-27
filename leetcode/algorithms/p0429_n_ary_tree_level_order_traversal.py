from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()

                level.append(node.val)

                if node.children:
                    for child in node.children:
                        queue.append(child)

            levels.append(level)

        return levels
