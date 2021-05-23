from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        paths = {}
        duplicates = []

        self._get_path(root, paths)

        for nodes in paths.values():
            if len(nodes) > 1:
                duplicates.append(nodes[0])

        return duplicates

    def _get_path(self, root, paths):
        if not root:
            return ''

        left_path = self._get_path(root.left, paths)
        right_path = self._get_path(root.right, paths)
        full_path = 'l' + left_path + 'c' + str(root.val) + 'r' + right_path

        if full_path in paths:
            paths[full_path].append(root)
        else:
            paths[full_path] = [root]

        return full_path
