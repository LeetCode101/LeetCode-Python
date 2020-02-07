def knows(a: int, b: int) -> bool:
    graph = [
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
        [0, 0, 0, 1]
    ]

    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_celebrities = []

        for i in range(n):
            know_someone = False

            for j in range(n):
                if i == j:
                    continue

                if knows(i, j):
                    know_someone = True

                    break

            if not know_someone:
                possible_celebrities.append(i)

        for i in possible_celebrities:
            is_celebrity = True

            for j in range(n):
                if not knows(j, i):
                    is_celebrity = False

                    break

            if is_celebrity:
                return i

        return -1
