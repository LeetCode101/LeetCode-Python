from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) \
            -> bool:
        if not root1 and not root2:
            return True

        stack1 = [root1]
        stack2 = [root2]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if not self._equal(node1, node2):
                return False

            left1 = node1.left
            right1 = node1.right
            left2 = node2.left
            right2 = node2.right

            if left1:
                stack1.append(left1)

            if right1:
                stack1.append(right1)

            if self._equal(left1, left2) and self._equal(right1, right2):
                if left2:
                    stack2.append(left2)

                if right2:
                    stack2.append(right2)
            elif self._equal(left1, right2) and self._equal(right1, left2):
                if right2:
                    stack2.append(right2)

                if left2:
                    stack2.append(left2)
            else:
                return False

        return not stack1 and not stack2

    def _equal(self, root1, root2):
        if root1 and root2:
            return root1.val == root2.val
        else:
            return not root1 and not root2
