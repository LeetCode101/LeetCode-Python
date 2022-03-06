from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)

        while left < right:
            middle = left + (right - left) // 2
            count = self._count_bouquets(bloomDay, middle, k)

            if count >= m:
                right = middle
            else:
                left = middle + 1

        return left

    def _count_bouquets(self, bloom_day, day, k):
        flower = 0
        result = 0

        for x in bloom_day:
            if x > day:
                flower = 0
            else:
                flower += 1

            if flower == k:
                result += 1
                flower = 0

        return result
