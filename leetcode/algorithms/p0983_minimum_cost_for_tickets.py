from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        days_set = set(days)

        for i in range(1, last_day + 1):
            if i not in days_set:
                dp[i] = dp[i - 1]

                continue

            one_day_cost = costs[0] + dp[i - 1]
            seven_day_cost = costs[1] + dp[max(i - 7, 0)]
            thirty_day_cost = costs[2] + dp[max(i - 30, 0)]
            dp[i] = min(one_day_cost, seven_day_cost, thirty_day_cost)

        return dp[-1]
