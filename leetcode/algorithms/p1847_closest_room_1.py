import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) \
            -> List[int]:
        sorted_rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
        result = []

        for room_id, size in queries:
            i = self._select_left(sorted_rooms, size)
            min_abs = sys.maxsize
            min_room_id = sys.maxsize

            for j in range(i, len(rooms)):
                current_room_id = sorted_rooms[j][0]
                current_abs = abs(room_id - current_room_id)

                if current_abs < min_abs:
                    min_abs = current_abs
                    min_room_id = sorted_rooms[j][0]
                elif current_abs == min_abs and min_room_id > current_room_id:
                    min_room_id = current_room_id

            if min_abs != sys.maxsize:
                result.append(min_room_id)
            else:
                result.append(-1)

        return result

    def _select_left(self, rooms, target):
        low, high = 0, len(rooms) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if rooms[middle][1] < target:
                low = middle + 1
            else:
                high = middle - 1

        return low
