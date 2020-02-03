from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1)

    def build(self, preorder: List[int], preorder_left: int,
              preorder_right: int, inorder: List[int],
              inorder_left: int, inorder_right: int) -> TreeNode:
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return None

        root_value = preorder[preorder_left]
        i = next(j for j in range(inorder_left, inorder_right + 1)
                 if inorder[j] == root_value)

        left_tree_length = i - inorder_left
        root = TreeNode(root_value)
        root.left = self.build(
            preorder, preorder_left + 1, preorder_left + left_tree_length,
            inorder, inorder_left, i - 1)
        root.right = self.build(
            preorder, preorder_left + left_tree_length + 1, preorder_right,
            inorder, i + 1, inorder_right)

        return root
