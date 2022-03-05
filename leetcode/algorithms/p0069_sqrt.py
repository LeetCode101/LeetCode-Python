class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x

        while low <= high:
            middle = low + (high - low) // 2
            square = middle * middle

            if square > x:
                high = middle - 1
            elif square < x:
                low = middle + 1
            else:
                return middle

        return high
