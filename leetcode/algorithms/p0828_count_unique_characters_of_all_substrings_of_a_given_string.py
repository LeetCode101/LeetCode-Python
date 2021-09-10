class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        dp = [[[0, set()] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = [1, set(s[i])]

            for j in range(i + 1, n):
                prev_unique_count = dp[i][j - 1][0]
                prev_unique_letters = dp[i][j - 1][1]

                if s[j] in prev_unique_letters:
                    dp[i][j] = [prev_unique_count - 1, prev_unique_letters - {s[j]}]
                else:
                    dp[i][j] = [prev_unique_count + 1, prev_unique_letters | {s[j]}]

        count = 0

        for i in range(n):
            for j in range(n):
                count += dp[i][j][0]

        return count
