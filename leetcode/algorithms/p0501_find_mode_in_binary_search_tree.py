from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        max_length = 0
        current_length = 0
        prev_value = None
        current = root
        stack = []

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            current_value = node.val

            if prev_value == current_value:
                current_length += 1
            else:
                if max_length == current_length:
                    result.append(prev_value)
                elif max_length < current_length:
                    max_length = current_length
                    result = [prev_value]

                current_length = 1

            prev_value = current_value
            current = node.right

        if max_length == current_length:
            result.append(prev_value)
        elif max_length < current_length:
            result = [prev_value]

        return result
