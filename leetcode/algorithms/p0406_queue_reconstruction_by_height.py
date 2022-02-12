from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        queue = []

        for p in sorted_people:
            queue.insert(p[1], p)

        return queue
