import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) \
            -> List[int]:
        candles = [i for i, c in enumerate(s) if c == '|']
        result = []

        for start, end in queries:
            i = bisect.bisect_left(candles, start)
            j = bisect.bisect_right(candles, end) - 1

            if i < j:
                window_size = candles[j] - candles[i] + 1
                candle_size = j - i + 1
                result.append(window_size - candle_size)
            else:
                result.append(0)

        return result
