class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return k

        same_color_count, different_color_count = k, k * (k - 1)

        for _ in range(3, n + 1):
            same_color_count, different_color_count = \
                different_color_count, \
                same_color_count * (k - 1) + different_color_count * (k - 1)

        return same_color_count + different_color_count
