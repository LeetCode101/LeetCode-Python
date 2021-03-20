# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher,
# otherwise return 0
def guess(num: int) -> int:
    if num > 10:
        return -1
    elif num < 10:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            middle = low + (high - low) // 2
            compare = guess(middle)

            if compare == 1:
                low = middle + 1
            elif compare == -1:
                high = middle - 1
            else:
                return middle
