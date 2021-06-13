from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.column = 0

    def next(self) -> int:
        if self.hasNext():
            value = self.vec[self.row][self.column]
            self.column += 1

            return value

    def hasNext(self) -> bool:
        while self.row < len(self.vec) \
                and self.column == len(self.vec[self.row]):
            self.row += 1
            self.column = 0

        return self.row < len(self.vec)
