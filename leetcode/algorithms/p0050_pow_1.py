class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.pow(x, abs(n)) if n >= 0 else self.pow(1 / x, abs(n))

    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, (n - 1) // 2) * x
