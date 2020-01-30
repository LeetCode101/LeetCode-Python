class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        start, end = 0, 0
        dp = [[False for _ in range(length)] for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

            for j in range(i):
                dp[j][i] = s[i] == s[j] and (i - j == 1 or dp[j + 1][i - 1])

                if dp[j][i] and i - j > end - start:
                    start, end = j, i

        return s[start:end + 1]
