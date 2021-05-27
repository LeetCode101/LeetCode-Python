from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        values = []

        while stack:
            node = stack.pop()

            values.append(node.val)

            if node.children:
                for i in range(len(node.children) - 1, -1, -1):
                    stack.append(node.children[i])

        return values
