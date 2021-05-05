from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self._build_tree(preorder, 0, len(preorder) - 1,
                                inorder, 0, len(inorder) - 1)

    def _build_tree(self, preorder: List[int], preorder_left: int,
                    preorder_right: int, inorder: List[int],
                    inorder_left: int, inorder_right: int) -> TreeNode:
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return None

        root_value = preorder[preorder_left]
        root = TreeNode(root_value)
        inorder_root_index = -1

        for i in range(inorder_left, inorder_right + 1):
            if inorder[i] == root_value:
                inorder_root_index = i

                break

        left_tree_length = inorder_root_index - inorder_left
        root.left = self._build_tree(
            preorder, preorder_left + 1, preorder_left + left_tree_length,
            inorder, inorder_left, inorder_root_index - 1)
        root.right = self._build_tree(
            preorder, preorder_left + left_tree_length + 1, preorder_right,
            inorder, inorder_root_index + 1, inorder_right)

        return root
