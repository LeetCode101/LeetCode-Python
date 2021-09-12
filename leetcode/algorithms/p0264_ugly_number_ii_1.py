import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        heapq.heapify(ugly_numbers)
        ugly = 1
        visited = set()

        for _ in range(n):
            ugly = heapq.heappop(ugly_numbers)

            for i in [2, 3, 5]:
                next_ugly = ugly * i

                if next_ugly not in visited:
                    visited.add(next_ugly)
                    heapq.heappush(ugly_numbers, next_ugly)

        return ugly
