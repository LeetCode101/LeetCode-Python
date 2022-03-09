import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        last_train_required_time = abs(hour - math.floor(hour))
        last_train_required_speed = \
            math.ceil(dist[-1] / last_train_required_time) \
            if last_train_required_time > 0 else 0
        left, right = 1, max(max(dist), last_train_required_speed)

        while left < right:
            middle = left + (right - left) // 2
            cost = self._get_cost(dist, middle)

            if cost > hour:
                left = middle + 1
            else:
                right = middle

        return left

    def _get_cost(self, dist, speed):
        cost = 0

        for i in range(len(dist) - 1):
            cost += math.ceil(dist[i] / speed)

        cost += dist[-1] / speed

        return cost
