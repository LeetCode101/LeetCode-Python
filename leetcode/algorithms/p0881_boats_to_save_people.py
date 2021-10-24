from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        sorted_people = sorted(people)
        low, high = 0, len(people) - 1

        while low <= high:
            if sorted_people[low] + sorted_people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1

            count += 1

        return count
