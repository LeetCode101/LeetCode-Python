class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def __init__(self):
        self.max_length = 0

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self._dfs(root)

        return self.max_length

    def _dfs(self, root):
        if not root:
            return 0

        max1, max2 = 0, 0

        for child in root.children:
            height = self._dfs(child)

            if height > max1:
                max1, max2 = height, max1
            elif height > max2:
                max2 = height

        self.max_length = max(self.max_length, max1 + max2)

        return max1 + 1
