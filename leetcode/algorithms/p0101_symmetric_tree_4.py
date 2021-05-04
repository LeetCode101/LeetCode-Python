class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack1 = [root.left]
        stack2 = [root.right]

        while stack1 and stack2:
            left = stack1.pop()
            right = stack2.pop()

            if left is None and right is None:
                continue
            elif left and right:
                if left.val != right.val:
                    return False

                stack1.append(left.left)
                stack1.append(left.right)
                stack2.append(right.right)
                stack2.append(right.left)
            else:
                return False

        return True
