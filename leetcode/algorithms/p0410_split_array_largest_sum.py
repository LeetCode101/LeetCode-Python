from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            middle = low + (high - low) // 2
            count, current = 1, 0

            for num in nums:
                current += num

                if current > middle:
                    current = num
                    count += 1

            if count > m:
                low = middle + 1
            else:
                high = middle

        return low
