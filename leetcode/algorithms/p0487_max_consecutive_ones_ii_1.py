from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        prev_length = -1

        for n in nums:
            if n == 1:
                length_so_far += 1
            else:
                prev_length, length_so_far = length_so_far, 0

            max_length = max(length_so_far + prev_length + 1, max_length)

        return max_length
