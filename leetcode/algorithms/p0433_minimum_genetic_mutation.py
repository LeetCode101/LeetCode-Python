import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = collections.deque([(start, 0)])
        visited = set()

        while queue:
            gene, times = queue.popleft()

            if gene == end:
                return times

            for c in ['A', 'C', 'G', 'T']:
                for i in range(len(start)):
                    if gene[i] != c:
                        new_gene = gene[:i] + c + gene[i + 1:]

                        if new_gene in bank_set and new_gene not in visited:
                            queue.append((new_gene, times + 1))
                            visited.add(new_gene)

        return -1
