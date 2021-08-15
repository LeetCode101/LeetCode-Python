class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = list(range(n))

        for middle in range(1, n):
            self._dp(middle, middle, dp, s)
            self._dp(middle - 1, middle, dp, s)

        return dp[-1]

    def _dp(self, start, end, dp, s):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            dp[end] = min(dp[end], 0 if start == 0 else dp[start - 1] + 1)
            start -= 1
            end += 1
