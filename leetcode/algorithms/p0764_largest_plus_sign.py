from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(4):
                    dp[i][j][k] = 1

        for x, y in mines:
            for k in range(4):
                dp[x][y][k] = 0

        for i in range(1, n):
            for j in range(1, n):
                if dp[i][j][0] == 0:
                    continue

                dp[i][j][0] = dp[i][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j][1] + 1

        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if dp[i][j][2] == 0:
                    continue

                dp[i][j][2] = dp[i][j + 1][2] + 1
                dp[i][j][3] = dp[i + 1][j][3] + 1

        largest = 0

        for i in range(n):
            for j in range(n):
                largest = max(largest, min(dp[i][j]))

        return largest
