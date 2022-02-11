from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        sorted_ratings = sorted([(rating, i) for i, rating
                                 in enumerate(ratings)])
        n = len(ratings)
        candies = [0] * n

        for rating, i in sorted_ratings:
            left, right = 0, 0

            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                left = candies[i - 1]

            if i + 1 < n and ratings[i] > ratings[i + 1]:
                right = candies[i + 1]

            candies[i] = 1 + max(left, right)

        return sum(candies)
