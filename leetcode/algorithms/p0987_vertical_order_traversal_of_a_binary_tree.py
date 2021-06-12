import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        columns = collections.defaultdict(list)
        queue = [(root, 0, 0)]

        for node, row, column in queue:
            if node:
                columns[column].append((row, node.val))
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        return [self._get_sorted_row(columns[row]) for row in sorted(columns)]

    def _get_sorted_row(self, row):
        return [x[1] for x in sorted(row)]
