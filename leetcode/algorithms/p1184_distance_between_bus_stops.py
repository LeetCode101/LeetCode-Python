from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int],
                                start: int, destination: int) -> int:
        clockwise_distance = 0
        counterclockwise_distance = 0
        start, destination = min(start, destination), max(start, destination)

        for i in range(start, destination):
            clockwise_distance += distance[i]

        i = destination

        while i != start:
            counterclockwise_distance += distance[i]
            i = (i + 1) % len(distance)

        return min(clockwise_distance, counterclockwise_distance)
