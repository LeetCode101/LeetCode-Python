import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = collections.Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] not in counts:
                continue

            current_counts = {}

            for j in range(i, i + len(s1)):
                if s2[j] in current_counts:
                    current_counts[s2[j]] += 1
                else:
                    current_counts[s2[j]] = 1

            if counts == current_counts:
                return True

        return False
