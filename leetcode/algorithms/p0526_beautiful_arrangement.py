class Solution:
    def countArrangement(self, n: int) -> int:
        return self._count_arrangement(n, 1, [False] * (n + 1))

    def _count_arrangement(self, n, start, visited):
        if start > n:
            return 1

        count = 0

        for i in range(1, n + 1):
            if visited[i]:
                continue

            visited[i] = True

            if start % i == 0 or i % start == 0:
                count += self._count_arrangement(n, start + 1, visited)

            visited[i] = False

        return count
