from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            depth += 1
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.children:
                    for child in node.children:
                        queue.append(child)

        return depth
