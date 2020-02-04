from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3

        for number in nums:
            counts[number] += 1

        j = 0

        for i, count in enumerate(counts):
            for _ in range(count):
                nums[j] = i
                j += 1
