import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        graph = collections.defaultdict(list)
        leaves = []
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                graph[node.left].append(node)
                queue.append(node.left)

            if node.right:
                graph[node.right].append(node)
                queue.append(node.right)

            if not node.left and not node.right:
                leaves.append(node)

        min_path = ''

        for leaf in leaves:
            path = ''
            node = leaf

            if min_path and chr(node.val + 97) > min_path:
                continue

            while node:
                path += chr(node.val + 97)
                node = graph[node][0] if graph[node] else None

            min_path = path if not min_path else min(min_path, path)

        return min_path
