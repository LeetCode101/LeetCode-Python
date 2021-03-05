from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        middle = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:middle])
        right_skyline = self.getSkyline(buildings[middle:])

        return self._merge(left_skyline, right_skyline)

    def _merge(self, left_skyline, right_skyline):
        left_height, right_height = 0, 0
        left, right = 0, 0
        result = []

        while left < len(left_skyline) and right < len(right_skyline):
            if left_skyline[left][0] < right_skyline[right][0]:
                skyline = [left_skyline[left][0],
                           max(left_skyline[left][1], right_height)]
                left_height = left_skyline[left][1]
                left += 1
            elif left_skyline[left][0] > right_skyline[right][0]:
                skyline = [right_skyline[right][0],
                           max(right_skyline[right][1], left_height)]
                right_height = right_skyline[right][1]
                right += 1
            else:
                skyline = [
                    left_skyline[left][0],
                    max(left_skyline[left][1], right_skyline[right][1])]
                left_height = left_skyline[left][1]
                right_height = right_skyline[right][1]
                left += 1
                right += 1

            if len(result) == 0 or result[-1][1] != skyline[1]:
                result.append(skyline)

        result.extend(left_skyline[left:] or right_skyline[right:])

        return result
