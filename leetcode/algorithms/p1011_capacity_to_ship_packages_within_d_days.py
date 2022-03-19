from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low < high:
            middle = low + (high - low) // 2
            required_days = self._count_days(weights, middle)

            if required_days > days:
                low = middle + 1
            else:
                high = middle

        return low

    def _count_days(self, weights, capacity):
        days = 0
        current_capacity = 0

        for weight in weights:
            if current_capacity + weight > capacity:
                days += 1
                current_capacity = weight
            else:
                current_capacity += weight

        if current_capacity > 0:
            days += 1

        return days
