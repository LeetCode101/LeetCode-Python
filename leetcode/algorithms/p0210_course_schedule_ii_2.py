import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) \
            -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        order = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1

        queue = collections.deque(
            [course for course, degree in enumerate(degrees) if degree == 0])

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                degrees[next_course] -= 1

                if degrees[next_course] == 0:
                    queue.append(next_course)

        return order if sum(degrees) == 0 else []
