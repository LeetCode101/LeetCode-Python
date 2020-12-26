from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        consecutive_and = 1

        for n in nums:
            consecutive_and &= n

            if consecutive_and == 1:
                length_so_far += 1
                max_length = max(length_so_far, max_length)
            else:
                length_so_far = 0
                consecutive_and = 1

        return max_length
