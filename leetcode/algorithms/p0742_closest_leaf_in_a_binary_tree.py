import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        queue = collections.deque([root])
        target = None
        parent_map = {root: None}

        while queue:
            node = queue.popleft()

            if node.val == k:
                target = node

            if node.left:
                queue.append(node.left)
                parent_map[node.left] = node

            if node.right:
                queue.append(node.right)
                parent_map[node.right] = node

        queue = collections.deque([target])
        visited = {target.val}

        while queue:
            node = queue.popleft()

            if not node.left and not node.right:
                return node.val

            if node.left and node.left.val not in visited:
                queue.append(node.left)
                visited.add(node.left.val)

            if node.right and node.right.val not in visited:
                queue.append(node.right)
                visited.add(node.right.val)

            if parent_map[node] and parent_map[node].val not in visited:
                queue.append(parent_map[node])
                visited.add(parent_map[node].val)
