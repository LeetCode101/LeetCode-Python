import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        positions = collections.defaultdict(list)

        for i, c in enumerate(s):
            positions[c].append(i)

        count = 0

        for position in positions.values():
            for i in range(len(position)):
                prev = position[i - 1] if i > 0 else -1
                next = position[i + 1] if i < len(position) - 1 else n
                count += (position[i] - prev) * (next - position[i])

        return count
