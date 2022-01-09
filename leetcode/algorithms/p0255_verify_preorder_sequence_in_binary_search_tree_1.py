import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self._verify(preorder, 0, len(preorder) - 1,
                            -sys.maxsize, sys.maxsize)

    def _verify(self, preorder, start, end, min_value, max_value):
        if start > end:
            return True

        root = preorder[start]

        if root < min_value or root > max_value:
            return False

        i = start + 1

        while i <= end and preorder[i] <= root:
            i += 1

        return self._verify(preorder, start + 1, i - 1, min_value, root) \
            and self._verify(preorder, i, end, root, max_value)
