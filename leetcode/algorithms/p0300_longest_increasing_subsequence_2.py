from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = []

        for number in nums:
            if not lis or number > lis[-1]:
                lis.append(number)
            else:
                low, high = 0, len(lis) - 1

                while low <= high:
                    middle = (low + high) // 2

                    if lis[middle] < number:
                        low = middle + 1
                    else:
                        high = middle - 1

                lis[low] = number

        return len(lis)
