from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: len(str(x)) & 1 == 0, nums)))
