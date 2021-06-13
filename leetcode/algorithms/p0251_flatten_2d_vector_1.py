from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = self._get_next_row(vec, 0)
        self.column = 0 if self.row != -1 else -1
        self.total_row = len(vec)

    def next(self) -> int:
        value = self.vec[self.row][self.column]

        if self.column == len(self.vec[self.row]) - 1:
            if self.row == self.total_row - 1:
                self.row = -1
                self.column = -1
            else:
                self.row = self._get_next_row(self.vec, self.row + 1)
                self.column = 0 if self.row > -1 else -1
        else:
            self.column += 1

        return value

    def hasNext(self) -> bool:
        return self.row != -1 and self.column != -1

    def _get_next_row(self, vec, row):
        for i in range(row, len(vec)):
            if vec[i]:
                return i

        return -1
