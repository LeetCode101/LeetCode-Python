# Time Limit Exceeded!
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True

        for i in range(minJump, n):
            if s[i] != '0':
                continue

            for j in range(max(i - maxJump, 0), i - minJump + 1):
                if dp[j]:
                    dp[i] = True

                    break

        return dp[-1]
