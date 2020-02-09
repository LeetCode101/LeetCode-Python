# Memory Limit Exceeded!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        max_length = 1

        for i in range(0, n):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[j] not in set(s[j - dp[i][j - 1]:j]):
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    dp[i][j] = 1

                max_length = max(max_length, dp[i][j])

        return max_length
