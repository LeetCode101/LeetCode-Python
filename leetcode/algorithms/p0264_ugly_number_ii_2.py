class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        ugly_2 = ugly_3 = ugly_5 = 0

        for i in range(1, n):
            ugly = min(dp[ugly_2] * 2, dp[ugly_3] * 3, dp[ugly_5] * 5)
            dp[i] = ugly

            if ugly == dp[ugly_2] * 2:
                ugly_2 += 1

            if ugly == dp[ugly_3] * 3:
                ugly_3 += 1

            if ugly == dp[ugly_5] * 5:
                ugly_5 += 1

        return dp[-1]
