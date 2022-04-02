import bisect
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int],
                      pills: int, strength: int) -> int:
        low, high = 0, min(len(tasks), len(workers))
        sorted_tasks = sorted(tasks)
        sorted_workers = sorted(workers)

        while low < high:
            middle = low + (high - low) // 2 + 1

            if self._is_valid(sorted_tasks, sorted_workers,
                              pills, strength, middle):
                low = middle
            else:
                high = middle - 1

        return low

    def _is_valid(self, sorted_tasks, sorted_workers, pills, strength, k):
        workers = sorted_workers[-k:]
        tasks = reversed(sorted_tasks[:k])

        for task in tasks:
            if task <= workers[-1]:
                workers.pop()
            elif pills > 0 and task <= workers[-1] + strength:
                pills -= 1
                i = bisect.bisect_left(workers, task - strength)
                workers.pop(i)
            else:
                return False

        return True
