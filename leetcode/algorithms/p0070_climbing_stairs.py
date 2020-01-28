class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        step = 0
        prev_prev, prev = 1, 2

        for i in range(2, n):
            step = prev_prev + prev
            prev_prev, prev = prev, step

        return step
