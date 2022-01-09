import sys
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        i = 0
        lower_bound = -sys.maxsize

        for node in preorder:
            if node < lower_bound:
                return False

            while i > 0 and node > preorder[i - 1]:
                lower_bound = preorder[i - 1]
                i -= 1

            preorder[i] = node
            i += 1

        return True
