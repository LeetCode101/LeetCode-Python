import collections


class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = -1
        self.array = [0] * length
        self.snaps = [collections.defaultdict(int) for _ in range(length)]
        self.set_index = set()

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        self.set_index.add(index)

    def snap(self) -> int:
        self.snap_id += 1

        for i in self.set_index:
            snap = self.snaps[i]
            snap[self.snap_id] = self.array[i]

        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[index][snap_id]
