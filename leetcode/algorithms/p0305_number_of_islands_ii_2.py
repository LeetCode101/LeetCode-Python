from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.roots = [-1] * n
        self.count = 0

    def add(self, index: int):
        if self.roots[index] == -1:
            self.roots[index] = index
            self.count += 1

    def get_parent(self, index: int):
        return self.roots[index]

    def find_root(self, index: int) -> int:
        while index != self.roots[index]:
            index = self.roots[index]

        return index

    def union(self, p: int, q: int):
        p_root = self.find_root(p)
        q_root = self.find_root(q)

        if p_root == q_root:
            return

        self.roots[p_root] = q_root
        self.count -= 1

    def get_count(self):
        return self.count


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) \
            -> List[int]:
        counts = []
        uf = UnionFind(m * n)
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for position in positions:
            root = n * position[0] + position[1]

            if uf.get_parent(root) != -1:
                counts.append(uf.get_count())

                continue

            uf.add(root)

            for direction in directions:
                x = position[0] + direction[0]
                y = position[1] + direction[1]
                neighbour = n * x + y

                if x < 0 or x >= m or y < 0 or y >= n \
                        or uf.get_parent(neighbour) == -1:
                    continue

                uf.union(root, neighbour)

            counts.append(uf.get_count())

        return counts
