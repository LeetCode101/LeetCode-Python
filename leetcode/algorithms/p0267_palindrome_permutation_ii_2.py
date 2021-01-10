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

            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        if len(chars) > 1:
            return []

        result = []
        middle = next(iter(chars)) if len(chars) == 1 else ''
        self.generate(counts, middle, result, len(s))

        return result

    def generate(self, counts, permutation_so_far, result, target_length):
        if len(permutation_so_far) == target_length:
            result.append(permutation_so_far)

        for key in counts:
            if counts[key] <= 1:
                continue

            counts[key] -= 2
            self.generate(counts, key + permutation_so_far + key, result, target_length)

            counts[key] += 2
