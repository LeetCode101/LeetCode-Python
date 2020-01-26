class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.pow(x, n) if n > 0 else self.pow(1 / x, -n)

    def pow(self, x: float, n: int) -> float:
        result = 1

        while n > 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n = n // 2

        return result
