import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        ugly = 1
        visited = set()

        for _ in range(n):
            ugly = heapq.heappop(ugly_numbers)

            for i in primes:
                next_ugly = ugly * i

                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly_numbers, next_ugly)

                if ugly % i == 0:
                    break

        return ugly
