import sys
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = -sys.maxsize

        for node in preorder:
            if node < lower_bound:
                return False

            while stack and node > stack[-1]:
                lower_bound = stack.pop()

            stack.append(node)

        return True
