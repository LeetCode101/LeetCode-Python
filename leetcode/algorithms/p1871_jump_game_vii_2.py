from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if not s:
            return False

        n = len(s)
        queue = deque([0])

        for i in range(1, n):
            if queue and queue[0] < i - maxJump:
                queue.popleft()

            if s[i] == '0' and queue and queue[0] <= i - minJump:
                queue.append(i)

        return len(queue) > 0 and queue[-1] == n - 1
