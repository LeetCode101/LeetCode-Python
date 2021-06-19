import bisect


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.numbers, num)

    def findMedian(self) -> float:
        size = len(self.numbers)

        return self.numbers[size // 2] if size & 1 == 1 \
            else (self.numbers[size // 2 - 1] + self.numbers[size // 2]) / 2
