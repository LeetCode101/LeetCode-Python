import math
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = []
        stack = []

        for position, speed in cars[::-1]:
            while stack and (
                    speed <= stack[-1][1]
                    or self._get_collide_time(stack, position, speed)
                    >= stack[-1][2]):
                stack.pop()

            if not stack:
                stack.append((position, speed, math.inf))
                result.append(-1)
            else:
                collide_time = self._get_collide_time(stack, position, speed)
                stack.append((position, speed, collide_time))
                result.append(collide_time)

        result.reverse()

        return result

    def _get_collide_time(self, stack, position, speed):
        return (stack[-1][0] - position) / (speed - stack[-1][1])
