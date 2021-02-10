import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = collections.Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] not in counts:
                continue

            current_counts = {}

            for j in range(i, i + len(s1)):
                current_counts[s2[j]] = current_counts.get(s2[j], 0) + 1

            if counts == current_counts:
                return True

        return False
