import bisect
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        sorted_events = sorted(events)
        starts = [x for x, _, _ in sorted_events]

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                next_event = bisect.bisect_right(starts, sorted_events[i][1])
                dp[i][j] = max(dp[i + 1][j],
                               sorted_events[i][2] + dp[next_event][j - 1])

        return dp[0][k]
