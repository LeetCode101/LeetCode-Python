class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_length = 0
        stack = [(root, 1)]

        while stack:
            node, length_so_far = stack.pop()
            max_length = max(max_length, length_so_far)

            for child in [node.left, node.right]:
                if not child:
                    continue

                length = length_so_far + 1 if child.val == node.val + 1 else 1

                stack.append((child, length))

        return max_length
