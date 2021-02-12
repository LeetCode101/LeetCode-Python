from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)

        for i in range(rowIndex + 1):
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = row[j - 1] + row[j]

        return row
