from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) \
            -> List[TreeNode]:
        result = []

        if root.val not in to_delete:
            result.append(root)

        self._dfs(root, set(to_delete), result)

        return result

    def _dfs(self, root, delete_set, result):
        if not root:
            return None

        root.left = self._dfs(root.left, delete_set, result)
        root.right = self._dfs(root.right, delete_set, result)

        if root.val in delete_set:
            if root.left:
                result.append(root.left)

            if root.right:
                result.append(root.right)

            return None

        return root
