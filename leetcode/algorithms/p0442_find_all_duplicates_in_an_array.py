import collections
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = collections.defaultdict(int)
        duplicates = []

        for n in nums:
            if counter[n] == 1:
                duplicates.append(n)
            else:
                counter[n] = 1

        return duplicates
