from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) \
            -> TreeNode:
        return self._build_tree(pre, 0, len(pre) - 1,
                                post, 0, len(post) - 1)

    def _build_tree(self, pre, pre_start, pre_end,
                    post, post_start, post_end):
        if pre_start > pre_end or post_start > post_end:
            return None

        root = TreeNode(pre[pre_start])

        if pre_start == pre_end:
            return root

        left_tree_root_value = pre[pre_start + 1]
        post_left_tree_root_index = -1

        for i, n in enumerate(post):
            if n == left_tree_root_value:
                post_left_tree_root_index = i

                break

        left_tree_size = post_left_tree_root_index - post_start + 1

        root.left = self._build_tree(
            pre, pre_start + 1, pre_start + left_tree_size,
            post, post_start, post_start + left_tree_size - 1)
        root.right = self._build_tree(
            pre, pre_start + left_tree_size + 1, pre_end,
            post, post_start + left_tree_size, post_end - 1)

        return root
