from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        mapping = {}

        for n in nums:
            if n in mapping:
                continue

            left = mapping.get(n - 1, 0)
            right = mapping.get(n + 1, 0)
            length = left + right + 1
            max_length = max(max_length, length)

            mapping[n] = length
            mapping[n - left] = length
            mapping[n + right] = length

        return max_length
