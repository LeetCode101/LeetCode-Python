import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int,
                      destValue: int) -> str:
        graph = collections.defaultdict(list)
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.val].append((node.left.val, 'L'))
                graph[node.left.val].append((node.val, 'U'))
                queue.append(node.left)

            if node.right:
                graph[node.val].append((node.right.val, 'R'))
                graph[node.right.val].append((node.val, 'U'))
                queue.append(node.right)

        queue = collections.deque([(startValue, '')]) \
            if graph[startValue] else collections.deque([])
        visited = {startValue}

        while queue:
            node, path = queue.popleft()

            if node == destValue:
                return path

            for neighbour, direction in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + direction))

        return ''
