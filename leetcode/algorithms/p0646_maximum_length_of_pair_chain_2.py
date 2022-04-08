import sys
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        tail = -sys.maxsize
        max_length = 0

        for start, end in sorted_pairs:
            if start > tail:
                tail = end
                max_length += 1

        return max_length
