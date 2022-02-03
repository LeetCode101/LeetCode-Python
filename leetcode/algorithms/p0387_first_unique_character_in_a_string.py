class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrences = {}

        for i, c in enumerate(s):
            if c in occurrences:
                occurrences[c] = (occurrences[c][0] + 1, occurrences[c][1])
            else:
                occurrences[c] = (1, i)

        min_position = -1

        for occurrence in occurrences.values():
            if occurrence[0] == 1:
                if min_position == -1 or min_position > occurrence[1]:
                    min_position = occurrence[1]

        return min_position
