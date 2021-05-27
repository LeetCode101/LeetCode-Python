from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []

        self._postorder(root, values)

        return values

    def _postorder(self, root, values):
        if not root:
            return

        if root.children:
            for child in root.children:
                self._postorder(child, values)

        values.append(root.val)
