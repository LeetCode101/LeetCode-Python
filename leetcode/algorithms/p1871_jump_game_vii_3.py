class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        prev_reachable_count = 0

        for i in range(minJump, n):
            prev_reachable_count += 1 if dp[i - minJump] else 0

            if i > maxJump:
                prev_reachable_count -= 1 if dp[i - maxJump - 1] else 0

            dp[i] = prev_reachable_count > 0 and s[i] == '0'

        return dp[-1]
