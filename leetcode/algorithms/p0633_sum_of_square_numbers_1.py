import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()

        for i in range(0, math.ceil(math.sqrt(c) + 1)):
            square = i * i
            target = c - square

            if target in squares or 2 * square == c:
                return True

            squares.add(square)

        return False
