class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        while a is not b:
            a = q if a.parent is None else a.parent
            b = p if b.parent is None else b.parent

        return a
