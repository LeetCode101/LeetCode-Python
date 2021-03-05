class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self._pow(x, n) if n > 0 else self._pow(1 / x, -n)

    def _pow(self, x: float, n: int) -> float:
        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n = n // 2

        return result
