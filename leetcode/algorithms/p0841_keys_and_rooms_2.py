from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        visited = set()
        queue = deque([0])

        while queue:
            room = queue.popleft()
            visited.add(room)

            for key in rooms[room]:
                if key in visited:
                    continue

                queue.append(key)
                visited.add(key)

        return len(visited) == len(rooms)
