import collections


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv[key]
        low, high = 0, len(values)

        while low < high:
            middle = low + (high - low) // 2

            if values[middle][0] <= timestamp:
                low = middle + 1
            else:
                high = middle

        return '' if high == 0 else values[high - 1][1]
