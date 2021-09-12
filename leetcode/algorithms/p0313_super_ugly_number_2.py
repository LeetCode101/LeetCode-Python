from typing import List


# Time Limit Exceeded!
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        uglies = [0] * len(primes)

        for i in range(1, n):
            ugly = min(map(lambda x: dp[uglies[x]] * primes[x],
                           range(len(primes))))
            dp[i] = ugly

            for j in range(len(primes)):
                if ugly == dp[uglies[j]] * primes[j]:
                    uglies[j] += 1

        return dp[-1]
