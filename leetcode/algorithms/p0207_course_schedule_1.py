import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = collections.defaultdict(list)
        finished = set()

        for prerequisite in prerequisites:
            mapping[prerequisite[0]].append(prerequisite[1])

        for i in range(numCourses):
            if not self._can_finish(i, mapping, set(), finished):
                return False

        return True

    def _can_finish(self, course, mapping, visited, finished):
        if course in visited and course not in finished:
            return False

        if course in finished:
            return True

        visited.add(course)

        if course in mapping:
            for prerequisite in mapping[course]:
                if not self._can_finish(prerequisite, mapping, visited, finished):
                    return False

        finished.add(course)

        return True
