from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        chars = set()
        counts = {}

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)

            counts[c] = counts.get(c, 0) + 1

        if len(chars) > 1:
            return []

        middle = next(iter(chars)) if len(chars) == 1 else ''

        return self._generate(counts, middle, len(s))

    def _generate(self, counts, permutation_so_far, target_length):
        if len(permutation_so_far) == target_length:
            return [permutation_so_far]

        permutations = []

        for key in counts:
            if counts[key] <= 1:
                continue

            counts[key] -= 2
            permutations += self._generate(counts,
                                           key + permutation_so_far + key,
                                           target_length)
            counts[key] += 2

        return permutations
