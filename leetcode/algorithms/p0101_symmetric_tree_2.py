from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue1 = deque([root.left])
        queue2 = deque([root.right])

        while queue1 and queue2:
            left = queue1.pop()
            right = queue2.pop()

            if left is None and right is None:
                continue
            elif left and right:
                if left.val != right.val:
                    return False

                queue1.append(left.left)
                queue1.append(left.right)
                queue2.append(right.right)
                queue2.append(right.left)
            else:
                return False

        return True
