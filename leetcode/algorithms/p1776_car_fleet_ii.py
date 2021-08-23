import math
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        result = [-1] * len(cars)
        stack = []

        for i in range(len(cars) - 1, -1, -1):
            position, speed = cars[i]

            while stack and (
                    speed <= stack[-1][1]
                    or self._get_collide_time(stack, position, speed)
                    >= stack[-1][2]):
                stack.pop()

            if not stack:
                stack.append((position, speed, math.inf))
                result[i] = -1
            else:
                collide_time = self._get_collide_time(stack, position, speed)
                stack.append((position, speed, collide_time))
                result[i] = collide_time

        return result

    def _get_collide_time(self, stack, position, speed):
        return (stack[-1][0] - position) / (speed - stack[-1][1])
