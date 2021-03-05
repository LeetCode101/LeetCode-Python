from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        chars = set()
        counts = {}
        used_counts = {}

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)

            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
                used_counts[c] = 0

        if len(chars) > 1:
            return []

        middle = next(iter(chars)) if len(chars) == 1 else ''
        permutations = self._generate(counts, used_counts)

        if permutations:
            return [permutation + middle + permutation[::-1]
                    for permutation in permutations]
        else:
            return [middle] if middle else []

    def _generate(self, counts, used_counts):
        permutations = []

        for key, count in counts.items():
            if count // 2 == used_counts[key]:
                continue

            used_counts[key] += 1
            rest_permutations = self._generate(counts, used_counts)

            if not rest_permutations:
                permutations += [key]
            else:
                permutations += [key + permutation
                                 for permutation in rest_permutations]

            used_counts[key] -= 1

        return permutations
