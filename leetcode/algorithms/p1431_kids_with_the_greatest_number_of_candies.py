from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) \
            -> List[bool]:
        max_candies = max(candies)

        return list(map(lambda x: x + extraCandies >= max_candies, candies))
