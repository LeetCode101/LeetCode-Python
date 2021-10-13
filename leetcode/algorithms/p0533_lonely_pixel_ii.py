import collections
from typing import List


class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        row_to_column = collections.defaultdict(list)
        column_to_row = collections.defaultdict(list)

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_to_column[i].append(j)
                    column_to_row[j].append(i)

        count = 0

        for i in range(m):
            if i not in row_to_column or len(row_to_column[i]) != target:
                continue

            for j in range(len(row_to_column[i])):
                if len(column_to_row[row_to_column[i][j]]) != target:
                    continue

                is_valid = True

                for k in range(1, target):
                    row = column_to_row[row_to_column[i][j]]

                    if picture[row[k - 1]] != picture[row[k]]:
                        is_valid = False

                        break
                if is_valid:
                    count += 1

        return count
