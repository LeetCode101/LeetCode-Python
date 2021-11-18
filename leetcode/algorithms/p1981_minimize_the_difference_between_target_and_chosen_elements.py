from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possible_sum = {0}

        for row in mat:
            current_sum = set()

            for x in possible_sum:
                for y in sorted(set(row)):
                    current_sum.add(x + y)

                    if x + y > target:
                        break

            possible_sum = current_sum

        return min(abs(x - target) for x in possible_sum)
