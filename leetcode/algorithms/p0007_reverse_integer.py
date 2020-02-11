class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        result = 0
        max_value = pow(2, 31) - 1
        min_value = -max_value - 1

        while x > 0:
            result *= 10
            result += x % 10
            x //= 10

            if result < min_value or result > max_value:
                return 0

        return -result if is_negative else result
