class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        prev_prev = 0
        prev = 1
        current = 0

        for _ in range(2, N + 1):
            current = prev_prev + prev
            prev_prev = prev
            prev = current

        return current
