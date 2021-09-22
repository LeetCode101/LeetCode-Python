# Time Limit Exceeded!
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = {
            0: 'a',
            1: 'b',
            2: 'c'
        }

        return self._dfs([a, b, c], '', chars)

    def _dfs(self, counts, s, chars):
        if counts[0] == 0 and counts[1] == 0 and counts[2] == 0:
            return s

        longest = s

        for i, count in enumerate(counts):
            if count == 0 or s[-2:] == chars[i] * 2:
                continue

            new_counts = [x for x in counts]
            new_counts[i] -= 1
            current = self._dfs(new_counts, s + chars[i], chars)

            if len(current) > len(longest):
                longest = current

        return longest
