from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for row in range(9):
            for column in range(9):
                number = board[row][column]

                if number == '.':
                    continue

                box_index = (row // 3) * 3 + column // 3
                rows[row][number] = rows[row].get(number, 0) + 1
                columns[column][number] = columns[column].get(number, 0) + 1
                boxes[box_index][number] = boxes[box_index].get(number, 0) + 1

                if rows[row][number] > 1 or columns[column][number] > 1 \
                        or boxes[box_index][number] > 1:
                    return False

        return True
