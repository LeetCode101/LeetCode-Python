# Memory Limit Exceeded!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_length = 1

        for i in range(0, n):
            dp[i][i] = True

            for j in range(i + 1, n):
                if dp[i][j - 1] and s[j] not in set(s[i:j]):
                    dp[i][j] = True

                if dp[i][j]:
                    max_length = max(max_length, j - i + 1)

        return max_length
