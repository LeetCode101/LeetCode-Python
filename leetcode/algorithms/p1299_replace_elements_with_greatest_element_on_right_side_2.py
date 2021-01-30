import heapq
from typing import List


class Node(object):
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        largest = [Node(-arr[i], i) for i in range(1, length)]
        heapq.heapify(largest)

        for i in range(length):
            while largest and largest[0].index <= i:
                heapq.heappop(largest)

            arr[i] = -largest[0].value if largest else -1

        return arr
