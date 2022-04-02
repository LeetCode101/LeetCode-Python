import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
                            worker: List[int]) -> int:
        sorted_profit = sorted([(x, i) for i, x in enumerate(profit)],
                               reverse=True)
        sorted_worker = sorted(worker)
        worker_end = len(sorted_worker) - 1
        max_profit = 0

        for p, i in sorted_profit:
            if difficulty[i] > sorted_worker[worker_end]:
                continue

            j = bisect.bisect_left(sorted_worker, difficulty[i],
                                   lo=0, hi=worker_end + 1)
            max_profit += p * (worker_end - j + 1)
            worker_end = j - 1

        return max_profit
