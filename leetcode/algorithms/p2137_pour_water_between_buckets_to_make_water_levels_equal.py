from typing import List


class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        low, high = min(buckets), max(buckets)

        while high - low >= 1e-5:
            middle = low + (high - low) / 2

            if self._is_valid(buckets, middle, loss):
                low = middle
            else:
                high = middle

        return low

    def _is_valid(self, buckets, gallon, loss):
        count = 0

        for bucket in buckets:
            if bucket >= gallon:
                count += (bucket - gallon) * (1 - loss / 100)
            else:
                count -= (gallon - bucket)

        return count >= 0
