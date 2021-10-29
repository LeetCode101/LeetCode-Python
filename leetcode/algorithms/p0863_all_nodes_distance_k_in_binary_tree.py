from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        target_info = self._find_target(root, target)

        if not target_info:
            return []

        target_depth, target_dx = target_info
        stack = [(root, 0, 0)]
        result = []

        while stack:
            node, depth, dx = stack.pop()

            if dx * target_dx <= 0 and k == depth + target_depth:
                result.append(node.val)
            elif dx * target_dx > 0 and abs(target_depth - depth) == k:
                result.append(node.val)

            if node.left:
                stack.append((node.left, depth + 1, dx - 1))

            if node.right:
                stack.append((node.right, depth + 1, dx + 1))

        return result

    def _find_target(self, root, target):
        stack = [(root, 0, 0)]

        while stack:
            node, depth, dx = stack.pop()

            if node == target:
                return depth, dx

            if node.left:
                stack.append((node.left, depth + 1, dx - 1))

            if node.right:
                stack.append((node.right, depth + 1, dx + 1))

        return None
