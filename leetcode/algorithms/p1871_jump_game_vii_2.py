from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        dp = [False] * n
        dp[0] = True
        queue = deque([0])

        for i in range(minJump, n):
            if queue and queue[0] < i - maxJump:
                queue.popleft()

            if s[i] == '0' and queue and i - queue[0] >= minJump:
                dp[i] = True
                queue.append(i)

        return dp[-1]
