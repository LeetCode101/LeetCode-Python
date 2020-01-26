from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        self.dfs(root, 1, result)

        return result


    def dfs(self, root: TreeNode, level: int, result: List[List[int]]) -> None:
        if not root:
            return

        if level > len(result):
            result.append([])

        result[level - 1].append(root.val)

        self.dfs(root.left, level + 1, result)
        self.dfs(root.right, level + 1, result)
