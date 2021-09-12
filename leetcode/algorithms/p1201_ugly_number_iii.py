class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        if a == 1 or b == 1 or c == 1:
            return n

        lcm_ab = self._lcm(a, b)
        lcm_ac = self._lcm(a, c)
        lcm_bc = self._lcm(b, c)
        lcm_abc = self._lcm(lcm_ab, c)
        left = 0
        right = n * min(a, b, c)

        while left <= right:
            middle = left + (right - left) // 2
            count = middle // a + middle // b + middle // c \
                - middle // lcm_ab - middle // lcm_ac - middle // lcm_bc \
                + middle // lcm_abc

            if count == n:
                if middle % a == 0 or middle % b == 0 or middle % c == 0:
                    return middle
                else:
                    right = middle - 1
            elif count > n:
                right = middle - 1
            else:
                left = middle + 1

        return left

    def _lcm(self, a, b):
        return a * b // self._gcd(a, b)

    def _gcd(self, a, b):
        if a == 0:
            return b

        return self._gcd(b % a, a)
