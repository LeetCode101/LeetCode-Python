import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        sorted_courses = sorted(courses, key=lambda x: x[1])
        total_time = 0

        for course in sorted_courses:
            total_time += course[0]
            heapq.heappush(heap, -course[0])

            if total_time > course[1]:
                total_time -= -heapq.heappop(heap)

        return len(heap)
