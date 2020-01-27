class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num

        while low <= high:
            middle = (low + high) // 2
            square = middle * middle

            if square == num:
                return True
            elif square > num:
                high = middle - 1
            else:
                low = middle + 1

        return False
