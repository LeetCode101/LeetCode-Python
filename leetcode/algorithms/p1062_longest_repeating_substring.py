class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        return self._longest_common_subsequence(s, s)

    def _longest_common_subsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

                max_length = max(max_length, dp[i][j])

        return max_length
