from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_factors = sorted(g)
        sorted_cookies = sorted(s)
        count = 0
        i, n = 0, len(sorted_cookies)

        for factor in sorted_factors:
            while i < n and sorted_cookies[i] < factor:
                i += 1

            satisfied = i < n

            if satisfied:
                i += 1
                count += 1
            else:
                break

        return count
