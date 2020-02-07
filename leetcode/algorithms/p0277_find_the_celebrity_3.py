def knows(a: int, b: int) -> bool:
    graph = [
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]

    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_celebrity = 0

        for i in range(1, n):
            if knows(possible_celebrity, i):
                possible_celebrity = i

        for i in range(n):
            if possible_celebrity == i:
                continue

            if knows(possible_celebrity, i) \
                    or not knows(i, possible_celebrity):
                return -1

        return possible_celebrity
