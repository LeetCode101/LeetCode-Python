from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []

        if not root:
            return []

        queue = deque([(root, root.val, [root.val])])

        while queue:
            node, sum_so_far, path_so_far = queue.popleft()

            if not node.left and not node.right and sum_so_far == targetSum:
                paths.append(path_so_far)

            if node.left:
                queue.append((node.left, sum_so_far + node.left.val,
                              path_so_far + [node.left.val]))

            if node.right:
                queue.append((node.right, sum_so_far + node.right.val,
                              path_so_far + [node.right.val]))

        return paths
