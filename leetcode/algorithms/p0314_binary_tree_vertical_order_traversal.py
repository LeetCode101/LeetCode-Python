import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columns = collections.defaultdict(list)
        queue = [(root, 0)]

        for node, i in queue:
            if node:
                columns[i].append(node.val)
                queue.append((node.left, i - 1))
                queue.append((node.right, i + 1))

        return [columns[i] for i in sorted(columns)]
