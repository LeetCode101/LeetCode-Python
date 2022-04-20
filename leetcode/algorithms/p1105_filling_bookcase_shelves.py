from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + books[i - 1][1]
            width_sum = 0
            height = 0

            for j in range(i, -1, -1):
                width_sum += books[j - 1][0]

                if width_sum > shelfWidth:
                    break

                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[-1]
