import heapq
from typing import List


# Time Limit Exceeded!
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int],
                      pills: int, strength: int) -> int:
        task_heap = tasks[:]
        worker_heap = [(x, 0) for x in workers]
        heapq.heapify(task_heap)
        heapq.heapify(worker_heap)

        return self._assign(task_heap, worker_heap, pills, strength)

    def _assign(self, task_heap, worker_heap, pills, strength):
        count = 0

        while task_heap and worker_heap:
            task = task_heap[0]
            worker, has_pill = worker_heap[0]

            if task <= worker:
                heapq.heappop(task_heap)
                heapq.heappop(worker_heap)
                count += 1
            elif pills > 0:
                heapq.heappop(worker_heap)
                count1 = self._assign(task_heap[:], worker_heap[:],
                                      pills, strength)
                count2 = 0

                if task <= worker + strength and has_pill == 0:
                    pills -= 1
                    heapq.heappush(worker_heap, (worker + strength, 1))
                    count2 = self._assign(task_heap[:], worker_heap[:],
                                          pills, strength)

                return count + max(count1, count2)
            else:
                heapq.heappop(worker_heap)

        return count
