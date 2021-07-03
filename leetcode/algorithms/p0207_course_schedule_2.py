import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) \
            -> bool:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1

        queue = collections.deque(
            [course for course, degree in enumerate(degrees) if degree == 0])

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)

        return sum(degrees) == 0
