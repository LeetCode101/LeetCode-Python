import bisect


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.array[index] and self.array[index][-1][0] == self.snap_id:
            self.array[index].pop()

        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1

        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.array[index], [snap_id + 1]) - 1

        return self.array[index][i][1]
