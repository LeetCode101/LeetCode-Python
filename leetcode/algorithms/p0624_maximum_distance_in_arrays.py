import sys
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_value, max_value = sys.maxsize, -sys.maxsize
        min_array_index, max_array_index = 0, 0
        n = len(arrays)
        max_1, max_2 = 0, 0

        for i in range(n):
            if arrays[i][0] < min_value:
                min_value = arrays[i][0]
                min_array_index = i

            if arrays[i][-1] > max_value:
                max_value = arrays[i][-1]
                max_array_index = i

        for i in range(n):
            if i != min_array_index:
                max_1 = max(max_1, abs(min_value - arrays[i][-1]))

            if i != max_array_index:
                max_2 = max(max_2, abs(arrays[i][0] - max_value))

        return max(max_1, max_2)
