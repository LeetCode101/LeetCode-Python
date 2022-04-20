class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 1, 0

        if n == 0:
            return c
        elif n == 1:
            return b
        elif n == 2:
            return a

        for _ in range(n - 2):
            a, b, c = a + b + c, a, b

        return a
