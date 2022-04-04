from typing import List


# Time Limit Exceeded!
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) \
            -> List[int]:
        n = len(s)
        candle_sum_left = [0] * n
        candle_sum_right = [0] * n
        result = []

        for i in range(n):
            candle_sum_left[i] = (1 if s[i] == '|' else 0) + (
                candle_sum_left[i - 1] if i - 1 >= 0 else 0)

        for i in range(n - 1, -1, -1):
            candle_sum_right[i] = (1 if s[i] == '|' else 0) + (
                candle_sum_right[i + 1] if i + 1 < n else 0)

        for start, end in queries:
            count = 0

            for i in range(start, end + 1):
                if s[i] == '|':
                    continue

                left = (candle_sum_left[i - 1] if i - 1 >= 0 else 0) - (
                    candle_sum_left[start - 1] if start - 1 >= 0 else 0)
                right = (candle_sum_right[i + 1] if i + 1 < n else 0) - (
                    candle_sum_right[end + 1] if end + 1 < n else 0)
                count += 1 if left >= 1 and right >= 1 else 0

            result.append(count)

        return result
