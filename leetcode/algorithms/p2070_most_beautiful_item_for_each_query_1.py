from typing import List


# Time Limit Exceeded!
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) \
            -> List[int]:
        result = []
        sorted_items = sorted(items, key=lambda x: x[0])

        for price in queries:
            i = self._select_right(sorted_items, price)
            max_beauty = 0

            for j in range(i):
                max_beauty = max(max_beauty, sorted_items[j][1])

            result.append(max_beauty)

        return result

    def _select_right(self, items, target):
        low, high = 0, len(items) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if items[middle][0] <= target:
                low = middle + 1
            else:
                high = middle - 1

        return low
