from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) \
            -> List[int]:
        result = [0] * len(queries)
        sorted_items = sorted(items, key=lambda x: x[0])
        sorted_queries = sorted([(x, i) for i, x in enumerate(queries)])
        prev = 0
        max_beauty = 0

        for price, i in sorted_queries:
            j = self._select_right(sorted_items, price, prev)

            for k in range(max(0, prev), j):
                max_beauty = max(max_beauty, sorted_items[k][1])

            result[i] = max_beauty
            prev = j

        return result

    def _select_right(self, items, target, start):
        low, high = start, len(items) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if items[middle][0] <= target:
                low = middle + 1
            else:
                high = middle - 1

        return low
