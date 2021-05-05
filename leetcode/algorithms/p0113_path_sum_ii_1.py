from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []

        self._path_sum(root, targetSum, [], paths)

        return paths

    def _path_sum(self, root, target, path_so_far, paths):
        if not root:
            return
        elif root.left is None and root.right is None:
            if root.val == target:
                paths.append(path_so_far + [root.val])
        else:
            if root.left:
                self._path_sum(root.left, target - root.val,
                               path_so_far + [root.val], paths)

            if root.right:
                self._path_sum(root.right, target - root.val,
                               path_so_far + [root.val], paths)
