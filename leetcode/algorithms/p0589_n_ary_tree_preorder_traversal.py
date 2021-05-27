from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []

        self._preorder(root, values)

        return values

    def _preorder(self, root, values):
        if not root:
            return

        values.append(root.val)

        if root.children:
            for child in root.children:
                self._preorder(child, values)
