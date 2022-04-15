import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        queue = collections.deque([(root, None, None)])

        while queue:
            node, parent, grand_parent = queue.popleft()
            new_grand_parent = parent
            new_parent = node if node.val & 1 == 0 else None

            if grand_parent:
                total += node.val

            if node.left:
                queue.append((node.left, new_parent, new_grand_parent))

            if node.right:
                queue.append((node.right, new_parent, new_grand_parent))

        return total
