from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q)])

        while queue:
            a, b = queue.popleft()

            if a and b:
                if a.val != b.val:
                    return False

                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
            elif not a and not b:
                continue
            else:
                return False

        return True
