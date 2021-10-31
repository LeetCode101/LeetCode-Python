class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        stack = [(root, 1, [])]
        max_depth = 0
        candidates = []

        while stack:
            node, depth, paths = stack.pop()

            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    candidates = [paths + [node]]
                elif depth == max_depth:
                    candidates.append(paths + [node])

            if node.left:
                stack.append((node.left, depth + 1, paths + [node]))

            if node.right:
                stack.append((node.right, depth + 1, paths + [node]))

        if len(candidates) == 1:
            return candidates[0][-1]

        for i in range(len(candidates[0])):
            for j in range(1, len(candidates)):
                if candidates[j][i] != candidates[j - 1][i]:
                    return candidates[0][i - 1]
