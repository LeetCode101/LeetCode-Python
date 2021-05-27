from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        values = deque([])
        stack = [root]

        while stack:
            node = stack.pop()

            values.appendleft(node.val)

            if node.children:
                for child in node.children:
                    stack.append(child)

        return list(values)
