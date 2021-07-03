import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) \
            -> bool:
        dependency = collections.defaultdict(list)
        finished = set()

        for course, prerequisite in prerequisites:
            dependency[course].append(prerequisite)

        for i in range(numCourses):
            if not self._can_finish(i, dependency, set(), finished):
                return False

        return True

    def _can_finish(self, course, dependency, visited, finished):
        if course in visited and course not in finished:
            return False

        if course in finished:
            return True

        visited.add(course)

        if course in dependency:
            for prerequisite in dependency[course]:
                if not self._can_finish(prerequisite, dependency,
                                        visited, finished):
                    return False

        finished.add(course)

        return True
