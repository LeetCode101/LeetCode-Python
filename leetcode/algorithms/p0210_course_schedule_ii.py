import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) \
            -> List[int]:
        dependency = collections.defaultdict(list)
        order = []
        finished = set()

        for course, prerequisite in prerequisites:
            dependency[course].append(prerequisite)

        for i in range(numCourses):
            if not self._can_finish(i, dependency, set(), finished, order):
                return []

        return order

    def _can_finish(self, course, dependency, visited, finished, order):
        if course in visited and course not in finished:
            return False

        if course in finished:
            return True

        visited.add(course)

        if course in dependency:
            for prerequisite in dependency[course]:
                if not self._can_finish(prerequisite, dependency,
                                        visited, finished, order):
                    return False

        finished.add(course)
        order.append(course)

        return True
