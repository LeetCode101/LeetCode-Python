import sys
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1, max2, max3 = -sys.maxsize, -sys.maxsize, -sys.maxsize

        for n in nums:
            if n > max1:
                max3, max2, max1 = max2, max1, n
            elif max2 < n < max1:
                max3, max2 = max2, n
            elif max3 < n < max2:
                max3 = n

        return max3 if max3 != -sys.maxsize else max1
