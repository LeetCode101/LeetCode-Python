import math


class Solution:
    def isUgly(self, n: int) -> bool:
        while n % 2 == 0:
            n //= 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                if i not in [3, 5]:
                    return False

                n //= 2

        return n == 1 or n in [3, 5]
