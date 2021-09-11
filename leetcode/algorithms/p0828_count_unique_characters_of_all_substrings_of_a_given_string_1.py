# Time Limit Exceeded!
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        dp = [[[0, set(), set()] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = [1, set(s[i]), set()]

            for j in range(i + 1, n):
                prev_unique_count = dp[i][j - 1][0]
                prev_unique_letters = dp[i][j - 1][1]
                prev_duplicate_letters = dp[i][j - 1][2]

                if s[j] in prev_unique_letters:
                    dp[i][j] = [prev_unique_count - 1,
                                prev_unique_letters - {s[j]},
                                prev_duplicate_letters | {s[j]}]
                elif s[j] in prev_duplicate_letters:
                    dp[i][j] = [prev_unique_count,
                                prev_unique_letters,
                                prev_duplicate_letters]
                else:
                    dp[i][j] = [prev_unique_count + 1,
                                prev_unique_letters | {s[j]},
                                prev_duplicate_letters]

        count = 0

        for i in range(n):
            for j in range(n):
                count += dp[i][j][0]

        return count
