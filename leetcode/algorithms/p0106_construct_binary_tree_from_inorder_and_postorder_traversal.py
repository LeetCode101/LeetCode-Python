from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self._build_tree(inorder, 0, len(inorder) - 1,
                                postorder, 0, len(postorder) - 1)

    def _build_tree(self, inorder, inorder_start, inorder_end,
                    postorder, postorder_start, postorder_end):
        if inorder_start > inorder_end or postorder_start > postorder_end:
            return None

        root_value = postorder[postorder_end]
        root = TreeNode(root_value)
        inorder_root_index = -1

        for i in range(inorder_start, inorder_end + 1):
            if inorder[i] == root_value:
                inorder_root_index = i

                break

        left_tree_size = inorder_root_index - inorder_start
        root.left = self._build_tree(
            inorder, inorder_start, inorder_root_index - 1,
            postorder, postorder_start, postorder_start + left_tree_size - 1)
        root.right = self._build_tree(
            inorder, inorder_root_index + 1, inorder_end,
            postorder, postorder_start + left_tree_size, postorder_end - 1)

        return root
