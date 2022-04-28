import collections


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = collections.defaultdict(int)
        streak = 0

        for i in range(len(p)):
            if (ord(p[i - 1]) - 96) % 26 == (ord(p[i]) - 97):
                streak += 1
            else:
                streak = 1

            dp[p[i]] = max(dp[p[i]], streak)

        return sum(dp.values())
