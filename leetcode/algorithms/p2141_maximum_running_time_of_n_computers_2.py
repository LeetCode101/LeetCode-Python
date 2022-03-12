from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_energy = sum(batteries)
        left, right = 0, total_energy // n

        while left < right:
            middle = left + (right - left) // 2 + 1

            if self._can_run_all_computers(n, middle, batteries):
                left = middle
            else:
                right = middle - 1

        return left

    def _can_run_all_computers(self, n, time, batteries):
        required_batteries = n * time
        current_batteries = 0

        for battery in batteries:
            if battery < time:
                current_batteries += battery
            else:
                current_batteries += time

            if current_batteries >= required_batteries:
                return True

        return current_batteries >= required_batteries
