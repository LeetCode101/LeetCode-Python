from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        m = len(mat)

        for i in range(m):
            low, high = 0, len(mat[i]) - 1

            while low < high:
                middle = low + (high - low) // 2 + 1

                if mat[i][middle] == 1:
                    low = middle
                else:
                    high = middle - 1

            count = low + 1 if mat[i][low] == 1 else 0

            rows.append((count, i))

        rows.sort(key=lambda x: (x[0], x[1]))

        return [rows[i][1] for i in range(k)]
