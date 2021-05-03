from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        visited = set()

        self._dfs(0, rooms, visited)

        return len(visited) == len(rooms)

    def _dfs(self, i, rooms, visited):
        if i in visited:
            return

        visited.add(i)

        for key in rooms[i]:
            self._dfs(key, rooms, visited)
