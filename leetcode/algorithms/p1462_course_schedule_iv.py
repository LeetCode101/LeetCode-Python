import collections
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        prerequisite_courses = [set() for _ in range(numCourses)]

        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)
            degrees[course] += 1

        queue = collections.deque(
            [course for course, degree in enumerate(degrees) if degree == 0])

        while queue:
            course = queue.popleft()

            for next_course in graph[course]:
                degrees[next_course] -= 1
                prerequisite_courses[next_course].add(course)

                for prerequisite_course in prerequisite_courses[course]:
                    prerequisite_courses[next_course].add(prerequisite_course)

                if degrees[next_course] == 0:
                    queue.append(next_course)

        return [prerequisite in prerequisite_courses[course]
                for prerequisite, course in queries]
