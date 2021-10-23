from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        n = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])

            while stack and stack[-1].val < child.val:
                node = stack.pop()

            if node.val > child.val:
                node.left = child
            else:
                node.right = child

            stack.append(child)

        return root
