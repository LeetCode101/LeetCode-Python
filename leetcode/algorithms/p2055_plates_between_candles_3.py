from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) \
            -> List[int]:
        n = len(s)
        candle_sum_left = [0] * n
        nearest_candle_left = [0] * n
        nearest_candle_right = [0] * n
        result = []

        for i in range(n):
            candle_sum_left[i] = (1 if s[i] == '|' else 0) + (
                candle_sum_left[i - 1] if i - 1 >= 0 else 0)
            nearest_candle_left[i] = i if s[i] == '|' else (
                nearest_candle_left[i - 1] if i - 1 >= 0 else -1)

        for i in range(n - 1, -1, -1):
            nearest_candle_right[i] = i if s[i] == '|' else (
                nearest_candle_right[i + 1] if i + 1 < n else -1)

        for start, end in queries:
            left = nearest_candle_right[start]
            right = nearest_candle_left[end]

            if left < right and left != -1 and right != -1:
                window_size = right - left + 1
                candle_size = candle_sum_left[right] - (
                    candle_sum_left[left - 1] if left - 1 >= 0 else 0)
                result.append(window_size - candle_size)
            else:
                result.append(0)

        return result
