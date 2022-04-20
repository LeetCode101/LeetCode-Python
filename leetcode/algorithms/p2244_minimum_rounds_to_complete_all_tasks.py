import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = collections.Counter(tasks)
        round = 0

        dp = [0] * (max(4, max(counter.values())) + 1)
        dp[1] = 0
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2

        for count in counter.values():
            current_round = self._get_round(dp, count)

            if current_round > 0:
                round += current_round
            else:
                return -1

        return round

    def _get_round(self, dp, n):
        if n <= 4:
            return dp[n]

        if dp[n] > 0:
            return dp[n]

        for i in range(5, n + 1):
            dp[i] = 1 + min(dp[i - 2], dp[i - 3])

        return dp[n]
