class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1 if s[0] != '0' else 0

        for i in range(1, n):
            one_digit = int(s[i:i + 1])
            two_digits = int(s[i - 1:i + 1])

            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]
