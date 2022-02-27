import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, math.ceil(math.sqrt(c))

        while left <= right:
            square_sum = left * left + right * right

            if square_sum < c:
                left += 1
            elif square_sum > c:
                right -= 1
            else:
                return True

        return False
