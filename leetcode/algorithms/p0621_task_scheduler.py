import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [[-count, task] for task, count in counter.items()]
        heapq.heapify(heap)

        units = 0

        while heap:
            current_tasks = []
            current_unit = 0

            for _ in range(n + 1):
                if not heap:
                    break

                current_tasks.append(heapq.heappop(heap))
                current_unit += 1

            for count, task in current_tasks:
                if count + 1 < 0:
                    heapq.heappush(heap, [count + 1, task])

            units += (n + 1) if heap else current_unit

        return units
