from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) \
            -> int:
        stack = []

        for position, car_speed in sorted(zip(position, speed), reverse=True):
            distance = target - position

            if not stack:
                stack.append(distance / car_speed)
            elif distance / car_speed > stack[-1]:
                stack.append(distance / car_speed)

        return len(stack)
