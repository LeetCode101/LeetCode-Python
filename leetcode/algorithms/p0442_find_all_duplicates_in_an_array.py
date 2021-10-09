from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numbers = set()
        duplicates = []

        for n in nums:
            if n in numbers:
                duplicates.append(n)
            else:
                numbers.add(n)

        return duplicates
