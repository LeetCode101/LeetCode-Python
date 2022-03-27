import bisect
from typing import List


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) \
            -> List[int]:
        sorted_rooms = sorted(rooms, key=lambda x: x[1], reverse=True)
        sorted_queries = sorted([[i, q] for i, q in enumerate(queries)],
                                key=lambda x: x[1][1], reverse=True)

        i = 0
        room_ids = []
        n, k = len(sorted_rooms), len(queries)
        result = [-1] * k

        for index, (preferred_room_id, min_size) in sorted_queries:
            while i < n and sorted_rooms[i][1] >= min_size:
                bisect.insort(room_ids, sorted_rooms[i][0])
                i += 1

            result[index] = self._search_closest_room_id(
                room_ids, preferred_room_id)

        return result

    def _search_closest_room_id(self, room_ids, preferred_room_id):
        if len(room_ids) == 0:
            return -1

        candidates = []
        i = bisect.bisect_right(room_ids, preferred_room_id)

        if i > 0:
            candidates.append(room_ids[i - 1])

        if i < len(room_ids):
            candidates.append(room_ids[i])

        return min(candidates, key=lambda x: abs(x - preferred_room_id))
