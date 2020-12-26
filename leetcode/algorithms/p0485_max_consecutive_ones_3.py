from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0

        for n in nums:
            length_so_far *= n
            length_so_far += n
            max_length = max(max_length, length_so_far)

        return max_length
