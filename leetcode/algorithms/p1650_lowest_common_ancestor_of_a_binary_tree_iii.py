class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set()

        while p or q:
            if p and q and p.parent is q.parent:
                return p.parent

            if p and p in parents:
                return p

            if q and q in parents:
                return q

            if p:
                parents.add(p)
                p = p.parent

            if q:
                parents.add(q)
                q = q.parent
