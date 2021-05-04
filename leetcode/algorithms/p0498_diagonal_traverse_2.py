from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        result = []
        row, column = len(mat), len(mat[0])
        diagonal_to_numbers = {}

        for i in range(row):
            for j in range(column):
                p = i + j

                if p not in diagonal_to_numbers:
                    diagonal_to_numbers[p] = []

                diagonal_to_numbers[p].append(mat[i][j])

        for i in sorted(diagonal_to_numbers.keys()):
            if i & 1 == 0:
                result += list(reversed(diagonal_to_numbers[i]))
            else:
                result += diagonal_to_numbers[i]

        return result
