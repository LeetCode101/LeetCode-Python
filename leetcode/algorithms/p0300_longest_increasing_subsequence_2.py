from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails = []

        for number in nums:
            if not tails or number > tails[-1]:
                tails.append(number)
            else:
                low, high = 0, len(tails) - 1

                while low <= high:
                    middle = (low + high) // 2

                    if tails[middle] < number:
                        low = middle + 1
                    else:
                        high = middle - 1

                tails[low] = number

        return len(tails)
