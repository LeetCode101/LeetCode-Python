from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        m, n = len(mat), len(mat[0])

        for i in range(m):
            count = 0

            for j in range(n):
                if mat[i][j] == 0:
                    break

                count += 1

            rows.append((count, i))

        rows.sort(key=lambda x: x[0])

        return [rows[i][1] for i in range(k)]
