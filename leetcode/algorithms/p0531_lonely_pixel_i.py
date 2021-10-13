from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        columns = [0] * n
        count = 0

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    columns[j] += 1

        for i in range(m):
            if rows[i] != 1:
                continue

            for j in range(n):
                if picture[i][j] == 'B' and columns[j] == 1:
                    count += 1

        return count
