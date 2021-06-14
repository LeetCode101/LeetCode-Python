from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.accumulated_weight_sum = [i for i in w]

        for i in range(1, len(w)):
            self.accumulated_weight_sum[i] += \
                self.accumulated_weight_sum[i - 1]

    def pickIndex(self) -> int:
        low, high = 0, len(self.accumulated_weight_sum) - 1
        target = randint(1, self.accumulated_weight_sum[-1])

        while low < high:
            middle = low + (high - low) // 2

            if self.accumulated_weight_sum[middle] == target:
                return middle
            elif self.accumulated_weight_sum[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low
